import requests

def index():
    media = None
    filmes = db(db.filme.id > 0).select()
    if filmes:
        notas = [f.nota for f in filmes if f.nota is not None]
        if notas:
            media = sum(notas) / len(notas)
    return dict(filmes=filmes, media=media)

def criar():
    form = SQLFORM(db.filme)
    if form.process().accepted:
        api_key = '32f8f9c9'  
        titulo = form.vars.titulo
        r = requests.get(f'http://www.omdbapi.com/?t={titulo}&apikey={api_key}')
        if r.status_code == 200:
            data = r.json()
            if data.get('Response') == 'True':
                db(db.filme.id == form.vars.id).update(
                    ano=data.get('Year'),
                    sinopse=data.get('Plot'),
                    poster=data.get('Poster')
                )
        redirect(URL('index'))
    return dict(form=form)

def editar():
    filme_id = request.args(0, cast=int)
    form = SQLFORM(db.filme, filme_id)
    if form.process().accepted:
        redirect(URL('index'))
    return dict(form=form)

def deletar():
    filme_id = request.args(0, cast=int)
    db(db.filme.id == filme_id).delete()
    redirect(URL('index'))
