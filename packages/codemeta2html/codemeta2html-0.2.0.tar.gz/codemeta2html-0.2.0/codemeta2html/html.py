import sys
import os.path
from datetime import datetime
from collections import OrderedDict, defaultdict
import codemeta.parsers.gitapi
import unicodedata
import re
import json
from hashlib import md5
from rdflib import Graph, URIRef, BNode, Literal
#pyri
from rdflib import RDF, SKOS, RDFS, DCTERMS #type: ignore
from typing import Union, IO, Optional, Sequence, Iterator
from itertools import chain

if sys.version_info.minor < 8:
    from importlib_metadata import version as get_version  # backported
else:
    from importlib.metadata import version as get_version
from codemeta.common import (
    AttribDict,
    REPOSTATUS,
    SDO,
    CODEMETA,
    SOFTWARETYPES,
    SOFTWAREIODATA,
    TRL,
    CODEMETAPY,
    ORDEREDLIST_PROPERTIES,
    get_last_component,
    query,
    iter_ordered_list,
    get_doi,
)
import codemeta.parsers.gitapi
from jinja2 import Environment, FileSystemLoader


def get_triples(
    g: Graph,
    res: Union[URIRef, BNode, None],
    prop,
    labelprop=(SDO.name, SDO.legalName, RDFS.label, SKOS.prefLabel),
    abcsort=False,
    contextgraph: Optional[Graph] = None,
    max=0,
):
    """Get all triples for a particular resource and properties, also returns labels which are looked for in the contextgraph when needed, and handles sorting"""
    results = []
    havepos = False
    if not isinstance(labelprop, (tuple, list)):
        labelprop = (labelprop,)
    if res is not None and prop in ORDEREDLIST_PROPERTIES:
        triples = iter_ordered_list(g, res, prop)
    else:
        triples = g.triples((res, prop, None))
    for i, (_, _, res2) in enumerate(triples):
        if (
            isinstance(res2, Literal)
            and str(res2).startswith(("http", "_", "/"))
            and (URIRef(res2), None, None) in g
        ):
            # if a literals referers to an existing URI in the graph, treat it as a URIRef instead
            res2 = URIRef(str(res2))
        if isinstance(res2, Literal):
            results.append((res2, res2, 9999, 9999))
        else:
            if prop in ORDEREDLIST_PROPERTIES:
                # already returned in order
                pos = i
            else:
                # follow schema:position if available
                pos = g.value(res2, SDO.position)
                if pos is not None:
                    havepos = True
                elif isinstance(pos, int):
                    pass
                elif isinstance(pos, str):
                    pos = int(pos) if pos.isnumeric() else 9999
            label = None
            for p in labelprop:
                label = get_english_value(g,res2,p) #type: ignore
                if label:
                    break
                elif contextgraph:
                    label = get_english_value(contextgraph,res2,p) #type: ignore
            if label:
                results.append((label, res2, pos, _get_sortkey2(g, res2))) #type: ignore
            else:
                results.append((str(res2), res2, pos, _get_sortkey2(g, res2))) #type: ignore
        if max and len(results) >= max:
            break
    if havepos:
        try:
            results.sort(key=lambda x: x[2])
        except TypeError:  # protection against edge cases, leave unsorted then
            pass
    if abcsort:
        try:
            results.sort(key=lambda x: (x[0].lower(), x[3]))
        except TypeError:  # protection against edge cases, leave unsorted then
            pass
    return [tuple(x[:2]) for x in results]




def _get_sortkey2(g: Graph, res: Union[URIRef, BNode, None]):
    # set a secondary sort-key for items with the very same name
    # ensures certain interface types are listed before others in case of a tie
    if (res, RDF.type, SDO.WebApplication):
        return 0
    elif (res, RDF.type, SDO.WebSite) in g:
        return 1
    elif (res, RDF.type, SDO.WebPage) in g:
        return 3
    elif (res, RDF.type, SDO.WebAPI) in g:
        return 4
    elif (res, RDF.type, SDO.CommandLineApplication) in g:
        return 5
    else:
        return 9999


def get_index(g: Graph, restype=SDO.SoftwareSourceCode):
    groups = OrderedDict()
    for res, _, _ in g.triples((None, RDF.type, restype)):
        found = False
        label = g.value(res, SDO.name)
        if not label:
            label = g.value(res, SDO.identifier)
            if label:
                label = str(label).strip("/ \n").capitalize()
            else:
                label = "~untitled"

        for _, _, group in g.triples((res, SDO.applicationSuite, None)):
            groups.setdefault((str(group), True), []).append(
                (res, str(label))
            )  # explicit group
            found = True

        if not found:
            # ad-hoc group (singleton)
            group = str(label)
            groups.setdefault((group, False), []).append(
                (res, str(label))
            )  # ad-hoc group

    for key in groups:
        groups[key].sort(key=lambda x: x[1].lower())

    return sorted(
        ((k[0], k[1], v) for k, v in groups.items()), key=lambda x: x[0].lower()
    )


def is_resource(res) -> bool:
    return isinstance(res, (URIRef, BNode))


def get_badge(g: Graph, res: Union[URIRef, None], key):
    source = str(g.value(res, SDO.codeRepository)).strip("/")
    cleaned_url = source
    prefix = ""
    if source.startswith("https://"):
        repo_kind = codemeta.parsers.gitapi.get_repo_kind(source)
        git_address = cleaned_url.replace("https://", "").split("/")[0]
        prefix = "https://"
        git_suffix = cleaned_url.replace(prefix + git_address, "")[1:]
        if "github" == repo_kind:
            # github badges
            if key == "stars":
                yield f"https://img.shields.io/github/stars/{git_suffix}.svg?style=flat&color=5c7297", None, "Stars are an indicator of the popularity of this project on GitHub"
            elif key == "issues":
                # https://shields.io/category/issue-tracking
                yield f"https://img.shields.io/github/issues/{git_suffix}.svg?style=flat&color=5c7297", None, "The number of open issues on the issue tracker"
                yield f"https://img.shields.io/github/issues-closed/{git_suffix}.svg?style=flat&color=5c7297", None, "The number of closes issues on the issue tracker"
            elif key == "lastcommits":
                yield f"https://img.shields.io/github/last-commit/{git_suffix}.svg?style=flat&color=5c7297", None, "Last commit (main branch). Gives an indication of project development activity and rough indication of how up-to-date the latest release is."
                yield f"https://img.shields.io/github/commits-since/{git_suffix}/latest.svg?style=flat&color=5c7297&sort=semver", None, "Number of commits since the last release. Gives an indication of project development activity and rough indication of how up-to-date the latest release is."
        elif "gitlab" == repo_kind:
            # https://docs.gitlab.com/ee/api/project_badges.html
            # https://github.com/Naereen/badges
            if key == "lastcommits":
                # append all found badges at the end
                encoded_git_suffix = git_suffix.replace("/", "%2F")
                response = codemeta.parsers.gitapi.rate_limit_get(
                    f"{prefix}{git_address}/api/v4/projects/{encoded_git_suffix}/badges",
                    "gitlab",
                )
                if response:
                    response = response.json() #type: ignore
                    for badge in response:
                        if badge["kind"] == "project":
                            # or rendered_image_url field?
                            image_url = badge["image_url"]
                            name = badge["name"]
                            yield f"{image_url}", f"{name}", f"{name}"


def has_actionable_targetapps(g: Graph, res: Union[URIRef, BNode]) -> bool:
    for _, _, targetres in g.triples((res, CODEMETA.isSourceCodeOf, None)):
        if (targetres, SDO.url, None) in g:
            return True
    return False


def has_displayable_targetapps(g: Graph, res: Union[URIRef, BNode]) -> bool:
    for _, _, targetres in g.triples((res, CODEMETA.isSourceCodeOf, None)):
        if (
            (targetres, SDO.url, None) in g
            or (targetres, SDO.name, None) in g
            or (targetres, SOFTWARETYPES.executableName, None) in g
        ):
            return True
    return False


def type_label(g: Graph, res: Union[URIRef, None]) -> str:
    label = g.value(res, RDF.type)
    if label:
        label = str(label).split("/")[-1]
        return label
    else:
        return ""


def get_interface_types(
    g: Graph, res: Union[URIRef, None], contextgraph: Graph, fallback=False
):
    """Returns labels and definitions (2-tuple) for the interface types that this SoftwareSourceCode resource provides"""
    types = set()
    for _, _, res3 in g.triples((res, RDF.type, None)):
        if res3 != SDO.SoftwareSourceCode:
            stype = contextgraph.value(res3, RDFS.label)
            comment = contextgraph.value(res3, RDFS.comment)  # used for definitions
            if stype:
                types.add((stype, comment))
    for _, _, res2 in g.triples((res, CODEMETA.isSourceCodeOf, None)):
        for _, _, res3 in g.triples((res2, RDF.type, None)):
            stype = contextgraph.value(res3, RDFS.label)
            comment = contextgraph.value(res3, RDFS.comment)  # used for definitions
            if stype:
                types.add((stype, comment))

    if not types and fallback:
        types.add(
            (
                "Unknown",
                "Sorry, we don't know what kind of interfaces this software provides. No interface types have been specified or could be automatically extracted.",
            )
        )
    return list(sorted(types))


def get_filters(
    g: Graph, res: Union[URIRef, None], contextgraph: Graph, json_filterables=False
) -> Union[str, list]:
    classes = defaultdict(set)
    sort_order = ["interfacetype", "developmentstatus","trl", "metadatarating", "category"]
    for interfacetype, description in get_interface_types(
        g, res, contextgraph, fallback=True
    ):
        if json_filterables:
            classes["interfacetype"].add(slugify(interfacetype, "interfacetype"))
        else:
            classes["interfacetype"].add(
                (
                    slugify(interfacetype, "interfacetype"),
                    interfacetype,
                    description,
                    "Interface type",
                )
            )

    for _, _, devstatres in g.triples((res, CODEMETA.developmentStatus, None)):
        if str(devstatres).startswith(REPOSTATUS):
            filter_id = "developmentstatus"
            filter_label = "Development status"
        elif str(devstatres).startswith(TRL):
            filter_id = "trl"
            filter_label = "Technology Readiness Level"
        else:
            continue
        if json_filterables:
            classes[filter_id].add(
                slugify(str(devstatres), filter_id)
            )
        else:
            devstatlabel = get_label(contextgraph, devstatres) #type: ignore
            devstatdesc = get_description(contextgraph, devstatres) #type: ignore
            classes[filter_id].add(
                (
                    slugify(str(devstatres), filter_id),
                    devstatlabel,
                    devstatdesc,
                    filter_label,
                )
            )

    if json_filterables:
        for _, _, review in g.triples((res, SDO.review, None)):
            if str(g.value(review, SDO.name)).startswith("Automatic software metadata validation report"):
                if (review, SDO.reviewRating, None) in g:
                    rating = int(g.value(review, SDO.reviewRating))
                    classes["metadatarating"].add(slugify(str(rating), "metadatarating"))
    else:
        classes["metadatarating"].add((slugify("0", "metadatarating"), "0 - ☆☆☆☆☆ (worst)", "No or hardly any software metadata provided", "Metadata Quality"))
        classes["metadatarating"].add((slugify("1", "metadatarating"), "1 - ★☆☆☆☆ (bad)", "Too little metadata has been provided", "Metadata Quality"))
        classes["metadatarating"].add((slugify("2", "metadatarating"), "2 - ★★☆☆☆ (minimal)", "Some metadata has been provided but significant fields are missing still", "Metadata Quality"))
        classes["metadatarating"].add((slugify("3", "metadatarating"), "3 - ★★★☆☆ (ok)", "Acceptable metadata quality", "Metadata Quality"))
        classes["metadatarating"].add((slugify("4", "metadatarating"), "4 - ★★★★☆ (good)", "Good metadata quality", "Metadata Quality"))
        classes["metadatarating"].add((slugify("5", "metadatarating"), "5 - ★★★★★ (best))", "Excellent metadata quality", "Metadata Quality"))


    for _, _, catres in g.triples((res, SDO.applicationCategory, None)):
        if not isinstance(catres, URIRef) and str(catres).startswith("http"): #this is a bit of an ugly patch, shouldn't be neede
            catres = URIRef(catres) #type: ignore
        if (catres, SKOS.inScheme, None) in contextgraph:
            scheme = contextgraph.value(catres, SKOS.inScheme)
            if not isinstance(scheme, URIRef) and str(scheme).startswith("http"): #this is a bit of an ugly patch, shouldn't be needed
                scheme = URIRef(scheme) #type: ignore
            filter_id = md5(str(scheme).encode('utf-8')).hexdigest()
            if not json_filterables:
                filter_label = get_label(contextgraph,scheme) #type: ignore  
                if filter_label == str(scheme):
                    filter_label = f"Category ({str(scheme)})"
                else:
                    filter_label = f"Category ({filter_label})"
                if filter_id not in sort_order:
                    sort_order.insert(sort_order.index("category"), filter_id)
        else:
            filter_id = "category"
            filter_label = "Category (unassorted schemes)"
        if json_filterables:
            classes[filter_id].add(slugify(str(catres), filter_id))
        else:
            catlabel = get_label(contextgraph, catres) #type: ignore
            catdesc = get_description(contextgraph, catres) #type: ignore
            classes[filter_id].add(
                (slugify(str(catres), filter_id), catlabel, catdesc, filter_label) #type: ignore
            )

    sort_order.append("keywords")
    for _, _, keyword in g.triples((res, SDO.keywords, None)):
        if json_filterables:
            classes["keywords"].add(slugify(str(keyword), "keywords"))
        else:
            classes["keywords"].add(
                (slugify(str(keyword), "keywords"), str(keyword).lower(), "", "Keywords")
            )

    if json_filterables:
        for key in classes:
            classes[key] = list( #type: ignore
                classes[key]
            )  # sets are not json serializable, so make it into a list
        return json.dumps(classes, ensure_ascii=False).replace('"', "'")
    else:
        for key in classes:
            l = list(classes[key])
            l.sort(key=lambda x: x[1])
            classes[key] = l #type: ignore

        return sorted(classes.items(), key=lambda x: sort_order.index(x[0]))


def get_english_value(g: Graph, s: Union[URIRef,BNode], p: URIRef, default="") -> str:
    result = default
    for _,_,candidate in g.triples((s,p,None)):
        if isinstance(candidate, Literal) and candidate.language in (None,'en'): #hard-coded english for now
            result = candidate
            break
    return result


def get_label(g: Graph, res: URIRef) -> str:
    for prop in (SKOS.prefLabel, SKOS.altLabel, SDO.name, DCTERMS.title, RDFS.label):
        label = get_english_value(g,res, prop)
        if label: 
            return label
    return str(res)

def get_description(g: Graph, res: URIRef) -> str:
    for prop in (SKOS.definition, SKOS.note, SDO.description, DCTERMS.description):
        desc = get_english_value(g,res, prop)
        if desc: 
            return desc
    return ""


def slugify(s: str, prefix: str) -> str:
    slug = unicodedata.normalize("NFKD", s.lower())
    slug = re.sub(r"[^a-z0-9]+", "_", slug).strip("-")
    slug = re.sub(r"[_]+", "_", slug)
    if len(slug) > 30:
        slug = md5(slug.encode("utf-8")).hexdigest()
    return prefix + "_" + slug


def get_target_platforms(g: Graph, res: Union[URIRef, None]):
    types = set()
    for label, _ in get_triples(g, res, SDO.runtimePlatform):
        label = label.lower().split(" ")[0]
        types.add(label.capitalize())
    for label, _ in get_triples(g, res, SDO.operatingSystem):
        label = label.lower().split(" ")[0]
        types.add(label.capitalize())
    return list(sorted(types))


def serialize_to_html(
    g: Graph,
    res: Union[Sequence, URIRef, None],
    args: AttribDict,
    contextgraph: Graph,
    sparql_query: Optional[str] = None,
    **kwargs,
) -> str:
    """Serialize to HTML with RDFa"""
    rootpath = sys.modules["codemeta2html"].__path__[0]
    env = Environment(
        loader=FileSystemLoader(os.path.join(rootpath, "templates")),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    # env.policies['json.dumps_kwargs']['ensure_ascii'] = False
    # env.policies['json.dumps_function'] = to_json
    if res and not isinstance(res, (list, tuple)):
        assert isinstance(res, URIRef) or res is None
        if (res, RDF.type, SDO.SoftwareSourceCode) in g:
            template = "page_softwaresourcecode.html"
        elif (
            (res, RDF.type, SDO.SoftwareApplication) in g
            or (res, RDF.type, SDO.WebPage) in g
            or (res, RDF.type, SDO.WebSite) in g
            or (res, RDF.type, SDO.WebAPI) in g
            or (res, RDF.type, SOFTWARETYPES.CommandLineApplication) in g
            or (res, RDF.type, SOFTWARETYPES.SoftwareLibrary) in g
        ):
            template = "page_targetproduct.html"
        elif (res, RDF.type, SDO.Person) in g or (res, RDF.type, SDO.Organization):
            template = "page_person_or_org.html"
        else:
            template = "page_generic.html"
        index = []
    else:
        template = kwargs.get("indextemplate", "index.html")
        if isinstance(res, (list, tuple)):
            index = [
                ("Selected resource(s)", True, [(x, g.value(x, SDO.name)) for x in res])
            ]
            res = None
        elif sparql_query:
            index = query(g, sparql_query)
            index = [("Search results", True, index)]
        else:
            index = get_index(g)
    template = env.get_template(template)
    return template.render(
        g=g,
        res=res,
        SDO=SDO,
        CODEMETA=CODEMETA,
        CODEMETAPY=CODEMETAPY,
        RDF=RDF,
        RDFS=RDFS,
        STYPE=SOFTWARETYPES,
        SOFTWAREIODATA=SOFTWAREIODATA,
        REPOSTATUS=REPOSTATUS,
        SKOS=SKOS,
        TRL=TRL,
        get_triples=get_triples,
        get_description=get_description,
        get_target_platforms=get_target_platforms,
        type_label=type_label,
        styledir=args.styledir,
        css=args.css,
        contextgraph=contextgraph,
        URIRef=URIRef,
        get_badge=get_badge,
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        index=index,
        get_interface_types=get_interface_types,
        get_filters=get_filters,
        baseuri=args.baseuri,
        baseurl=args.baseurl,
        buildsite=args.buildsite,
        serverside=args.serverside,
        link_resource=link_resource,
        intro=args.intro,
        get_last_component=get_last_component,
        is_resource=is_resource,
        int=int,
        range=range,
        str=str,
        Literal=Literal,
        get_version=get_version,
        chain=chain,
        get_doi=get_doi,
        has_actionable_targetapps=has_actionable_targetapps,
        has_displayable_targetapps=has_displayable_targetapps,
        **kwargs,
    )


def to_json(o, **kwargs):
    result = json.dumps(o, ensure_ascii=False, indent=None)
    result.replace('"', "'")
    return result


def link_resource(g: Graph, res: URIRef, baseuri: Optional[str], format="html", anchor="") -> str:
    """produces a link to a resource page"""
    link = str(res)  # fallback
    if baseuri:
        link = str(res).replace(
            baseuri, ""
        )  # we remove the (absolute) baseuri and rely on baseurl set in html/head/base
    elif (res, SDO.identifier, None) in g:
        pos = str(res).find("/" + str(g.value(res, SDO.identifier)))
        if pos > -1:
            link = str(res)[pos + 1 :]
        elif str(res).startswith(("https://", "http://")):
            link = "/".join(str(res).split("/")[3:])
    if link and link[-1] != "/":
        link += "/"
    if format != "html":
        link += f"data.{format}"
    if anchor:
        link += f"#{anchor}"
    return link
