# acpcweb
academic curriculum proof copy web

# truncade cascade all tables
SELECT 'TRUNCATE TABLE ' ||  tablename || ';'
FROM pg_tables
WHERE tableowner='acpc'
	and tablename like 'trabalhos_%'

TRUNCATE TABLE trabalhos_tag cascade;
TRUNCATE TABLE trabalhos_eventotrabalho cascade;
TRUNCATE TABLE trabalhos_entidade cascade;
TRUNCATE TABLE trabalhos_trabalho cascade;
TRUNCATE TABLE trabalhos_arquivo cascade;
TRUNCATE TABLE trabalhos_evento cascade;
TRUNCATE TABLE trabalhos_natureza cascade;