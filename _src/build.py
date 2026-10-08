# _src/src.html に FX（おいわいの 演出）を うめこんで index.html を つくる
import io, os
here = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(here, 'src.html'), encoding='utf-8').read()
fx = io.open(os.path.join(here, 'fx.js'), encoding='utf-8').read()
assert '/*FX_HERE*/' in src
out = src.replace('/*FX_HERE*/', fx.strip())
io.open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8', newline='\n').write(out)
print('built', len(out))
