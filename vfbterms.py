import sys
from os import listdir, chdir
from os.path import isfile, join
from vfb_connect.cross_server_tools import VfbConnect


def build_index(src, key, dest, path=[]):
    for k, v in src.iteritems():
        fv = path+[v]
        if isinstance(v, dict):
            build_index(v, key, dest, fv)
        else:
            if key == k:
                try:
                    dest[v].append(fv)
                except KeyError:
                    dest[v] = [fv]


def wrapStringInHTMLMac(term):
    import datetime
    import json
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = term["term"]["core"]["short_form"] + ".md"
    f = open(filename, "w", encoding="utf-8")
    note = """
{{% alert title="Note" color="primary" %}}This page displays the raw VFB json record for this term. Please use the link below to open the term inside the Virtual Fly Brain viewer{{% /alert %}}
    """
    wrapper = """---
    title: "{0} [{1}]"
    tags: [{4}]
    content: [term]
    date: {7}
    description: >
        {2} {3}
---

{8}

<span style="font-size:larger;">[Open **{0}** in **VFB**](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id={1})</span>


## VFB Term Json

```json
{5}
```
## Available images
<a href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id={1}">
{6}
</a>

    """
    folders=[]
    build_index(term, "image_folder", folders)
    images = ""
    for folder in folders:
        images += '<img src="' + folder + 'thumbnail.png" alt="drawing" width="200"/>'
    print(images)
    whole = wrapper.format(term["term"]["core"]["label"],term["term"]["core"]["short_form"],' '.join(term["term"]["description"]),' '.join(term["term"]["comment"]),','.join(term["term"]["core"]["types"]),json.dumps(term, indent=4),images,now,note)
    try:
        f.write(whole)
    except:
        print(whole)
    f.close()


vc = VfbConnect()

mypath = sys.argv[1]
print("Updating all files in " + mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

chdir(mypath)

all = sorted([w.replace(".md", "") for w in onlyfiles if w.startswith("FBbt")])
for id in all:
    print(id)
    terms = vc.neo_query_wrapper.get_TermInfo([id])
    for term in terms:
        wrapStringInHTMLMac(term)
