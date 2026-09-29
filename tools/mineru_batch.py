import os, sys, subprocess, glob, shutil, re
M_KIT="/Volumes/D/toolchain-cache/mineru-venv/bin/mineru-kit"
D="/Users/aurolafly/Collected-Papers-of-Fields-Medalists"
LOG="/tmp/mineru_batch.log"
def log(m):
    with open(LOG,"a") as f: f.write(m+"\n")
def pages_of(p):
    try:
        out=subprocess.run(["pdfinfo",p],capture_output=True,text=True).stdout
        for l in out.split("\n"):
            if l.startswith("Pages:"): return int(l.split()[-1])
    except: pass
    return 0

files=[]
for root,dirs,fs in os.walk(D):
    if "/." in root: continue
    for f in fs:
        if f.lower().endswith(".pdf"):
            p=os.path.join(root,f)
            base=f[:-4]
            md=os.path.join(root, base+".md")
            has_md = any(x.lower()==(base+".md").lower() for x in fs)
            files.append((pages_of(p), p, base, has_md))
files.sort()
log(f"START {len(files)} files")

for n,p,base,has_md in files:
    d=os.path.dirname(p)
    mdir=os.path.join(d, base+"_mineru")
    md_ready=os.path.isdir(mdir) and len(glob.glob(os.path.join(mdir,"**","*.md"),recursive=True))>0
    if has_md or md_ready:
        log(f"SKIP {base} (md exists)"); continue
    log(f"PARSE {base} ({n}p)")
    expdir="/tmp/mexp_"+re.sub(r'\W','_',base)[:30]
    shutil.rmtree(expdir, ignore_errors=True); os.makedirs(expdir, exist_ok=True)
    ok=False
    if n>200:
        # split 180-page parts
        partdir="/tmp/msplit_"+re.sub(r'\W','_',base)[:20]
        shutil.rmtree(partdir, ignore_errors=True); os.makedirs(partdir)
        part=1; start=1
        while start<=n:
            end=min(start+179, n)
            outp=os.path.join(partdir, f"part{part:02d}.pdf")
            subprocess.run(["gs","-q","-dNOPAUSE","-dBATCH","-sDEVICE=pdfwrite",
                            f"-sOutputFile={outp}",f"-dFirstPage={start}",f"-dLastPage={end}",p],
                           check=False)
            r=subprocess.run([M_KIT,"parse",outp,"-o",expdir,"--format","zip","--remote",
                              "-p",f"1-{end-start+1}"],capture_output=True,text=True)
            start=end+1; part+=1
        ok=True
        parts_done=True
    else:
        r=subprocess.run([M_KIT,"parse",p,"-o",expdir,"--format","zip","--remote",
                          "-p",f"1-{n}"],capture_output=True,text=True)
        ok = r.returncode==0
    zips=glob.glob(os.path.join(expdir,"*.zip"))
    if zips:
        dest=os.path.join(d, base+"_mineru")
        os.makedirs(dest, exist_ok=True)
        for z in zips:
            zn=os.path.basename(z)[:-4]
            zd=os.path.join(dest, zn)
            os.makedirs(zd, exist_ok=True)
            subprocess.run(["unzip","-qo",z,"-d",zd],check=False)
            md=os.path.join(zd,"markdown.md")
            if os.path.exists(md):
                os.replace(md, os.path.join(dest, f"{base}__{zn}.md"))
        for z in zips: os.remove(z)
        log(f"EXPORT OK {base} ({len(zips)} zips)")
    else:
        log(f"EXPORT FAIL {base}")
log("ALL DONE")
