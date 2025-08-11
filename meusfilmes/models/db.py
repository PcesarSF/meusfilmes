# Conexão com o banco
db = DAL('sqlite://storage.sqlite')

# Definição da tabela Filme
db.define_table('filme',
    Field('titulo', 'string', requires=IS_NOT_EMPTY()),
    Field('ano', 'string'),
    Field('nota', 'double'),
    Field('sinopse', 'text'),
    Field('poster', 'string')
)

# Rotular campos
db.filme.titulo.label = 'Título'
db.filme.ano.label = 'Ano'
db.filme.nota.label = 'Nota'
db.filme.sinopse.label = 'Sinopse'
db.filme.poster.label = 'URL do Poster'

db.commit()
