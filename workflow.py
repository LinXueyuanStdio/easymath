# -*- coding: utf-8 

import markdown
import os
import sys
from importlib import reload
reload(sys)


class MathProof():
    def __init__(self, proof=""):
        self.mathProof = proof
        
    def proof(self, *args):
        for s in args:
            self.mathProof += s+"\n"
        print(self.mathProof)
        f = open("proof.html", "a")
        f.write(self.md2html(self.mathProof))
        f.close()
        print("proof success! \nPlease open file proof.html")
        
    def md2html(self, mdstr):
        exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

        html = '''
        <html lang="zh-cn">
        <head>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <link href="default.css" rel="stylesheet">
        <link href="github.css" rel="stylesheet">
        </head>
        <body>
        %s
        </body>
    <!--使markdown支持latex-->
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            jax: ["input/TeX", "output/HTML-CSS"],
            tex2jax: {
                inlineMath: [ ['$', '$'] ],
                displayMath: [ ['$$', '$$']],
                processEscapes: true,
                skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
            },
            messageStyle: "none",
            "HTML-CSS": { preferredFont: "TeX", availableFonts: ["STIX","TeX"] }
        });
    </script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js"></script>
        </html>
       '''

        ret = markdown.markdown(mdstr,extensions=exts)
        return html % ret
