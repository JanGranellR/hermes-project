dataset = {
    "path": "./data",
    "path_raw": "raw",
    "path_processed": "processed",
    "path_cache": "cache",
    "path_train": "train",
    "path_test": "test",
    "webs": [
        # Astronomy
        {
            "category": "astronomy",
            "name": "astroblog",
            "url": "http://astroblog.cl/feed/",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "universo_rayado",
            "url": "http://feeds.feedburner.com/naukas/universorayado",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "universidad_de_salamanca",
            "url": "https://diarium.usal.es/guillermo/category/astronomia/feed/",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "entry"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "astrobitos",
            "url": "https://astrobitos.org/feed/rss/",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post_text"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "noticias_de_la_ciencia",
            "url": "https://noticiasdelaciencia.com/rss/ciencia-astron-y-espacio",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "new_text"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "novaciencia",
            "url": "https://novaciencia.es/rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "td-post-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
       {
            "category": "astronomy",
            "name": "bbc_news",
            "url": "https://www.bbc.com/mundo/temas/ciencia/index.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//ns:entry/ns:link/@href",
            "options": {
                "container": "main",
                "container_attrs": {"role": "main"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "el_pais",
            "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/ciencia/portada",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"data-dtm-region": "articulo_cuerpo"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "el_pais",
            "url": "https://e00-elmundo.uecdn.es/blogs/elmundo/cosmos/index.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "tamano"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
         {
            "category": "astronomy",
            "name": "astroaficion",
            "url": "https://astroaficion.com/rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
         {
            "category": "astronomy",
            "name": "wired",
            "url": "https://es.wired.com/feed/ciencia/rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "body__inner-container"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "rtve",
            "url": "https://www.rtve.es/api/tematicas/1067/noticias.rss",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "artBody"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "surastronomico",
            "url": "http://www.surastronomico.com/rss/actualidad.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "mainContent"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "ialp_fcaglp_unlp",
            "url": "https://ialp.fcaglp.unlp.edu.ar/blog/feed",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "diario_sur",
            "url": "https://www.diariosur.es/rss/atom/?section=ciencia/espacio",
             "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//ns:entry/ns:link/@href",
            "options": {
                "container": "div",
                "container_attrs": {"class": "v-d--ab-c"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "reino_de_las_estrellas",
            "url": "https://www.reinodelasestrellas.com/feed/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
          {
            "category": "astronomy",
            "name": "astronomia_y_algo_mas",
            "url": "http://astroblog.cl/feed/podcast",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
         {
            "category": "astronomy",
            "name": "astronomia_amateur",
            "url": "https://aporcel.wordpress.com/feed/", 
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
          {
            "category": "astronomy",
            "name": "facultad_de_ciencias_astronomicas_y_geofisicas",
            "url": "https://www.fcaglp.unlp.edu.ar/rss", 
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//ns:entry/ns:link/@href",
            "options": {    
                "container": "div",
                "container_attrs": {"class": "body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "no_cierres_los_ojos",
            "url": "http://www.nocierreslosojos.com/category/astronomia/feed/", 
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {    
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "astronomy",
            "name": "universidad_pablo_de_olavide",
            "url": "https://www.upo.es/diario/tag/astronomia/rss", 
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {    
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
       
        #Ocio
         {
            "category": "play",
            "name": "diario_de_leon",
            "url": "https://www.diariodeleon.es/rss/ocio.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "div",
                "container_attrs": {"class": "c-detail__body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300,
        },
        {
            "category": "play",
            "name": "diario_de_sevilla",
            "url": "https://www.diariodesevilla.es/rss/ocio/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "div",
                "container_attrs": {"class":"mce-body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300,
        },
        {
            "category": "play",
            "name": "diario_de_sevilla",
            "url": "https://www.diariodesevilla.es/rss/television/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "div",
                "container_attrs": {"class":"mce-body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300,
        },
        
        {
            "category": "play",
            "name": "sensacine",
            "url": "https://www.sensacine.com/rss/noticias.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "article",
                "container_attrs": {"class": "article-container"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300,
        },
        {
            "category": "play",
            "name": "sensacine",
            "url": "https://www.sensacine.com/rss/noticias-cine.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "article",
                "container_attrs": {"class": "article-container"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300,
        },
        {
            "category": "play",
            "name": "sensacine",
            "url": "https://www.sensacine.com/rss/noticias-series.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "article",
                "container_attrs": {"class": "article-container"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300,
        },
        {
            "category": "play",
            "name": "vidaextra",
            "url": "https://www.vidaextra.com/feedburner.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 400,
        },
        {
            "category": "play",
            "name": "de_lector_a_lector",
            "url": "https://www.delectoralector.com/rss",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "div",
                "container_attrs": {"class": "et_pb_post_content_0_tb_body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300,
        },
       {
            "category": "play",
            "name": "espinof",
            "url": "https://www.espinof.com/categoria/estrenos/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
           "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 600,
        },
       {
            "category": "play",
            "name": "abc",
            "url": "https://www.abc.es/rss/2.0/play/series/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "article",
                "container_attrs": {"class": "voc-d__article"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "play",
            "name": "abc",
            "url": "https://www.abc.es/rss/2.0/play/cine/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "article",
                "container_attrs": {"class": "voc-d__article"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "play",
            "name": "abc",
            "url": "https://www.abc.es/rss/2.0/play/television/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "article",
                "container_attrs": {"class": "voc-d__article"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "play",
            "name": "abc",
            "url": "https://www.epe.es/es/rss/ocio/rss.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "article",
                "container_attrs": {"class": "ft-layout-grid-flex__row"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
         {
            "category": "play",
            "name": "el_periodico",
            "url": "https://www.elperiodico.com/es/rss/videos/ocio-y-cultura/rss.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
           "options": {
                "container": "div",
                "container_attrs": {"class": "ep-detail-body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        
         # Religion
         {
            "category": "religion",
            "name": "cnnespanol",
            "url": "https://cnnespanol.cnn.com/category/religion/rss/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "story-body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
          {
            "category": "religion",
            "name": "vidanuevadigital",
            "url": "https://www.vidanuevadigital.com/feed/",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
         {
            "category": "religion",
            "name": "religiondigital",
            "url": "https://www.religiondigital.org/rss/",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "mce-body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "bbc_news",
            "url": "https://www.bbc.com/mundo/temas/religion/index.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//ns:entry/ns:link/@href",
            "options": {
                "container": "main",
                "container_attrs": {"role": "main"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
        },
        {
            "category": "religion",
            "name": "vidanuevadigital",
            "url": "https://www.europapress.es/rss/rss.aspx?buscar=iglesia-catolica",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "texto_noticia"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
         {
            "category": "religion",
            "name": "vatican_news",
            "url": "https://www.vaticannews.va/es.rss.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {    
                "container": "div",
                "container_attrs": {"class": "article__text"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "el_confidencial_digital",
            "url": "https://religion.elconfidencialdigital.com/rss/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/portada.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/articulos.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/lo-mas-leido.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/ciencia_y_fe.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/nueva_evangelizacion.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
         {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/papa_francisco.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/cultura.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/mundo.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/personajes.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
         {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/vida_familia.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/historias/historias_de_evangelizacion.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/vaticano.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
          {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/noticias/polemicas.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "religion_en_libertad",
            "url": "https://www.religionenlibertad.com/rss/historias/historias_de_conversion.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "Contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "aci_prensa",
            "url": "http://feeds.feedburner.com/noticiasaci-espana",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "aci_prensa",
            "url": "http://feeds.feedburner.com/noticiasaci-vaticano",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "aci_prensa",
            "url": "http://feeds.feedburner.com/noticiasaci-vidayfamilia",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "aci_prensa",
            "url": "http://feeds.feedburner.com/noticiasaci-mundo",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "aci_prensa",
            "url": "http://feeds.feedburner.com/noticiasaci-eventoscatolicos",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "aci_prensa",
            "url": "http://feeds.feedburner.com/noticiasaci-internet",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "post-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
         {
            "category": "religion",
            "name": "islam_news",
            "url": "https://www.islamnews.es/rss/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "religion",
            "name": "islam_news",
            "url": "https://www.islamnews.es/rss/comunidad/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        
        {
            "category": "religion",
            "name": "okdiario",
            "url": "https://okdiario.com/noticias/budismo/rss",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
          {
            "category": "religion",
            "name": "okdiario",
            "url": "https://okdiario.com/noticias/religion/rss",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "entry-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
          {
            "category": "religion",
            "name": "biblicamente",
            "url": "https://www.biblicamente.org/rss/falacias-ateas.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "wrapperContent" },
                "elements_to_extract": "p",
                "elements_ignore_last": True
            }
        },
        {
            "category": "religion",
            "name": "biblicamente",
            "url": "https://www.biblicamente.org/rss/la-biblia-en-las-noticias-actuales.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "wrapperContent" },
                "elements_to_extract": "p",
                "elements_ignore_last": True
            }
        },
        {
            "category": "religion",
            "name": "christianpost",
            "url": "https://spanish.christianpost.com/feed.xml?category=iglesia-ministerio",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "article",
                "container_attrs": { "class": "full-article" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "https://es.catholic.net/rss/sectas.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "https://es.catholic.net/rss/virtudesyvalores.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "https://es.catholic.net/rss/mariologia.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "https://es.catholic.net/rss/evangelio.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "https://es.catholic.net/rss/religiosas.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "https://es.catholic.net/rss/clero.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "https://es.catholic.net/rss/vaticano.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "http://es.catholic.net/rss/familiayvida.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "religion",
            "name": "catholic",
            "url": "http://es.catholic.net/rss/conocetufe.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "art_texto" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },

        # Motor
        {
            "category": "motor",
            "name": "coches_net",
            "url": "https://www.coches.net/noticias/rss/?idTipo=3",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "mt-DocumentContentful"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "coches_net",
            "url": "https://www.coches.net/noticias/rss/?idTipo=2",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "mt-DocumentContentful"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "coches_net",
            "url": "https://www.coches.net/noticias/rss/?idTipo=4",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "mt-DocumentContentful"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "es_motor1",
            "url": "https://es.motor1.com/rss/category/actualidad/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "postBody"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "es_motor1",
            "url": "https://es.motor1.com/rss/articles/all/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "postBody"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "motor_es",
            "url": "https://www.motor.es/feed/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"id": "content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "el_periodico",
            "url": "https://www.elperiodico.com/es/rss/motor/rss.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "infomotor",
            "url": "https://www.infomotor.es/rss/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "inner-article-data"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "marca",
            "url": "https://e00-marca.uecdn.es/rss/motor/modelos-coches.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "article",
                "container_attrs": {"class": "news-item"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "el_pais",
            "url": "https://motor.elpais.com/rss",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "content__main__content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "el_mundo",
            "url": "https://e00-elmundo.uecdn.es/elmundomotor/rss/portada.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "ue-c-article__body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "car_and_driver",
            "url": "https://www.caranddriver.com/es/rss/all.xml/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "main",
                "container_attrs": {"id": "main-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "autobild",
            "url": "https://www.autobild.es/rss",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "article",
                "container_attrs": {"id": "page-article"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "motorpasion",
            "url": "https://www.motorpasion.com/feedburner.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "autopista_es",
            "url": "https://www.autopista.es/uploads/feeds/feed_autopista_es.xml",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "c-mainarticle__body"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "autofacil",
            "url": "https://www.autofacil.es/rss",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "modulo-noticia--contenido"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "el_confidencial",
            "url": "https://rss.elconfidencial.com/deportes/formula-1/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//entry/id/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "news-body-complete"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "highmotor",
            "url": "https://www.highmotor.com/rss",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "content-single"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "motor",
            "name": "abc",
            "url": "https://www.abc.es/rss/2.0/motor/",
            "namespace": {"ns": "http://www.w3.org/2005/Atom"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "article",
                "container_attrs": {"class": "voc-d__article"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },

         # Alimentation
          {
            "category": "alimentation",
            "name": "el_pais",
            "url": "https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/gastronomia",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"data-dtm-region": "articulo_cuerpo"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 500
       },
        {
            "category": "alimentation",
            "name": "directo_al_paladar",
            "url": "https://www.directoalpaladar.com/categoria/utensilios/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 250
        },
        {
            "category": "alimentation",
            "name": "directo_al_paladar",
            "url": "https://www.directoalpaladar.com/categoria/ingredientes-y-alimentos/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 350
        },
        {
            "category": "alimentation",
            "name": "directo_al_paladar",
            "url": "https://www.directoalpaladar.com/categoria/cultura-gastronomica/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
             "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300
        },
        {
            "category": "alimentation",
            "name": "directo_al_paladar",
            "url": "https://www.directoalpaladar.com/categoria/recetario/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
            "limit": 300
        },
        
        # Tech
        {
            "category": "tech",
            "name": "topes_de_gama",
            "url": "https://feeds.feedburner.com/topesdegama",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "full-text"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "tech",
            "name": "el_periodico",
            "url": "https://www.elperiodico.com/es/rss/tecnologia/rss.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "tech",
            "name": "el_economista",
            "url": "https://www.eleconomista.es/rss/rss-category.php?category=tecnologia",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "Article__paragraphGroup"},
                "elements_to_extract": "p",
                "elements_ignore_last": False,
            },
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/moviles/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit":200,
        },  
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/ordenadores/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/perifericos/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/robotica-e-ia/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/tablets/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/historia-tecnologica/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/realidad-virtual-aumentada/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/relojes-inteligentes/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/wearables/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/domotica-1/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/drones/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/internet-of-things/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/criptomonedas/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },
        {
            "category": "tech",
            "name": "xataka",
            "url": "https://www.xataka.com/categoria/inteligencia-artificial/sitemap.xml",
            "namespace": {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
            "xpath": "//ns:url/ns:loc/text()",
            "options": {
                "container": "div",
                "container_attrs": {"class": "article-content"},
                "elements_to_extract": "p",
                "elements_ignore_last": True,
            },
            "limit": 200,
        },

        # Medicine
        {
            "category": "medicine", # This one was scraped using a different technique
            "name": "portales_medicos",
            "url": "https://www.portalesmedicos.com",
            "ignore": True
        },

        # Military
        {
            "category": "military",
            "name": "el_confidencial_digital",
            "url": "https://www.elconfidencialdigital.com/rss/defensa/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "military",
            "name": "galaxia_militar",
            "url": "https://galaxiamilitar.es/feed/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "entry-content" },
                "elements_to_extract": "p",
                "elements_ignore_last": True
            }
        },
        {
            "category": "military",
            "name": "defensa",
            "url": "https://www.defensa.com/rss/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "entry-content" },
                "elements_to_extract": "span",
                "elements_ignore_last": False
            }
        },

        # Politics
        {
            "category": "politics",
            "name": "ceuta_actualidad",
            "url": "https://www.ceutaactualidad.com/rss/politica1/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "el_confidencial_digital",
            "url": "https://www.elconfidencialdigital.com/rss/politica/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "anroca",
            "url": "https://www.anroca.com.ar/rss/politica",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "contenido" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "el_diario_cantabria",
            "url": "https://eldiariocantabria.publico.es/rss/politica/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "content-body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "el_diario",
            "url": "https://www.eldiario.es/rss/politica",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-page__body-row" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "diario_critico",
            "url": "https://red.diariocritico.com/rss/seccion/39/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "textoNoticia" },
                "elements_to_extract": ["div", "p"],
                "elements_ignore_last": True
            }
        },
        {
            "category": "politics",
            "name": "la_politica_online",
            "url": "https://www.lapoliticaonline.com/files/rss/politica.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "vsmcontent" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "es_diario",
            "url": "https://www.esdiario.com/rss/andalucia/politica-andalucia.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "card-body-article" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "clarin",
            "url": "https://www.clarin.com/rss/politica/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "StoryTextContainer" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "el_periodico_de_espana",
            "url": "https://www.epe.es/es/rss/politica/rss.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "el_periodico",
            "url": "https://www.elperiodico.com/es/rss/politica/rss.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "politics",
            "name": "la_vanguardia",
            "url": "https://www.lavanguardia.com/rss/politica.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-modules" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },

        # Fashion
        {
            "category": "fashion",
            "name": "el_dia",
            "url": "https://www.eldia.es/rss/section/12701",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-body" },
                "elements_to_extract": "p",
                "elements_ignore_last": True
            }
        },
        {
            "category": "fashion",
            "name": "el_periodico_de_aragon",
            "url": "https://www.elperiodicodearagon.com/rss/section/23589",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "atalayar",
            "url": "https://www.atalayar.com/rss/moda/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "espana_diario",
            "url": "https://espanadiario.tips/rss/tag/moda",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "content_text" },
                "elements_to_extract": "p",
                "elements_ignore_last": True
            }
        },
        {
            "category": "fashion",
            "name": "mun_diario",
            "url": "https://www.mundiario.com/rss/moda/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "diez_minutos",
            "url": "https://www.diezminutos.es/rss/moda-belleza.xml/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-body-content" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "mujer_hoy",
            "url": "https://www.mujerhoy.com/rss/2.0/?section=moda/novias",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "voc-detail" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "mujer_hoy",
            "url": "https://www.mujerhoy.com/rss/2.0/?section=moda/pasarelas",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "voc-detail" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "mujer_hoy",
            "url": "https://www.mujerhoy.com/rss/2.0/?section=moda/no-te-pierdas",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "voc-detail" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "mujer_hoy",
            "url": "https://www.mujerhoy.com/rss/2.0/?section=moda/tendencias",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "voc-detail" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "lula_logy",
            "url": "https://www.lulalogy.com/feed/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "sq-post-content" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "vanitatis",
            "url": "https://rss.vanitatis.elconfidencial.com/estilo/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//ns:entry/ns:id/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "news-body-cc" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "el_mira",
            "url": "https://www.elmira.es/rss/moda/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "moda_punta",
            "url": "https://www.modapunta.com/rss/seccion/15/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "textoNoticia" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "moda_punta",
            "url": "https://www.modapunta.com/rss/seccion/4/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "textoNoticia" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "fashion_network",
            "url": "https://es.fashionnetwork.com/rss/feed/es,2,114.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/guid/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "newsContent" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "fashion_network",
            "url": "https://es.fashionnetwork.com/rss/feed/es,2,70.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/guid/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "newsContent" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "fashion_network",
            "url": "https://es.fashionnetwork.com/rss/feed/es,2,60.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/guid/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "newsContent" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "fashion",
            "name": "telva",
            "url": "https://e00-telva.uecdn.es/rss/moda.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/guid/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ue-c-article__body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },

        # Economy
        {
            "category": "economy",
            "name": "investing",
            "url": "https://es.investing.com/rss/news_301.rss",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "WYSIWYG" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "investing",
            "url": "https://es.investing.com/rss/news_1.rss",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "WYSIWYG" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "investing",
            "url": "https://es.investing.com/rss/news_95.rss",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "WYSIWYG" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "investing",
            "url": "https://es.investing.com/rss/news_14.rss",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "WYSIWYG" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "investing",
            "url": "https://es.investing.com/rss/news_25.rss",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "WYSIWYG" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "diario_cordoba",
            "url": "https://www.diariocordoba.com/rss/section/19019",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "diario_de_sevilla",
            "url": "https://www.diariodesevilla.es/rss/economia/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "mce-body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "el_periodico_de_aragon",
            "url": "https://www.elperiodicodearagon.com/rss/section/23503",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ft-layout-grid-flex__colXs-12 ft-layout-grid-flex__colSm-11" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "es_diario",
            "url": "https://www.esdiario.com/rss/economia/economia.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "card-body-article" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "la_vanguardia",
            "url": "https://www.lavanguardia.com/rss/economia.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-modules" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "el_diario",
            "url": "https://www.eldiario.es/rss/economia",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-page__body-row" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "libertad_digital",
            "url": "http://feeds2.feedburner.com/libertaddigital/economia",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "content" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "el_economista",
            "url": "https://www.eleconomista.es/rss/rss-economia.php",
            "namespace": { "ns": "http://www.sitemaps.org/schemas/sitemap/0.9" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "id": "cuerpo_noticia" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "el_mundo_financiero",
            "url": "https://www.elmundofinanciero.com/rss/seccion/21/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "contenidoAmpliable" },
                "elements_to_extract": ["p", "span"],
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "europapress",
            "url": "https://www.europapress.es/rss/rss.aspx?ch=136",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "texto_noticia" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "economy",
            "name": "la_informacion",
            "url": "https://www.lainformacion.com/rss/economia-negocios-y-finanzas/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "article-text" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },

        # Sports
        {
            "category": "sport",
            "name": "diario_as",
            "url": "https://feeds.as.com/mrss-s/pages/as/site/as.com/section/futbol/subsection/segunda/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "art__bo" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "sport",
            "name": "diario_as",
            "url": "https://feeds.as.com/mrss-s/pages/as/site/as.com/section/baloncesto/subsection/acb/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "art__bo" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "sport",
            "name": "diario_as",
            "url": "https://feeds.as.com/mrss-s/pages/as/site/as.com/section/baloncesto/subsection/nba/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "art__bo" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "sport",
            "name": "diario_as",
            "url": "https://feeds.as.com/mrss-s/pages/as/site/as.com/section/tenis/subsection/masters_1000/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "art__bo" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "sport",
            "name": "diario_as",
            "url": "https://feeds.as.com/mrss-s/pages/as/site/as.com/section/tenis/subsection/mas_tenis/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "art__bo" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "sport",
            "name": "diario_as",
            "url": "https://feeds.as.com/mrss-s/pages/as/site/as.com/section/masdeporte/subsection/atletismo/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "art__bo" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "sport",
            "name": "diario_as",
            "url": "https://feeds.as.com/mrss-s/pages/as/site/as.com/section/masdeporte/subsection/balonmano/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "art__bo" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "sport",
            "name": "diario_as",
            "url": "https://feeds.as.com/mrss-s/pages/as/site/as.com/section/futbol/subsection/primera/",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "art__bo" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        },
        {
            "category": "sport",
            "name": "el_pais",
            "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/deportes/portada",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//guid/text()",
            "options": {
                "container": "div",
                "container_attrs": { "data-dtm-region": "articulo_cuerpo" },
                "elements_to_extract": "p",
                "elements_ignore_last": True
            }
        },
        {
            "category": "sport",
            "name": "marca",
            "url": "https://e00-marca.uecdn.es/rss/portada.xml",
            "namespace": { "ns": "http://www.w3.org/2005/Atom" },
            "xpath": "//item/link/text()",
            "options": {
                "container": "div",
                "container_attrs": { "class": "ue-c-article__body" },
                "elements_to_extract": "p",
                "elements_ignore_last": False
            }
        }
    ],
    "headers": {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
    },
    "split_ratio": 0.8,
    "limit": 1_000
}

model = {
    "path": "./data",
    "path_model": "model",
    "nnet": {
        "path": "nnet",
        "name": "model.h5"
    },
    "svm": {
        "path": "svm",
        "name": "model.joblib"
    },
    "forest": {
        "path": "forest",
        "name": "model.joblib"
    },
    "decision": {
        "path": "decision",
        "name": "model.joblib"
    }
}