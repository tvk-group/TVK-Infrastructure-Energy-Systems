"""Non-English locale bundles for TVK Partner Portal app i18n."""

HREFS = ["/energy-systems", "/infrastructure", "/strategic-partnerships", "/insights"]
EMAILS = ["partners@tvk.group", "invest@tvk.group", "support@tvk.group", "contact@tvk.group"]
STAGE_KEYS = ["development", "development", "active"]


def make_docs(items):
    return [{"title": t, "description": d, "href": h} for (t, d), h in zip(items, HREFS)]


def make_channels(items):
    return [{"title": t, "description": d, "email": e} for (t, d), e in zip(items, EMAILS)]


def make_projects(items):
    return [
        {"title": t, "stage": s, "stageKey": k, "description": d}
        for (t, s, d), k in zip(items, STAGE_KEYS)
    ]


def bundle(header_pp, header_app, footer_pp, app):
    return {
        "header": {"partnerPortal": header_pp, "getApp": header_app},
        "footer": {"partnerPortal": footer_pp},
        "app": app,
    }


LOCALE_BUNDLES = {}

LOCALE_BUNDLES["de"] = bundle(
    "Partner Portal", "App herunterladen", "Partner Portal App →",
    {
        "meta": {"title": "Partner Portal", "description": "Partnerportal von TVK Infrastructure & Energy Systems — beantragen Sie strategische Partnerschaften, verfolgen Sie Entwicklungsinitiativen und greifen Sie auf Kompetenzdokumente zu."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Website",
        "navAria": "Partnerportal-Navigation",
        "nav": {"dashboard": "Dashboard", "apply": "Bewerben", "projects": "Projekte", "documents": "Dokumente", "support": "Support"},
        "dashboard": {
            "title": "Partner-Dashboard",
            "subtitle": "Verfolgen Sie Ihre Partnerschaftsanfrage, Entwicklungsinitiativen und nächste Schritte innerhalb des TVK Ecosystem.",
            "stats": [{"label": "Partnerschaftsphase", "value": "Entwicklung"}, {"label": "Aktive Initiativen", "value": "6 Bereiche"}, {"label": "Anfragestatus", "value": "Offen"}, {"label": "Portalsprachen", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline strategischer Partnerschaften", "badge": "In Entwicklung", "description": "TVK Infrastructure & Energy Systems befindet sich in einer Phase der Forschung, Entwicklung und des Aufbaus von Partnerschaften. Reichen Sie eine Bewerbung ein, um ein strukturiertes Kooperationsgespräch zu beginnen."},
            "nextSteps": {"title": "Empfohlene nächste Schritte", "items": ["Reichen Sie eine Bewerbung für eine strategische Partnerschaft mit den Details Ihrer Organisation ein", "Prüfen Sie Kompetenzbereiche in Energiesystemen und Infrastrukturtechnologien", "Erkunden Sie aktive Entwicklungsinitiativen im Bereich Projekte", "Kontaktieren Sie unser Partnerschaftsteam für Pilot- oder Kooperationsmöglichkeiten"]},
            "cta": "Partnerschaftsbewerbung einreichen →",
        },
        "apply": {"title": "Partnerschaftsbewerbung", "subtitle": "Bewerben Sie sich für eine strategische Zusammenarbeit mit TVK Infrastructure & Energy Systems.", "intro": "Füllen Sie dieses Formular aus, um Ihre Organisation vorzustellen und Ihr Partnerschaftsinteresse zu beschreiben. Unser Team prüft alle Bewerbungen und antwortet qualifizierten Anfragen.", "disclaimer": "Diese Bewerbung stellt keine verbindliche Vereinbarung dar. TVK Infrastructure & Energy Systems LTD befindet sich in einer Entwicklungsphase — die Informationen beschreiben Kompetenzbereiche, keine operativen Verpflichtungen."},
        "applyForm": {
            "interestAreas": ["Energiesysteme", "Infrastrukturtechnologien", "Industrielle Lösungen", "Energy Intelligence", "KI-Infrastruktur", "Strategische Partnerschaften", "Allgemeine Anfrage"],
            "success": {"title": "Bewerbung erhalten", "message": "Vielen Dank für Ihr Partnerschaftsinteresse. Unser Team wird Ihre Bewerbung prüfen und innerhalb von 5–10 Werktagen antworten."},
            "fields": {"name": "Vollständiger Name", "company": "Organisation", "role": "Position / Titel", "country": "Land", "email": "E-Mail", "interest": "Partnerschaftsbereich", "allocation": "Indikativer Umfang (USD oder Beschreibung)", "message": "Partnerschaftsvorschlag", "required": "*"},
            "placeholders": {"name": "Ihr vollständiger Name", "company": "Name der Organisation", "role": "Ihre Position", "country": "Land des Betriebs", "email": "professionell@unternehmen.com", "interest": "Bereich auswählen", "allocation": "z. B. Pilotprojekt, 500.000 USD Kooperation, Technologieintegration", "message": "Beschreiben Sie Ihre Organisation, strategische Passung und vorgeschlagene Zusammenarbeit..."},
            "submit": "Partnerschaftsbewerbung einreichen",
        },
        "projects": {"title": "Entwicklungsinitiativen", "subtitle": "Aktuelle Kompetenzbereiche und Initiativen in der Entwicklungsphase innerhalb des TVK Ecosystem.", "items": make_projects([("Integration von Energiesystemen", "In Entwicklung", "Integration erneuerbarer Energien, industrielle Energielösungen und intelligente Energiemanagement-Frameworks."), ("Intelligente Infrastrukturtechnologien", "Forschung", "Digitale Infrastruktursysteme, Überwachungsplattformen und Entwicklung kritischer Infrastrukturtechnologien."), ("Industrielle KI & Analytik", "Aktive Forschung", "Industrielle KI, Infrastrukturanalytik und Forschung zu intelligenter Automatisierung für komplexe Betriebsumgebungen.")])},
        "documents": {"title": "Kompetenzdokumente", "subtitle": "Offizielle Kompetenzübersichten und Referenzmaterialien von der Unternehmenswebsite.", "openLabel": "Dokument öffnen", "items": make_docs([("Energiesystem-Kompetenzen", "Überblick über Energiesystementwicklung, Integration erneuerbarer Energien und Energy Intelligence."), ("Infrastrukturtechnologien", "Intelligente Infrastruktur, digitale Systeme und Entwicklung kritischer Infrastrukturtechnologien."), ("Strategische Partnerschaften", "Partnerschaftsmodelle, Kooperationsrahmen und Engagementprozess."), ("Einblicke & Forschung", "Branchenperspektiven zu Energie, Infrastruktur und Industrietechnologie.")])},
        "support": {"title": "Partner-Support", "subtitle": "Kontaktieren Sie das Team von TVK Infrastructure & Energy Systems für Partnerschafts-, technische und allgemeine Anfragen.", "disclaimer": "Bei dringenden operativen Angelegenheiten wenden Sie sich an Ihren zuständigen Partnerschaftsvertreter. Antwortzeiten: 1–2 Werktage für allgemeine Anfragen.", "channels": make_channels([("Partnerschaftsanfragen", "Strategische Zusammenarbeit, Pilotmöglichkeiten und langfristige Partnerschaftsentwicklung."), ("Investor Relations", "Kapitalbildung und strategische Investitionsgespräche innerhalb des TVK Ecosystem."), ("Technischer Support", "Portalzugang, Bewerbungsstatus und technische Fragen."), ("Allgemeiner Kontakt", "Allgemeine Anfragen zu TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Partner Portal App", "title": "Holen Sie sich die TVK Partner Portal App", "subtitle": "Installieren Sie das Partnerschaftsportal auf Ihrem Telefon — bewerben Sie sich, verfolgen Sie Initiativen und greifen Sie über ein Home-Screen-Symbol auf Kompetenzdokumente zu. Funktioniert heute über Zum Home-Bildschirm; App-Store-Eintrag für Phase 2 geplant.", "openApp": "Partner Portal öffnen", "howToInstall": "So installieren Sie", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Partner Portal öffnen → Teilen → Zum Home-Bildschirm"}, "android": {"title": "Android", "steps": "Chrome → Partner Portal öffnen → Menü → App installieren oder Zum Startbildschirm hinzufügen"}, "desktop": {"title": "Desktop", "steps": "Chrome oder Edge → Installationssymbol in der Adressleiste oder Partner Portal als Lesezeichen speichern"}},
    },
)

LOCALE_BUNDLES["fr"] = bundle(
    "Partner Portal", "Télécharger l'application", "Application Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Portail partenaires de TVK Infrastructure & Energy Systems — postulez pour des partenariats stratégiques, suivez les initiatives de développement et accédez aux documents de compétences."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Site web",
        "navAria": "Navigation du portail partenaires",
        "nav": {"dashboard": "Tableau de bord", "apply": "Postuler", "projects": "Projets", "documents": "Documents", "support": "Assistance"},
        "dashboard": {
            "title": "Tableau de bord partenaire",
            "subtitle": "Suivez votre demande de partenariat, les initiatives de développement et les prochaines actions au sein du TVK Ecosystem.",
            "stats": [{"label": "Phase de partenariat", "value": "Développement"}, {"label": "Initiatives actives", "value": "6 domaines"}, {"label": "Statut de la demande", "value": "Ouvert"}, {"label": "Langues du portail", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline de partenariats stratégiques", "badge": "En développement", "description": "TVK Infrastructure & Energy Systems est en phase de recherche, de développement et de construction de partenariats. Soumettez une candidature pour entamer une conversation de collaboration structurée."},
            "nextSteps": {"title": "Prochaines étapes recommandées", "items": ["Soumettez une candidature de partenariat stratégique avec les détails de votre organisation", "Consultez les domaines de compétences en systèmes énergétiques et technologies d'infrastructure", "Explorez les initiatives de développement actives dans la section projets", "Contactez notre équipe partenariats pour des opportunités de pilote ou de collaboration"]},
            "cta": "Soumettre une candidature de partenariat →",
        },
        "apply": {"title": "Candidature de partenariat", "subtitle": "Postulez pour une collaboration stratégique avec TVK Infrastructure & Energy Systems.", "intro": "Complétez ce formulaire pour présenter votre organisation et décrire votre intérêt pour un partenariat. Notre équipe examine toutes les candidatures et répond aux demandes qualifiées.", "disclaimer": "Cette candidature ne constitue pas un accord contraignant. TVK Infrastructure & Energy Systems LTD est en phase de développement — les informations décrivent des domaines de compétences, et non des engagements opérationnels."},
        "applyForm": {
            "interestAreas": ["Systèmes énergétiques", "Technologies d'infrastructure", "Solutions industrielles", "Energy Intelligence", "Infrastructure IA", "Partenariats stratégiques", "Demande générale"],
            "success": {"title": "Candidature reçue", "message": "Merci pour votre intérêt pour un partenariat. Notre équipe examinera votre candidature et répondra sous 5 à 10 jours ouvrables."},
            "fields": {"name": "Nom complet", "company": "Organisation", "role": "Fonction / Titre", "country": "Pays", "email": "E-mail", "interest": "Domaine de partenariat", "allocation": "Portée indicative (USD ou description)", "message": "Proposition de partenariat", "required": "*"},
            "placeholders": {"name": "Votre nom complet", "company": "Nom de l'organisation", "role": "Votre poste", "country": "Pays d'activité", "email": "professionnel@entreprise.com", "interest": "Sélectionner un domaine", "allocation": "p. ex. Projet pilote, collaboration de 500 000 USD, intégration technologique", "message": "Décrivez votre organisation, l'adéquation stratégique et la collaboration proposée..."},
            "submit": "Soumettre la candidature de partenariat",
        },
        "projects": {"title": "Initiatives de développement", "subtitle": "Domaines de compétences actuels et initiatives en phase de développement au sein du TVK Ecosystem.", "items": make_projects([("Intégration des systèmes énergétiques", "En développement", "Intégration des énergies renouvelables, solutions énergétiques industrielles et cadres de gestion intelligente de l'énergie."), ("Technologies d'infrastructure intelligente", "Recherche", "Systèmes d'infrastructure numérique, plateformes de surveillance et développement de technologies d'infrastructure critique."), ("IA industrielle et analytique", "Recherche active", "IA industrielle, analytique d'infrastructure et recherche en automatisation intelligente pour des environnements opérationnels complexes.")])},
        "documents": {"title": "Documents de compétences", "subtitle": "Notes de compétences officielles et documents de référence du site corporate.", "openLabel": "Ouvrir le document", "items": make_docs([("Compétences en systèmes énergétiques", "Aperçu du développement des systèmes énergétiques, de l'intégration des renouvelables et de l'Energy Intelligence."), ("Technologies d'infrastructure", "Infrastructure intelligente, systèmes numériques et développement de technologies d'infrastructure critique."), ("Partenariats stratégiques", "Modèles de partenariat, cadres de collaboration et processus d'engagement."), ("Perspectives et recherche", "Points de vue sectoriels sur l'énergie, l'infrastructure et la technologie industrielle.")])},
        "support": {"title": "Assistance partenaires", "subtitle": "Contactez l'équipe TVK Infrastructure & Energy Systems pour les demandes de partenariat, techniques et générales.", "disclaimer": "Pour les questions opérationnelles urgentes, contactez votre représentant partenariat assigné. Délais de réponse : 1 à 2 jours ouvrables pour les demandes générales.", "channels": make_channels([("Demandes de partenariat", "Collaboration stratégique, opportunités pilotes et développement de partenariats à long terme."), ("Relations investisseurs", "Formation de capital et discussions d'investissement stratégique au sein du TVK Ecosystem."), ("Assistance technique", "Accès au portail, statut de candidature et questions techniques."), ("Contact général", "Demandes générales concernant TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Application Partner Portal", "title": "Obtenez l'application TVK Partner Portal", "subtitle": "Installez le portail partenaires sur votre téléphone — postulez, suivez les initiatives et accédez aux documents de compétences depuis une icône d'écran d'accueil. Fonctionne dès aujourd'hui via Ajouter à l'écran d'accueil ; publication sur l'App Store prévue pour la phase 2.", "openApp": "Ouvrir Partner Portal", "howToInstall": "Comment installer", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Ouvrir Partner Portal → Partager → Sur l'écran d'accueil"}, "android": {"title": "Android", "steps": "Chrome → Ouvrir Partner Portal → menu → Installer l'application ou Ajouter à l'écran d'accueil"}, "desktop": {"title": "Bureau", "steps": "Chrome ou Edge → icône d'installation dans la barre d'adresse, ou ajoutez Partner Portal aux favoris"}},
    },
)

LOCALE_BUNDLES["es"] = bundle(
    "Partner Portal", "Descargar la app", "App Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Portal de socios de TVK Infrastructure & Energy Systems — solicite alianzas estratégicas, siga iniciativas de desarrollo y acceda a documentos de capacidades."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Sitio web",
        "navAria": "Navegación del portal de socios",
        "nav": {"dashboard": "Panel", "apply": "Solicitar", "projects": "Proyectos", "documents": "Documentos", "support": "Soporte"},
        "dashboard": {
            "title": "Panel de socios",
            "subtitle": "Siga su consulta de alianza, iniciativas de desarrollo y próximas acciones dentro del TVK Ecosystem.",
            "stats": [{"label": "Etapa de alianza", "value": "Desarrollo"}, {"label": "Iniciativas activas", "value": "6 áreas"}, {"label": "Estado de consulta", "value": "Abierto"}, {"label": "Idiomas del portal", "value": "25"}],
            "partnershipStatus": {"title": "Canal de alianzas estratégicas", "badge": "En desarrollo", "description": "TVK Infrastructure & Energy Systems se encuentra en una etapa de investigación, desarrollo y construcción de alianzas. Envíe una solicitud para iniciar una conversación de colaboración estructurada."},
            "nextSteps": {"title": "Próximos pasos recomendados", "items": ["Envíe una solicitud de alianza estratégica con los datos de su organización", "Revise las áreas de capacidades en sistemas energéticos y tecnologías de infraestructura", "Explore iniciativas de desarrollo activas en la sección de proyectos", "Contacte a nuestro equipo de alianzas para oportunidades piloto o de colaboración"]},
            "cta": "Enviar solicitud de alianza →",
        },
        "apply": {"title": "Solicitud de alianza", "subtitle": "Solicite colaboración estratégica con TVK Infrastructure & Energy Systems.", "intro": "Complete este formulario para presentar su organización y describir su interés en una alianza. Nuestro equipo revisa todas las solicitudes y responde a consultas calificadas.", "disclaimer": "Esta solicitud no constituye un acuerdo vinculante. TVK Infrastructure & Energy Systems LTD está en etapa de desarrollo — la información describe áreas de capacidades, no compromisos operativos."},
        "applyForm": {
            "interestAreas": ["Sistemas energéticos", "Tecnologías de infraestructura", "Soluciones industriales", "Energy Intelligence", "Infraestructura de IA", "Alianzas estratégicas", "Consulta general"],
            "success": {"title": "Solicitud recibida", "message": "Gracias por su interés en una alianza. Nuestro equipo revisará su solicitud y responderá en 5–10 días hábiles."},
            "fields": {"name": "Nombre completo", "company": "Organización", "role": "Cargo / Título", "country": "País", "email": "Correo electrónico", "interest": "Área de alianza", "allocation": "Alcance indicativo (USD o descripción)", "message": "Propuesta de alianza", "required": "*"},
            "placeholders": {"name": "Su nombre completo", "company": "Nombre de la organización", "role": "Su cargo", "country": "País de operación", "email": "profesional@empresa.com", "interest": "Seleccionar un área", "allocation": "p. ej. Proyecto piloto, colaboración de 500.000 USD, integración tecnológica", "message": "Describa su organización, encaje estratégico y colaboración propuesta..."},
            "submit": "Enviar solicitud de alianza",
        },
        "projects": {"title": "Iniciativas de desarrollo", "subtitle": "Áreas de capacidades actuales e iniciativas en etapa de desarrollo dentro del TVK Ecosystem.", "items": make_projects([("Integración de sistemas energéticos", "En desarrollo", "Integración de renovables, soluciones energéticas industriales y marcos de gestión inteligente de la energía."), ("Tecnologías de infraestructura inteligente", "Investigación", "Sistemas de infraestructura digital, plataformas de monitorización y desarrollo de tecnologías de infraestructura crítica."), ("IA industrial y analítica", "Investigación activa", "IA industrial, analítica de infraestructura e investigación en automatización inteligente para entornos operativos complejos.")])},
        "documents": {"title": "Documentos de capacidades", "subtitle": "Informes oficiales de capacidades y materiales de referencia del sitio corporativo.", "openLabel": "Abrir documento", "items": make_docs([("Capacidades en sistemas energéticos", "Resumen del desarrollo de sistemas energéticos, integración de renovables y Energy Intelligence."), ("Tecnologías de infraestructura", "Infraestructura inteligente, sistemas digitales y desarrollo de tecnologías de infraestructura crítica."), ("Alianzas estratégicas", "Modelos de alianza, marcos de colaboración y proceso de participación."), ("Perspectivas e investigación", "Perspectivas sectoriales sobre energía, infraestructura y tecnología industrial.")])},
        "support": {"title": "Soporte para socios", "subtitle": "Contacte al equipo de TVK Infrastructure & Energy Systems para consultas de alianzas, técnicas y generales.", "disclaimer": "Para asuntos operativos urgentes, contacte a su representante de alianzas asignado. Tiempos de respuesta: 1–2 días hábiles para consultas generales.", "channels": make_channels([("Consultas de alianzas", "Colaboración estratégica, oportunidades piloto y desarrollo de alianzas a largo plazo."), ("Relaciones con inversores", "Formación de capital y conversaciones de inversión estratégica dentro del TVK Ecosystem."), ("Soporte técnico", "Acceso al portal, estado de solicitud y preguntas técnicas."), ("Contacto general", "Consultas generales sobre TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "App Partner Portal", "title": "Obtenga la app TVK Partner Portal", "subtitle": "Instale el portal de socios en su teléfono — solicite, siga iniciativas y acceda a documentos de capacidades desde un icono de pantalla de inicio. Funciona hoy mediante Añadir a pantalla de inicio; publicación en App Store prevista para la fase 2.", "openApp": "Abrir Partner Portal", "howToInstall": "Cómo instalar", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Abrir Partner Portal → Compartir → Añadir a pantalla de inicio"}, "android": {"title": "Android", "steps": "Chrome → Abrir Partner Portal → menú → Instalar app o Añadir a pantalla de inicio"}, "desktop": {"title": "Escritorio", "steps": "Chrome o Edge → icono de instalación en la barra de direcciones, o guarde Partner Portal en favoritos"}},
    },
)

LOCALE_BUNDLES["it"] = bundle(
    "Partner Portal", "Scarica l'app", "App Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Portale partner di TVK Infrastructure & Energy Systems — candidati per partnership strategiche, monitora le iniziative di sviluppo e accedi ai documenti sulle competenze."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Sito web",
        "navAria": "Navigazione portale partner",
        "nav": {"dashboard": "Dashboard", "apply": "Candidati", "projects": "Progetti", "documents": "Documenti", "support": "Supporto"},
        "dashboard": {
            "title": "Dashboard partner",
            "subtitle": "Monitora la tua richiesta di partnership, le iniziative di sviluppo e le prossime azioni all'interno del TVK Ecosystem.",
            "stats": [{"label": "Fase di partnership", "value": "Sviluppo"}, {"label": "Iniziative attive", "value": "6 aree"}, {"label": "Stato richiesta", "value": "Aperto"}, {"label": "Lingue del portale", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline di partnership strategiche", "badge": "In sviluppo", "description": "TVK Infrastructure & Energy Systems è in una fase di ricerca, sviluppo e costruzione di partnership. Invia una candidatura per avviare una conversazione di collaborazione strutturata."},
            "nextSteps": {"title": "Prossimi passi consigliati", "items": ["Invia una candidatura di partnership strategica con i dettagli della tua organizzazione", "Esamina le aree di competenza nei sistemi energetici e nelle tecnologie infrastrutturali", "Esplora le iniziative di sviluppo attive nella sezione progetti", "Contatta il nostro team partnership per opportunità pilota o di collaborazione"]},
            "cta": "Invia candidatura di partnership →",
        },
        "apply": {"title": "Candidatura di partnership", "subtitle": "Candidati per una collaborazione strategica con TVK Infrastructure & Energy Systems.", "intro": "Compila questo modulo per presentare la tua organizzazione e descrivere il tuo interesse per una partnership. Il nostro team esamina tutte le candidature e risponde alle richieste qualificate.", "disclaimer": "Questa candidatura non costituisce un accordo vincolante. TVK Infrastructure & Energy Systems LTD è in fase di sviluppo — le informazioni descrivono aree di competenza, non impegni operativi."},
        "applyForm": {
            "interestAreas": ["Sistemi energetici", "Tecnologie infrastrutturali", "Soluzioni industriali", "Energy Intelligence", "Infrastruttura IA", "Partnership strategiche", "Richiesta generale"],
            "success": {"title": "Candidatura ricevuta", "message": "Grazie per il tuo interesse nella partnership. Il nostro team esaminerà la tua candidatura e risponderà entro 5–10 giorni lavorativi."},
            "fields": {"name": "Nome completo", "company": "Organizzazione", "role": "Ruolo / Titolo", "country": "Paese", "email": "Email", "interest": "Area di partnership", "allocation": "Ambito indicativo (USD o descrizione)", "message": "Proposta di partnership", "required": "*"},
            "placeholders": {"name": "Il tuo nome completo", "company": "Nome dell'organizzazione", "role": "La tua posizione", "country": "Paese di operatività", "email": "professionale@azienda.com", "interest": "Seleziona un'area", "allocation": "es. Progetto pilota, collaborazione da 500.000 USD, integrazione tecnologica", "message": "Descrivi la tua organizzazione, l'allineamento strategico e la collaborazione proposta..."},
            "submit": "Invia candidatura di partnership",
        },
        "projects": {"title": "Iniziative di sviluppo", "subtitle": "Aree di competenza attuali e iniziative in fase di sviluppo all'interno del TVK Ecosystem.", "items": make_projects([("Integrazione dei sistemi energetici", "In sviluppo", "Integrazione delle rinnovabili, soluzioni energetiche industriali e framework di gestione intelligente dell'energia."), ("Tecnologie di infrastruttura intelligente", "Ricerca", "Sistemi di infrastruttura digitale, piattaforme di monitoraggio e sviluppo di tecnologie per infrastrutture critiche."), ("IA industriale e analitica", "Ricerca attiva", "IA industriale, analitica infrastrutturale e ricerca sull'automazione intelligente per ambienti operativi complessi.")])},
        "documents": {"title": "Documenti sulle competenze", "subtitle": "Brief ufficiali sulle competenze e materiali di riferimento dal sito corporate.", "openLabel": "Apri documento", "items": make_docs([("Competenze nei sistemi energetici", "Panoramica sullo sviluppo dei sistemi energetici, integrazione delle rinnovabili e Energy Intelligence."), ("Tecnologie infrastrutturali", "Infrastruttura intelligente, sistemi digitali e sviluppo di tecnologie per infrastrutture critiche."), ("Partnership strategiche", "Modelli di partnership, framework di collaborazione e processo di coinvolgimento."), ("Approfondimenti e ricerca", "Prospettive di settore su energia, infrastrutture e tecnologia industriale.")])},
        "support": {"title": "Supporto partner", "subtitle": "Contatta il team TVK Infrastructure & Energy Systems per richieste di partnership, tecniche e generali.", "disclaimer": "Per questioni operative urgenti, contatta il tuo rappresentante partnership assegnato. Tempi di risposta: 1–2 giorni lavorativi per richieste generali.", "channels": make_channels([("Richieste di partnership", "Collaborazione strategica, opportunità pilota e sviluppo di partnership a lungo termine."), ("Relazioni con gli investitori", "Formazione del capitale e discussioni sugli investimenti strategici all'interno del TVK Ecosystem."), ("Supporto tecnico", "Accesso al portale, stato della candidatura e domande tecniche."), ("Contatto generale", "Richieste generali su TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "App Partner Portal", "title": "Scarica l'app TVK Partner Portal", "subtitle": "Installa il portale partner sul tuo telefono — candidati, monitora le iniziative e accedi ai documenti sulle competenze da un'icona nella schermata Home. Funziona oggi tramite Aggiungi a Home; pubblicazione su App Store prevista per la fase 2.", "openApp": "Apri Partner Portal", "howToInstall": "Come installare", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Apri Partner Portal → Condividi → Aggiungi a Home"}, "android": {"title": "Android", "steps": "Chrome → Apri Partner Portal → menu → Installa app o Aggiungi a schermata Home"}, "desktop": {"title": "Desktop", "steps": "Chrome o Edge → icona di installazione nella barra degli indirizzi, oppure aggiungi Partner Portal ai preferiti"}},
    },
)

LOCALE_BUNDLES["pt"] = bundle(
    "Partner Portal", "Obter o app", "App Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Portal de parceiros da TVK Infrastructure & Energy Systems — candidate-se a parcerias estratégicas, acompanhe iniciativas de desenvolvimento e aceda a documentos de capacidades."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Website",
        "navAria": "Navegação do portal de parceiros",
        "nav": {"dashboard": "Painel", "apply": "Candidatar", "projects": "Projetos", "documents": "Documentos", "support": "Suporte"},
        "dashboard": {
            "title": "Painel do parceiro",
            "subtitle": "Acompanhe a sua consulta de parceria, iniciativas de desenvolvimento e próximas ações dentro do TVK Ecosystem.",
            "stats": [{"label": "Fase da parceria", "value": "Desenvolvimento"}, {"label": "Iniciativas ativas", "value": "6 áreas"}, {"label": "Estado da consulta", "value": "Aberto"}, {"label": "Idiomas do portal", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline de parcerias estratégicas", "badge": "Em desenvolvimento", "description": "A TVK Infrastructure & Energy Systems está numa fase de investigação, desenvolvimento e construção de parcerias. Submeta uma candidatura para iniciar uma conversa de colaboração estruturada."},
            "nextSteps": {"title": "Próximos passos recomendados", "items": ["Submeta uma candidatura de parceria estratégica com os dados da sua organização", "Revise as áreas de capacidades em sistemas energéticos e tecnologias de infraestrutura", "Explore iniciativas de desenvolvimento ativas na secção de projetos", "Contacte a nossa equipa de parcerias para oportunidades piloto ou de colaboração"]},
            "cta": "Submeter candidatura de parceria →",
        },
        "apply": {"title": "Candidatura de parceria", "subtitle": "Candidate-se a uma colaboração estratégica com a TVK Infrastructure & Energy Systems.", "intro": "Preencha este formulário para apresentar a sua organização e descrever o seu interesse em parceria. A nossa equipa analisa todas as candidaturas e responde a consultas qualificadas.", "disclaimer": "Esta candidatura não constitui um acordo vinculativo. A TVK Infrastructure & Energy Systems LTD está numa fase de desenvolvimento — a informação descreve áreas de capacidades, não compromissos operacionais."},
        "applyForm": {
            "interestAreas": ["Sistemas energéticos", "Tecnologias de infraestrutura", "Soluções industriais", "Energy Intelligence", "Infraestrutura de IA", "Parcerias estratégicas", "Consulta geral"],
            "success": {"title": "Candidatura recebida", "message": "Obrigado pelo seu interesse em parceria. A nossa equipa analisará a sua candidatura e responderá em 5–10 dias úteis."},
            "fields": {"name": "Nome completo", "company": "Organização", "role": "Função / Título", "country": "País", "email": "E-mail", "interest": "Área de parceria", "allocation": "Âmbito indicativo (USD ou descrição)", "message": "Proposta de parceria", "required": "*"},
            "placeholders": {"name": "O seu nome completo", "company": "Nome da organização", "role": "A sua função", "country": "País de operação", "email": "profissional@empresa.com", "interest": "Selecionar uma área", "allocation": "p. ex. Projeto piloto, colaboração de 500.000 USD, integração tecnológica", "message": "Descreva a sua organização, adequação estratégica e colaboração proposta..."},
            "submit": "Submeter candidatura de parceria",
        },
        "projects": {"title": "Iniciativas de desenvolvimento", "subtitle": "Áreas de capacidades atuais e iniciativas em fase de desenvolvimento dentro do TVK Ecosystem.", "items": make_projects([("Integração de sistemas energéticos", "Em desenvolvimento", "Integração de renováveis, soluções energéticas industriais e frameworks de gestão inteligente de energia."), ("Tecnologias de infraestrutura inteligente", "Investigação", "Sistemas de infraestrutura digital, plataformas de monitorização e desenvolvimento de tecnologias de infraestrutura crítica."), ("IA industrial e analítica", "Investigação ativa", "IA industrial, analítica de infraestrutura e investigação em automação inteligente para ambientes operacionais complexos.")])},
        "documents": {"title": "Documentos de capacidades", "subtitle": "Resumos oficiais de capacidades e materiais de referência do site corporativo.", "openLabel": "Abrir documento", "items": make_docs([("Capacidades em sistemas energéticos", "Visão geral do desenvolvimento de sistemas energéticos, integração de renováveis e Energy Intelligence."), ("Tecnologias de infraestrutura", "Infraestrutura inteligente, sistemas digitais e desenvolvimento de tecnologias de infraestrutura crítica."), ("Parcerias estratégicas", "Modelos de parceria, frameworks de colaboração e processo de envolvimento."), ("Perspetivas e investigação", "Perspetivas setoriais sobre energia, infraestrutura e tecnologia industrial.")])},
        "support": {"title": "Suporte a parceiros", "subtitle": "Contacte a equipa da TVK Infrastructure & Energy Systems para consultas de parceria, técnicas e gerais.", "disclaimer": "Para assuntos operacionais urgentes, contacte o seu representante de parcerias designado. Tempos de resposta: 1–2 dias úteis para consultas gerais.", "channels": make_channels([("Consultas de parceria", "Colaboração estratégica, oportunidades piloto e desenvolvimento de parcerias a longo prazo."), ("Relações com investidores", "Formação de capital e discussões de investimento estratégico dentro do TVK Ecosystem."), ("Suporte técnico", "Acesso ao portal, estado da candidatura e questões técnicas."), ("Contacto geral", "Consultas gerais sobre a TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "App Partner Portal", "title": "Obtenha a app TVK Partner Portal", "subtitle": "Instale o portal de parceiros no seu telemóvel — candidate-se, acompanhe iniciativas e aceda a documentos de capacidades a partir de um ícone no ecrã inicial. Funciona hoje via Adicionar ao ecrã inicial; listagem na App Store prevista para a fase 2.", "openApp": "Abrir Partner Portal", "howToInstall": "Como instalar", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Abrir Partner Portal → Partilhar → Adicionar ao ecrã inicial"}, "android": {"title": "Android", "steps": "Chrome → Abrir Partner Portal → menu → Instalar app ou Adicionar ao ecrã inicial"}, "desktop": {"title": "Desktop", "steps": "Chrome ou Edge → ícone de instalação na barra de endereços, ou guarde Partner Portal nos favoritos"}},
    },
)

LOCALE_BUNDLES["nl"] = bundle(
    "Partner Portal", "App downloaden", "Partner Portal App →",
    {
        "meta": {"title": "Partner Portal", "description": "Partnerportaal van TVK Infrastructure & Energy Systems — vraag strategische partnerschappen aan, volg ontwikkelingsinitiatieven en krijg toegang tot capability-documenten."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Website",
        "navAria": "Partnerportaalnavigatie",
        "nav": {"dashboard": "Dashboard", "apply": "Aanvragen", "projects": "Projecten", "documents": "Documenten", "support": "Ondersteuning"},
        "dashboard": {
            "title": "Partnerdashboard",
            "subtitle": "Volg uw partnerschapsaanvraag, ontwikkelingsinitiatieven en volgende stappen binnen het TVK Ecosystem.",
            "stats": [{"label": "Partnerschapsfase", "value": "Ontwikkeling"}, {"label": "Actieve initiatieven", "value": "6 gebieden"}, {"label": "Aanvraagstatus", "value": "Open"}, {"label": "Portaal talen", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline strategische partnerschappen", "badge": "In ontwikkeling", "description": "TVK Infrastructure & Energy Systems bevindt zich in een fase van onderzoek, ontwikkeling en partnerschapsopbouw. Dien een aanvraag in om een gestructureerd samenwerkingsgesprek te starten."},
            "nextSteps": {"title": "Aanbevolen volgende stappen", "items": ["Dien een aanvraag voor een strategisch partnerschap in met de gegevens van uw organisatie", "Bekijk capability-gebieden op het gebied van energiesystemen en infrastructuurtechnologieën", "Verken actieve ontwikkelingsinitiatieven in het projectgedeelte", "Neem contact op met ons partnershipteam voor pilot- of samenwerkingsmogelijkheden"]},
            "cta": "Partnerschapsaanvraag indienen →",
        },
        "apply": {"title": "Partnerschapsaanvraag", "subtitle": "Vraag strategische samenwerking aan met TVK Infrastructure & Energy Systems.", "intro": "Vul dit formulier in om uw organisatie voor te stellen en uw partnerschapsinteresse te beschrijven. Ons team beoordeelt alle aanvragen en reageert op gekwalificeerde vragen.", "disclaimer": "Deze aanvraag vormt geen bindende overeenkomst. TVK Infrastructure & Energy Systems LTD bevindt zich in een ontwikkelingsfase — informatie beschrijft capability-gebieden, geen operationele verplichtingen."},
        "applyForm": {
            "interestAreas": ["Energiesystemen", "Infrastructuurtechnologieën", "Industriële oplossingen", "Energy Intelligence", "AI-infrastructuur", "Strategische partnerschappen", "Algemene vraag"],
            "success": {"title": "Aanvraag ontvangen", "message": "Bedankt voor uw partnerschapsinteresse. Ons team beoordeelt uw aanvraag en reageert binnen 5–10 werkdagen."},
            "fields": {"name": "Volledige naam", "company": "Organisatie", "role": "Functie / Titel", "country": "Land", "email": "E-mail", "interest": "Partnerschapsgebied", "allocation": "Indicatieve scope (USD of beschrijving)", "message": "Partnerschapsvoorstel", "required": "*"},
            "placeholders": {"name": "Uw volledige naam", "company": "Naam van de organisatie", "role": "Uw functie", "country": "Land van operatie", "email": "professioneel@bedrijf.com", "interest": "Selecteer een gebied", "allocation": "bijv. Pilotproject, samenwerking van $500K, technologie-integratie", "message": "Beschrijf uw organisatie, strategische fit en voorgestelde samenwerking..."},
            "submit": "Partnerschapsaanvraag indienen",
        },
        "projects": {"title": "Ontwikkelingsinitiatieven", "subtitle": "Huidige capability-gebieden en initiatieven in ontwikkelingsfase binnen het TVK Ecosystem.", "items": make_projects([("Integratie van energiesystemen", "In ontwikkeling", "Integratie van hernieuwbare energie, industriële energieoplossingen en intelligente energiemanagementframeworks."), ("Slimme infrastructuurtechnologieën", "Onderzoek", "Digitale infrastructuursystemen, monitoringplatforms en ontwikkeling van kritieke infrastructuurtechnologieën."), ("Industriële AI & analytics", "Actief onderzoek", "Industriële AI, infrastructuuranalytics en onderzoek naar intelligente automatisering voor complexe operationele omgevingen.")])},
        "documents": {"title": "Capability-documenten", "subtitle": "Officiële capability-overzichten en referentiematerialen van de corporate website.", "openLabel": "Document openen", "items": make_docs([("Energiesysteem-capabilities", "Overzicht van energiesysteemontwikkeling, integratie van hernieuwbare energie en Energy Intelligence."), ("Infrastructuurtechnologieën", "Slimme infrastructuur, digitale systemen en ontwikkeling van kritieke infrastructuurtechnologieën."), ("Strategische partnerschappen", "Partnerschapsmodellen, samenwerkingskaders en engagementproces."), ("Inzichten & onderzoek", "Sectorperspectieven over energie, infrastructuur en industriële technologie.")])},
        "support": {"title": "Partnerondersteuning", "subtitle": "Neem contact op met het team van TVK Infrastructure & Energy Systems voor partnership-, technische en algemene vragen.", "disclaimer": "Voor urgente operationele zaken neemt u contact op met uw toegewezen partnershipvertegenwoordiger. Reactietijden: 1–2 werkdagen voor algemene vragen.", "channels": make_channels([("Partnerschapsvragen", "Strategische samenwerking, pilotmogelijkheden en langdurige partnerschapsontwikkeling."), ("Investor Relations", "Kapitaalvorming en strategische investeringsgesprekken binnen het TVK Ecosystem."), ("Technische ondersteuning", "Portaaltoegang, aanvraagstatus en technische vragen."), ("Algemeen contact", "Algemene vragen over TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Partner Portal App", "title": "Download de TVK Partner Portal app", "subtitle": "Installeer het partnerschapsportaal op uw telefoon — vraag aan, volg initiatieven en krijg toegang tot capability-documenten via een startschermpictogram. Werkt vandaag via Toevoegen aan startscherm; App Store-vermelding gepland voor fase 2.", "openApp": "Partner Portal openen", "howToInstall": "Installatie-instructies", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Partner Portal openen → Delen → Zet op beginscherm"}, "android": {"title": "Android", "steps": "Chrome → Partner Portal openen → menu → App installeren of Toevoegen aan startscherm"}, "desktop": {"title": "Desktop", "steps": "Chrome of Edge → installatiepictogram in de adresbalk, of bookmark Partner Portal"}},
    },
)

LOCALE_BUNDLES["pl"] = bundle(
    "Partner Portal", "Pobierz aplikację", "Aplikacja Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Portal partnerski TVK Infrastructure & Energy Systems — składaj wnioski o partnerstwa strategiczne, śledź inicjatywy rozwojowe i uzyskuj dostęp do dokumentów kompetencyjnych."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Strona internetowa",
        "navAria": "Nawigacja portalu partnerskiego",
        "nav": {"dashboard": "Panel", "apply": "Aplikuj", "projects": "Projekty", "documents": "Dokumenty", "support": "Wsparcie"},
        "dashboard": {
            "title": "Panel partnera",
            "subtitle": "Śledź zapytanie partnerskie, inicjatywy rozwojowe i kolejne kroki w ramach TVK Ecosystem.",
            "stats": [{"label": "Etap partnerstwa", "value": "Rozwój"}, {"label": "Aktywne inicjatywy", "value": "6 obszarów"}, {"label": "Status zapytania", "value": "Otwarte"}, {"label": "Języki portalu", "value": "25"}],
            "partnershipStatus": {"title": "Lejek partnerstw strategicznych", "badge": "W rozwoju", "description": "TVK Infrastructure & Energy Systems jest na etapie badań, rozwoju i budowania partnerstw. Złóż wniosek, aby rozpocząć ustrukturyzowaną rozmowę o współpracy."},
            "nextSteps": {"title": "Zalecane kolejne kroki", "items": ["Złóż wniosek o partnerstwo strategiczne z danymi swojej organizacji", "Przejrzyj obszary kompetencyjne w systemach energetycznych i technologiach infrastrukturalnych", "Poznaj aktywne inicjatywy rozwojowe w sekcji projektów", "Skontaktuj się z naszym zespołem partnerskim w sprawie pilotażu lub współpracy"]},
            "cta": "Złóż wniosek partnerski →",
        },
        "apply": {"title": "Wniosek partnerski", "subtitle": "Aplikuj o strategiczną współpracę z TVK Infrastructure & Energy Systems.", "intro": "Wypełnij ten formularz, aby przedstawić swoją organizację i opisać zainteresowanie partnerstwem. Nasz zespół analizuje wszystkie wnioski i odpowiada na kwalifikujące się zapytania.", "disclaimer": "Ten wniosek nie stanowi wiążącej umowy. TVK Infrastructure & Energy Systems LTD jest na etapie rozwoju — informacje opisują obszary kompetencyjne, a nie zobowiązania operacyjne."},
        "applyForm": {
            "interestAreas": ["Systemy energetyczne", "Technologie infrastrukturalne", "Rozwiązania przemysłowe", "Energy Intelligence", "Infrastruktura AI", "Partnerstwa strategiczne", "Zapytanie ogólne"],
            "success": {"title": "Wniosek otrzymany", "message": "Dziękujemy za zainteresowanie partnerstwem. Nasz zespół przeanalizuje wniosek i odpowie w ciągu 5–10 dni roboczych."},
            "fields": {"name": "Imię i nazwisko", "company": "Organizacja", "role": "Stanowisko / Tytuł", "country": "Kraj", "email": "E-mail", "interest": "Obszar partnerstwa", "allocation": "Orientacyjny zakres (USD lub opis)", "message": "Propozycja partnerstwa", "required": "*"},
            "placeholders": {"name": "Twoje imię i nazwisko", "company": "Nazwa organizacji", "role": "Twoje stanowisko", "country": "Kraj działalności", "email": "profesjonalny@firma.com", "interest": "Wybierz obszar", "allocation": "np. Projekt pilotażowy, współpraca 500 tys. USD, integracja technologiczna", "message": "Opisz organizację, dopasowanie strategiczne i proponowaną współpracę..."},
            "submit": "Złóż wniosek partnerski",
        },
        "projects": {"title": "Inicjatywy rozwojowe", "subtitle": "Aktualne obszary kompetencyjne i inicjatywy na etapie rozwoju w ramach TVK Ecosystem.", "items": make_projects([("Integracja systemów energetycznych", "W rozwoju", "Integracja OZE, rozwiązania energetyczne dla przemysłu i inteligentne frameworki zarządzania energią."), ("Inteligentne technologie infrastrukturalne", "Badania", "Cyfrowe systemy infrastrukturalne, platformy monitoringu i rozwój technologii infrastruktury krytycznej."), ("Przemysłowa AI i analityka", "Aktywne badania", "Przemysłowa AI, analityka infrastrukturalna i badania inteligentnej automatyzacji dla złożonych środowisk operacyjnych.")])},
        "documents": {"title": "Dokumenty kompetencyjne", "subtitle": "Oficjalne briefy kompetencyjne i materiały referencyjne ze strony korporacyjnej.", "openLabel": "Otwórz dokument", "items": make_docs([("Kompetencje w systemach energetycznych", "Przegląd rozwoju systemów energetycznych, integracji OZE i Energy Intelligence."), ("Technologie infrastrukturalne", "Inteligentna infrastruktura, systemy cyfrowe i rozwój technologii infrastruktury krytycznej."), ("Partnerstwa strategiczne", "Modele partnerstwa, ramy współpracy i proces zaangażowania."), ("Spojrzenia i badania", "Perspektywy branżowe dotyczące energii, infrastruktury i technologii przemysłowej.")])},
        "support": {"title": "Wsparcie partnerów", "subtitle": "Skontaktuj się z zespołem TVK Infrastructure & Energy Systems w sprawach partnerskich, technicznych i ogólnych.", "disclaimer": "W pilnych sprawach operacyjnych skontaktuj się z przypisanym przedstawicielem partnerskim. Czas odpowiedzi: 1–2 dni robocze dla zapytań ogólnych.", "channels": make_channels([("Zapytania partnerskie", "Współpraca strategiczna, możliwości pilotażowe i długoterminowy rozwój partnerstwa."), ("Relacje inwestorskie", "Formowanie kapitału i rozmowy o inwestycjach strategicznych w ramach TVK Ecosystem."), ("Wsparcie techniczne", "Dostęp do portalu, status wniosku i pytania techniczne."), ("Kontakt ogólny", "Ogólne zapytania dotyczące TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Aplikacja Partner Portal", "title": "Pobierz aplikację TVK Partner Portal", "subtitle": "Zainstaluj portal partnerski na telefonie — aplikuj, śledź inicjatywy i uzyskuj dostęp do dokumentów kompetencyjnych z ikony ekranu głównego. Działa już dziś przez Dodaj do ekranu początkowego; publikacja w App Store planowana na fazę 2.", "openApp": "Otwórz Partner Portal", "howToInstall": "Jak zainstalować", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Otwórz Partner Portal → Udostępnij → Dodaj do ekranu początkowego"}, "android": {"title": "Android", "steps": "Chrome → Otwórz Partner Portal → menu → Zainstaluj aplikację lub Dodaj do ekranu głównego"}, "desktop": {"title": "Komputer", "steps": "Chrome lub Edge → ikona instalacji na pasku adresu lub dodaj Partner Portal do zakładek"}},
    },
)

LOCALE_BUNDLES["ru"] = bundle(
    "Partner Portal", "Скачать приложение", "Приложение Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Партнёрский портал TVK Infrastructure & Energy Systems — подавайте заявки на стратегические партнёрства, отслеживайте инициативы развития и получайте доступ к документам о компетенциях."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Сайт",
        "navAria": "Навигация партнёрского портала",
        "nav": {"dashboard": "Панель", "apply": "Подать заявку", "projects": "Проекты", "documents": "Документы", "support": "Поддержка"},
        "dashboard": {
            "title": "Партнёрская панель",
            "subtitle": "Отслеживайте запрос на партнёрство, инициативы развития и следующие шаги в рамках TVK Ecosystem.",
            "stats": [{"label": "Этап партнёрства", "value": "Разработка"}, {"label": "Активные инициативы", "value": "6 направлений"}, {"label": "Статус запроса", "value": "Открыт"}, {"label": "Языки портала", "value": "25"}],
            "partnershipStatus": {"title": "Воронка стратегических партнёрств", "badge": "В разработке", "description": "TVK Infrastructure & Energy Systems находится на этапе исследований, разработки и формирования партнёрств. Подайте заявку, чтобы начать структурированный диалог о сотрудничестве."},
            "nextSteps": {"title": "Рекомендуемые следующие шаги", "items": ["Подайте заявку на стратегическое партнёрство с данными вашей организации", "Изучите области компетенций в энергетических системах и инфраструктурных технологиях", "Ознакомьтесь с активными инициативами развития в разделе проектов", "Свяжитесь с нашей командой партнёрств для пилотных или совместных возможностей"]},
            "cta": "Подать заявку на партнёрство →",
        },
        "apply": {"title": "Заявка на партнёрство", "subtitle": "Подайте заявку на стратегическое сотрудничество с TVK Infrastructure & Energy Systems.", "intro": "Заполните эту форму, чтобы представить вашу организацию и описать интерес к партнёрству. Наша команда рассматривает все заявки и отвечает на квалифицированные запросы.", "disclaimer": "Эта заявка не является обязательным соглашением. TVK Infrastructure & Energy Systems LTD находится на этапе разработки — информация описывает области компетенций, а не операционные обязательства."},
        "applyForm": {
            "interestAreas": ["Энергетические системы", "Инфраструктурные технологии", "Промышленные решения", "Energy Intelligence", "ИИ-инфраструктура", "Стратегические партнёрства", "Общий запрос"],
            "success": {"title": "Заявка получена", "message": "Благодарим за интерес к партнёрству. Наша команда рассмотрит вашу заявку и ответит в течение 5–10 рабочих дней."},
            "fields": {"name": "Полное имя", "company": "Организация", "role": "Должность / Титул", "country": "Страна", "email": "Эл. почта", "interest": "Область партнёрства", "allocation": "Ориентировочный объём (USD или описание)", "message": "Предложение о партнёрстве", "required": "*"},
            "placeholders": {"name": "Ваше полное имя", "company": "Название организации", "role": "Ваша должность", "country": "Страна деятельности", "email": "professional@company.com", "interest": "Выберите область", "allocation": "напр. Пилотный проект, сотрудничество на $500K, интеграция технологий", "message": "Опишите вашу организацию, стратегическое соответствие и предлагаемое сотрудничество..."},
            "submit": "Подать заявку на партнёрство",
        },
        "projects": {"title": "Инициативы развития", "subtitle": "Текущие области компетенций и инициативы на этапе разработки в рамках TVK Ecosystem.", "items": make_projects([("Интеграция энергетических систем", "В разработке", "Интеграция ВИЭ, промышленные энергетические решения и интеллектуальные системы управления энергией."), ("Технологии умной инфраструктуры", "Исследование", "Цифровые инфраструктурные системы, платформы мониторинга и разработка технологий критической инфраструктуры."), ("Промышленный ИИ и аналитика", "Активные исследования", "Промышленный ИИ, инфраструктурная аналитика и исследования интеллектуальной автоматизации для сложных операционных сред.")])},
        "documents": {"title": "Документы о компетенциях", "subtitle": "Официальные обзоры компетенций и справочные материалы с корпоративного сайта.", "openLabel": "Открыть документ", "items": make_docs([("Компетенции в энергетических системах", "Обзор развития энергетических систем, интеграции ВИЭ и Energy Intelligence."), ("Инфраструктурные технологии", "Умная инфраструктура, цифровые системы и разработка технологий критической инфраструктуры."), ("Стратегические партнёрства", "Модели партнёрства, рамки сотрудничества и процесс взаимодействия."), ("Аналитика и исследования", "Отраслевые перспективы по энергетике, инфраструктуре и промышленным технологиям.")])},
        "support": {"title": "Поддержка партнёров", "subtitle": "Свяжитесь с командой TVK Infrastructure & Energy Systems по вопросам партнёрства, техническим и общим запросам.", "disclaimer": "По срочным операционным вопросам обращайтесь к назначенному представителю партнёрства. Время ответа: 1–2 рабочих дня для общих запросов.", "channels": make_channels([("Запросы о партнёрстве", "Стратегическое сотрудничество, пилотные возможности и долгосрочное развитие партнёрства."), ("Связи с инвесторами", "Формирование капитала и обсуждение стратегических инвестиций в рамках TVK Ecosystem."), ("Техническая поддержка", "Доступ к порталу, статус заявки и технические вопросы."), ("Общий контакт", "Общие запросы о TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Приложение Partner Portal", "title": "Скачайте приложение TVK Partner Portal", "subtitle": "Установите партнёрский портал на телефон — подавайте заявки, отслеживайте инициативы и получайте доступ к документам с иконки на главном экране. Уже работает через «На экран Домой»; публикация в App Store запланирована на фазу 2.", "openApp": "Открыть Partner Portal", "howToInstall": "Как установить", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Открыть Partner Portal → Поделиться → На экран «Домой»"}, "android": {"title": "Android", "steps": "Chrome → Открыть Partner Portal → меню → Установить приложение или Добавить на главный экран"}, "desktop": {"title": "Компьютер", "steps": "Chrome или Edge → значок установки в адресной строке или добавьте Partner Portal в закладки"}},
    },
)

LOCALE_BUNDLES["ar"] = bundle(
    "Partner Portal", "احصل على التطبيق", "تطبيق Partner Portal ←",
    {
        "meta": {"title": "Partner Portal", "description": "بوابة شركاء TVK Infrastructure & Energy Systems — تقدّم لطلب شراكات استراتيجية، وتتبّع مبادرات التطوير، واطّلع على وثائق القدرات."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "الموقع",
        "navAria": "تنقل بوابة الشركاء",
        "nav": {"dashboard": "لوحة التحكم", "apply": "تقديم طلب", "projects": "المشاريع", "documents": "المستندات", "support": "الدعم"},
        "dashboard": {
            "title": "لوحة تحكم الشريك",
            "subtitle": "تتبّع استفسار الشراكة ومبادرات التطوير والخطوات التالية ضمن TVK Ecosystem.",
            "stats": [{"label": "مرحلة الشراكة", "value": "التطوير"}, {"label": "المبادرات النشطة", "value": "6 مجالات"}, {"label": "حالة الاستفسار", "value": "مفتوح"}, {"label": "لغات البوابة", "value": "25"}],
            "partnershipStatus": {"title": "مسار الشراكات الاستراتيجية", "badge": "قيد التطوير", "description": "TVK Infrastructure & Energy Systems في مرحلة البحث والتطوير وبناء الشراكات. قدّم طلبًا لبدء محادثة تعاون منظّمة."},
            "nextSteps": {"title": "الخطوات التالية الموصى بها", "items": ["قدّم طلب شراكة استراتيجية مع تفاصيل مؤسستك", "راجع مجالات القدرات في أنظمة الطاقة وتقنيات البنية التحتية", "استكشف مبادرات التطوير النشطة في قسم المشاريع", "تواصل مع فريق الشراكات لدينا لفرص التجريب أو التعاون"]},
            "cta": "تقديم طلب الشراكة ←",
        },
        "apply": {"title": "طلب الشراكة", "subtitle": "قدّم للتعاون الاستراتيجي مع TVK Infrastructure & Energy Systems.", "intro": "أكمل هذا النموذج لتقديم مؤسستك ووصف اهتمامك بالشراكة. يراجع فريقنا جميع الطلبات ويرد على الاستفسارات المؤهلة.", "disclaimer": "هذا الطلب لا يُعدّ اتفاقًا ملزمًا. TVK Infrastructure & Energy Systems LTD في مرحلة التطوير — المعلومات تصف مجالات القدرات وليست التزامات تشغيلية."},
        "applyForm": {
            "interestAreas": ["أنظمة الطاقة", "تقنيات البنية التحتية", "الحلول الصناعية", "Energy Intelligence", "بنية الذكاء الاصطناعي", "الشراكات الاستراتيجية", "استفسار عام"],
            "success": {"title": "تم استلام الطلب", "message": "شكرًا لاهتمامك بالشراكة. سيراجع فريقنا طلبك ويرد خلال 5–10 أيام عمل."},
            "fields": {"name": "الاسم الكامل", "company": "المؤسسة", "role": "الدور / المسمى", "country": "البلد", "email": "البريد الإلكتروني", "interest": "مجال الشراكة", "allocation": "النطاق الإرشادي (USD أو وصف)", "message": "مقترح الشراكة", "required": "*"},
            "placeholders": {"name": "اسمك الكامل", "company": "اسم المؤسسة", "role": "منصبك", "country": "بلد العمل", "email": "professional@company.com", "interest": "اختر مجالًا", "allocation": "مثلًا: مشروع تجريبي، تعاون بقيمة 500 ألف دولار، تكامل تقني", "message": "صف مؤسستك والتوافق الاستراتيجي والتعاون المقترح..."},
            "submit": "تقديم طلب الشراكة",
        },
        "projects": {"title": "مبادرات التطوير", "subtitle": "مجالات القدرات الحالية والمبادرات في مرحلة التطوير ضمن TVK Ecosystem.", "items": make_projects([("تكامل أنظمة الطاقة", "قيد التطوير", "دمج الطاقة المتجددة وحلول الطاقة الصناعية وأطر إدارة الطاقة الذكية."), ("تقنيات البنية التحتية الذكية", "بحث", "أنظمة البنية التحتية الرقمية ومنصات المراقبة وتطوير تقنيات البنية التحتية الحيوية."), ("الذكاء الاصطناعي الصناعي والتحليلات", "بحث نشط", "الذكاء الاصطناعي الصناعي وتحليلات البنية التحتية وبحث الأتمتة الذكية للبيئات التشغيلية المعقدة.")])},
        "documents": {"title": "وثائق القدرات", "subtitle": "ملخصات رسمية للقدرات ومواد مرجعية من الموقع المؤسسي.", "openLabel": "فتح المستند", "items": make_docs([("قدرات أنظمة الطاقة", "نظرة عامة على تطوير أنظمة الطاقة ودمج المتجددة وEnergy Intelligence."), ("تقنيات البنية التحتية", "البنية التحتية الذكية والأنظمة الرقمية وتطوير تقنيات البنية التحتية الحيوية."), ("الشراكات الاستراتيجية", "نماذج الشراكة وأطر التعاون وعملية المشاركة."), ("رؤى وأبحاث", "منظورات صناعية حول الطاقة والبنية التحتية والتكنولوجيا الصناعية.")])},
        "support": {"title": "دعم الشركاء", "subtitle": "تواصل مع فريق TVK Infrastructure & Energy Systems للاستفسارات المتعلقة بالشراكة والدعم الفني والاستفسارات العامة.", "disclaimer": "للمسائل التشغيلية العاجلة، تواصل مع ممثل الشراكة المعيّن. أوقات الاستجابة: 1–2 يوم عمل للاستفسارات العامة.", "channels": make_channels([("استفسارات الشراكة", "التعاون الاستراتيجي وفرص التجريب وتطوير الشراكات طويلة الأمد."), ("علاقات المستثمرين", "تكوين رأس المال ومناقشات الاستثمار الاستراتيجي ضمن TVK Ecosystem."), ("الدعم الفني", "الوصول إلى البوابة وحالة الطلب والأسئلة التقنية."), ("اتصال عام", "استفسارات عامة حول TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "تطبيق Partner Portal", "title": "احصل على تطبيق TVK Partner Portal", "subtitle": "ثبّت بوابة الشراكة على هاتفك — قدّم الطلبات، وتتبّع المبادرات، واطّلع على وثائق القدرات من أيقونة الشاشة الرئيسية. يعمل اليوم عبر «إضافة إلى الشاشة الرئيسية»؛ الإدراج في App Store مخطط للمرحلة 2.", "openApp": "فتح Partner Portal", "howToInstall": "كيفية التثبيت", "iphone": {"title": "iPhone / iPad", "steps": "Safari ← فتح Partner Portal ← مشاركة ← إضافة إلى الشاشة الرئيسية"}, "android": {"title": "Android", "steps": "Chrome ← فتح Partner Portal ← القائمة ← تثبيت التطبيق أو إضافة إلى الشاشة الرئيسية"}, "desktop": {"title": "سطح المكتب", "steps": "Chrome أو Edge ← أيقونة التثبيت في شريط العنوان، أو احفظ Partner Portal في المفضلة"}},
    },
)

LOCALE_BUNDLES["zh"] = bundle(
    "Partner Portal", "获取应用", "Partner Portal 应用 →",
    {
        "meta": {"title": "Partner Portal", "description": "TVK Infrastructure & Energy Systems 合作伙伴门户 — 申请战略合作、跟踪开发举措并访问能力文档。"},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "网站",
        "navAria": "合作伙伴门户导航",
        "nav": {"dashboard": "仪表板", "apply": "申请", "projects": "项目", "documents": "文档", "support": "支持"},
        "dashboard": {
            "title": "合作伙伴仪表板",
            "subtitle": "在 TVK Ecosystem 内跟踪您的合作咨询、开发举措和后续行动。",
            "stats": [{"label": "合作阶段", "value": "开发中"}, {"label": "活跃举措", "value": "6 个领域"}, {"label": "咨询状态", "value": "开放"}, {"label": "门户语言", "value": "25"}],
            "partnershipStatus": {"title": "战略合作管道", "badge": "开发中", "description": "TVK Infrastructure & Energy Systems 目前处于研究、开发和合作伙伴建设阶段。提交申请以开始结构化的合作对话。"},
            "nextSteps": {"title": "建议的后续步骤", "items": ["提交包含组织信息的战略合作申请", "查阅能源系统和基础设施技术领域的能力", "在项目部分探索活跃的开发举措", "联系我们的合作伙伴团队了解试点或合作机会"]},
            "cta": "提交合作申请 →",
        },
        "apply": {"title": "合作申请", "subtitle": "申请与 TVK Infrastructure & Energy Systems 进行战略合作。", "intro": "填写此表单以介绍您的组织并描述合作意向。我们的团队会审核所有申请并对符合条件的咨询予以回复。", "disclaimer": "本申请不构成具有约束力的协议。TVK Infrastructure & Energy Systems LTD 处于开发阶段 — 信息描述的是能力领域，而非运营承诺。"},
        "applyForm": {
            "interestAreas": ["能源系统", "基础设施技术", "工业解决方案", "Energy Intelligence", "AI 基础设施", "战略合作", "一般咨询"],
            "success": {"title": "申请已收到", "message": "感谢您对合作的关注。我们的团队将在 5–10 个工作日内审核您的申请并回复。"},
            "fields": {"name": "全名", "company": "组织", "role": "职位 / 头衔", "country": "国家", "email": "电子邮件", "interest": "合作领域", "allocation": "参考范围（美元或描述）", "message": "合作提案", "required": "*"},
            "placeholders": {"name": "您的全名", "company": "组织名称", "role": "您的职位", "country": "运营国家/地区", "email": "professional@company.com", "interest": "选择领域", "allocation": "例如：试点项目、50 万美元合作、技术集成", "message": "描述您的组织、战略契合度及拟议合作..."},
            "submit": "提交合作申请",
        },
        "projects": {"title": "开发举措", "subtitle": "TVK Ecosystem 内当前的能力领域和开发阶段举措。", "items": make_projects([("能源系统集成", "开发中", "可再生能源集成、工业能源解决方案和智能能源管理框架。"), ("智能基础设施技术", "研究", "数字基础设施系统、监控平台和关键基础设施技术开发。"), ("工业 AI 与分析", "活跃研究", "面向复杂运营环境的工业 AI、基础设施分析和智能自动化研究。")])},
        "documents": {"title": "能力文档", "subtitle": "来自企业网站的官方能力简介和参考资料。", "openLabel": "打开文档", "items": make_docs([("能源系统能力", "能源系统开发、可再生能源集成和 Energy Intelligence 概述。"), ("基础设施技术", "智能基础设施、数字系统和关键基础设施技术开发。"), ("战略合作", "合作模式、协作框架和参与流程。"), ("洞察与研究", "关于能源、基础设施和工业技术的行业观点。")])},
        "support": {"title": "合作伙伴支持", "subtitle": "联系 TVK Infrastructure & Energy Systems 团队，获取合作、技术和一般咨询方面的帮助。", "disclaimer": "如有紧急运营事项，请联系指定的合作伙伴代表。一般咨询的回复时间：1–2 个工作日。", "channels": make_channels([("合作咨询", "战略合作、试点机会和长期合作伙伴关系发展。"), ("投资者关系", "TVK Ecosystem 内的资本形成和战略投资讨论。"), ("技术支持", "门户访问、申请状态和技术问题。"), ("一般联系", "关于 TVK Infrastructure & Energy Systems 的一般咨询。")])},
        "install": {"eyebrow": "Partner Portal 应用", "title": "获取 TVK Partner Portal 应用", "subtitle": "在手机上安装合作伙伴门户 — 申请、跟踪举措并从主屏幕图标访问能力文档。目前可通过「添加到主屏幕」使用；App Store 上架计划为第二阶段。", "openApp": "打开 Partner Portal", "howToInstall": "如何安装", "iphone": {"title": "iPhone / iPad", "steps": "Safari → 打开 Partner Portal → 共享 → 添加到主屏幕"}, "android": {"title": "Android", "steps": "Chrome → 打开 Partner Portal → 菜单 → 安装应用或添加到主屏幕"}, "desktop": {"title": "桌面", "steps": "Chrome 或 Edge → 地址栏中的安装图标，或将 Partner Portal 加入书签"}},
    },
)

LOCALE_BUNDLES["ja"] = bundle(
    "Partner Portal", "アプリを入手", "Partner Portal アプリ →",
    {
        "meta": {"title": "Partner Portal", "description": "TVK Infrastructure & Energy Systems パートナーポータル — 戦略的パートナーシップの申請、開発イニシアチブの追跡、能力ドキュメントへのアクセス。"},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "ウェブサイト",
        "navAria": "パートナーポータルナビゲーション",
        "nav": {"dashboard": "ダッシュボード", "apply": "申請", "projects": "プロジェクト", "documents": "ドキュメント", "support": "サポート"},
        "dashboard": {
            "title": "パートナーダッシュボード",
            "subtitle": "TVK Ecosystem 内でパートナーシップの問い合わせ、開発イニシアチブ、次のアクションを追跡します。",
            "stats": [{"label": "パートナーシップ段階", "value": "開発中"}, {"label": "アクティブなイニシアチブ", "value": "6 分野"}, {"label": "問い合わせ状況", "value": "受付中"}, {"label": "ポータル言語", "value": "25"}],
            "partnershipStatus": {"title": "戦略的パートナーシップパイプライン", "badge": "開発中", "description": "TVK Infrastructure & Energy Systems は研究・開発・パートナーシップ構築の段階にあります。申請を提出して、構造化された協業の対話を開始してください。"},
            "nextSteps": {"title": "推奨される次のステップ", "items": ["組織情報を記載した戦略的パートナーシップ申請を提出する", "エネルギーシステムとインフラ技術の能力分野を確認する", "プロジェクトセクションでアクティブな開発イニシアチブを探索する", "パイロットや協業の機会についてパートナーシップチームに連絡する"]},
            "cta": "パートナーシップ申請を提出 →",
        },
        "apply": {"title": "パートナーシップ申請", "subtitle": "TVK Infrastructure & Energy Systems との戦略的協業に申請する。", "intro": "このフォームに記入して組織を紹介し、パートナーシップへの関心を説明してください。当社チームがすべての申請を審査し、適格な問い合わせに回答します。", "disclaimer": "本申請は拘束力のある契約を構成するものではありません。TVK Infrastructure & Energy Systems LTD は開発段階にあり — 情報は能力分野を説明するものであり、運用上のコミットメントではありません。"},
        "applyForm": {
            "interestAreas": ["エネルギーシステム", "インフラ技術", "産業ソリューション", "Energy Intelligence", "AI インフラ", "戦略的パートナーシップ", "一般問い合わせ"],
            "success": {"title": "申請を受け付けました", "message": "パートナーシップへのご関心ありがとうございます。当社チームが申請を審査し、5〜10 営業日以内に回答します。"},
            "fields": {"name": "氏名", "company": "組織", "role": "役職 / 肩書", "country": "国", "email": "メール", "interest": "パートナーシップ分野", "allocation": "参考規模（USD または説明）", "message": "パートナーシップ提案", "required": "*"},
            "placeholders": {"name": "氏名", "company": "組織名", "role": "役職", "country": "事業国", "email": "professional@company.com", "interest": "分野を選択", "allocation": "例：パイロットプロジェクト、50 万ドルの協業、技術統合", "message": "組織、戦略的適合性、提案する協業について説明..."},
            "submit": "パートナーシップ申請を提出",
        },
        "projects": {"title": "開発イニシアチブ", "subtitle": "TVK Ecosystem 内の現在の能力分野と開発段階のイニシアチブ。", "items": make_projects([("エネルギーシステム統合", "開発中", "再生可能エネルギー統合、産業用エネルギーソリューション、インテリジェントエネルギー管理フレームワーク。"), ("スマートインフラ技術", "研究", "デジタルインフラシステム、監視プラットフォーム、重要インフラ技術の開発。"), ("産業 AI と分析", "アクティブな研究", "複雑な運用環境向けの産業 AI、インフラ分析、インテリジェント自動化の研究。")])},
        "documents": {"title": "能力ドキュメント", "subtitle": "コーポレートサイトの公式能力概要と参考資料。", "openLabel": "ドキュメントを開く", "items": make_docs([("エネルギーシステム能力", "エネルギーシステム開発、再生可能エネルギー統合、Energy Intelligence の概要。"), ("インフラ技術", "スマートインフラ、デジタルシステム、重要インフラ技術の開発。"), ("戦略的パートナーシップ", "パートナーシップモデル、協業フレームワーク、エンゲージメントプロセス。"), ("インサイトと研究", "エネルギー、インフラ、産業技術に関する業界の視点。")])},
        "support": {"title": "パートナーサポート", "subtitle": "パートナーシップ、技術、一般の問い合わせについて TVK Infrastructure & Energy Systems チームにお問い合わせください。", "disclaimer": "緊急の運用事項については、担当のパートナーシップ代表者にお問い合わせください。一般問い合わせの回答時間：1〜2 営業日。", "channels": make_channels([("パートナーシップ問い合わせ", "戦略的協業、パイロット機会、長期的なパートナーシップ開発。"), ("投資家向け情報", "TVK Ecosystem 内の資本形成と戦略的投資に関する協議。"), ("テクニカルサポート", "ポータルアクセス、申請状況、技術的な質問。"), ("一般連絡", "TVK Infrastructure & Energy Systems に関する一般問い合わせ。")])},
        "install": {"eyebrow": "Partner Portal アプリ", "title": "TVK Partner Portal アプリを入手", "subtitle": "スマートフォンにパートナーシップポータルをインストール — 申請、イニシアチブの追跡、ホーム画面アイコンから能力ドキュメントにアクセス。現在はホーム画面に追加で利用可能；App Store 掲載はフェーズ 2 で予定。", "openApp": "Partner Portal を開く", "howToInstall": "インストール方法", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Partner Portal を開く → 共有 → ホーム画面に追加"}, "android": {"title": "Android", "steps": "Chrome → Partner Portal を開く → メニュー → アプリをインストールまたはホーム画面に追加"}, "desktop": {"title": "デスクトップ", "steps": "Chrome または Edge → アドレスバーのインストールアイコン、または Partner Portal をブックマーク"}},
    },
)

LOCALE_BUNDLES["ko"] = bundle(
    "Partner Portal", "앱 받기", "Partner Portal 앱 →",
    {
        "meta": {"title": "Partner Portal", "description": "TVK Infrastructure & Energy Systems 파트너 포털 — 전략적 파트너십 신청, 개발 이니셔티브 추적, 역량 문서 접근."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "웹사이트",
        "navAria": "파트너 포털 탐색",
        "nav": {"dashboard": "대시보드", "apply": "신청", "projects": "프로젝트", "documents": "문서", "support": "지원"},
        "dashboard": {
            "title": "파트너 대시보드",
            "subtitle": "TVK Ecosystem 내에서 파트너십 문의, 개발 이니셔티브 및 다음 조치를 추적하세요.",
            "stats": [{"label": "파트너십 단계", "value": "개발"}, {"label": "활성 이니셔티브", "value": "6개 영역"}, {"label": "문의 상태", "value": "접수 중"}, {"label": "포털 언어", "value": "25"}],
            "partnershipStatus": {"title": "전략적 파트너십 파이프라인", "badge": "개발 중", "description": "TVK Infrastructure & Energy Systems는 연구, 개발 및 파트너십 구축 단계에 있습니다. 신청서를 제출하여 구조화된 협업 대화를 시작하세요."},
            "nextSteps": {"title": "권장 다음 단계", "items": ["조직 정보와 함께 전략적 파트너십 신청서 제출", "에너지 시스템 및 인프라 기술 역량 영역 검토", "프로젝트 섹션에서 활성 개발 이니셔티브 탐색", "파일럿 또는 협업 기회를 위해 파트너십 팀에 문의"]},
            "cta": "파트너십 신청서 제출 →",
        },
        "apply": {"title": "파트너십 신청", "subtitle": "TVK Infrastructure & Energy Systems와의 전략적 협업에 신청하세요.", "intro": "이 양식을 작성하여 조직을 소개하고 파트너십 관심 사항을 설명하세요. 당사 팀이 모든 신청서를 검토하고 자격을 갖춘 문의에 응답합니다.", "disclaimer": "본 신청은 구속력 있는 계약을 구성하지 않습니다. TVK Infrastructure & Energy Systems LTD는 개발 단계에 있으며 — 정보는 역량 영역을 설명하는 것이지 운영상의 약속이 아닙니다."},
        "applyForm": {
            "interestAreas": ["에너지 시스템", "인프라 기술", "산업 솔루션", "Energy Intelligence", "AI 인프라", "전략적 파트너십", "일반 문의"],
            "success": {"title": "신청 접수됨", "message": "파트너십에 관심을 가져 주셔서 감사합니다. 당사 팀이 신청서를 검토하고 5–10 영업일 내에 응답합니다."},
            "fields": {"name": "성명", "company": "조직", "role": "직책 / 직함", "country": "국가", "email": "이메일", "interest": "파트너십 영역", "allocation": "참고 범위(USD 또는 설명)", "message": "파트너십 제안", "required": "*"},
            "placeholders": {"name": "성명", "company": "조직명", "role": "직책", "country": "운영 국가", "email": "professional@company.com", "interest": "영역 선택", "allocation": "예: 파일럿 프로젝트, 50만 달러 협업, 기술 통합", "message": "조직, 전략적 적합성 및 제안된 협업을 설명..."},
            "submit": "파트너십 신청서 제출",
        },
        "projects": {"title": "개발 이니셔티브", "subtitle": "TVK Ecosystem 내 현재 역량 영역 및 개발 단계 이니셔티브.", "items": make_projects([("에너지 시스템 통합", "개발 중", "재생에너지 통합, 산업용 에너지 솔루션 및 지능형 에너지 관리 프레임워크."), ("스마트 인프라 기술", "연구", "디지털 인프라 시스템, 모니터링 플랫폼 및 핵심 인프라 기술 개발."), ("산업 AI 및 분석", "활성 연구", "복잡한 운영 환경을 위한 산업 AI, 인프라 분석 및 지능형 자동화 연구.")])},
        "documents": {"title": "역량 문서", "subtitle": "기업 웹사이트의 공식 역량 개요 및 참고 자료.", "openLabel": "문서 열기", "items": make_docs([("에너지 시스템 역량", "에너지 시스템 개발, 재생에너지 통합 및 Energy Intelligence 개요."), ("인프라 기술", "스마트 인프라, 디지털 시스템 및 핵심 인프라 기술 개발."), ("전략적 파트너십", "파트너십 모델, 협업 프레임워크 및 참여 프로세스."), ("인사이트 및 연구", "에너지, 인프라 및 산업 기술에 대한 업계 관점.")])},
        "support": {"title": "파트너 지원", "subtitle": "파트너십, 기술 및 일반 문의는 TVK Infrastructure & Energy Systems 팀에 연락하세요.", "disclaimer": "긴급 운영 사항은 지정된 파트너십 담당자에게 연락하세요. 일반 문의 응답 시간: 1–2 영업일.", "channels": make_channels([("파트너십 문의", "전략적 협업, 파일럿 기회 및 장기 파트너십 개발."), ("투자자 관계", "TVK Ecosystem 내 자본 형성 및 전략적 투자 논의."), ("기술 지원", "포털 접근, 신청 상태 및 기술 질문."), ("일반 연락", "TVK Infrastructure & Energy Systems에 대한 일반 문의.")])},
        "install": {"eyebrow": "Partner Portal 앱", "title": "TVK Partner Portal 앱 받기", "subtitle": "휴대폰에 파트너십 포털 설치 — 신청, 이니셔티브 추적, 홈 화면 아이콘에서 역량 문서 접근. 현재 홈 화면에 추가로 사용 가능; App Store 등록은 2단계 예정.", "openApp": "Partner Portal 열기", "howToInstall": "설치 방법", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Partner Portal 열기 → 공유 → 홈 화면에 추가"}, "android": {"title": "Android", "steps": "Chrome → Partner Portal 열기 → 메뉴 → 앱 설치 또는 홈 화면에 추가"}, "desktop": {"title": "데스크톱", "steps": "Chrome 또는 Edge → 주소 표시줄의 설치 아이콘 또는 Partner Portal 북마크"}},
    },
)

LOCALE_BUNDLES["hi"] = bundle(
    "Partner Portal", "ऐप प्राप्त करें", "Partner Portal ऐप →",
    {
        "meta": {"title": "Partner Portal", "description": "TVK Infrastructure & Energy Systems पार्टनर पोर्टल — रणनीतिक साझेदारी के लिए आवेदन करें, विकास पहलों को ट्रैक करें और क्षमता दस्तावेज़ों तक पहुँचें।"},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "वेबसाइट",
        "navAria": "पार्टनर पोर्टल नेविगेशन",
        "nav": {"dashboard": "डैशबोर्ड", "apply": "आवेदन", "projects": "परियोजनाएँ", "documents": "दस्तावेज़", "support": "सहायता"},
        "dashboard": {
            "title": "पार्टनर डैशबोर्ड",
            "subtitle": "TVK Ecosystem के भीतर अपनी साझेदारी पूछताछ, विकास पहलों और अगले कदमों को ट्रैक करें।",
            "stats": [{"label": "साझेदारी चरण", "value": "विकास"}, {"label": "सक्रिय पहल", "value": "6 क्षेत्र"}, {"label": "पूछताछ स्थिति", "value": "खुला"}, {"label": "पोर्टल भाषाएँ", "value": "25"}],
            "partnershipStatus": {"title": "रणनीतिक साझेदारी पाइपलाइन", "badge": "विकास में", "description": "TVK Infrastructure & Energy Systems अनुसंधान, विकास और साझेदारी निर्माण के चरण में है। संरचित सहयोग वार्ता शुरू करने के लिए आवेदन जमा करें।"},
            "nextSteps": {"title": "अनुशंसित अगले कदम", "items": ["अपने संगठन का विवरण देकर रणनीतिक साझेदारी आवेदन जमा करें", "ऊर्जा प्रणालियों और बुनियादी ढाँचा प्रौद्योगिकियों में क्षमता क्षेत्रों की समीक्षा करें", "परियोजना अनुभाग में सक्रिय विकास पहलों का अन्वेषण करें", "पायलट या सहयोग के अवसरों के लिए हमारी साझेदारी टीम से संपर्क करें"]},
            "cta": "साझेदारी आवेदन जमा करें →",
        },
        "apply": {"title": "साझेदारी आवेदन", "subtitle": "TVK Infrastructure & Energy Systems के साथ रणनीतिक सहयोग के लिए आवेदन करें।", "intro": "अपने संगठन का परिचय देने और साझेदारी रुचि का वर्णन करने के लिए यह फ़ॉर्म पूरा करें। हमारी टीम सभी आवेदनों की समीक्षा करती है और योग्य पूछताछों का जवाब देती है।", "disclaimer": "यह आवेदन कोई बाध्यकारी समझौता नहीं है। TVK Infrastructure & Energy Systems LTD विकास चरण में है — जानकारी क्षमता क्षेत्रों का वर्णन करती है, परिचालन प्रतिबद्धताओं का नहीं।"},
        "applyForm": {
            "interestAreas": ["ऊर्जा प्रणालियाँ", "बुनियादी ढाँचा प्रौद्योगिकियाँ", "औद्योगिक समाधान", "Energy Intelligence", "AI बुनियादी ढाँचा", "रणनीतिक साझेदारी", "सामान्य पूछताछ"],
            "success": {"title": "आवेदन प्राप्त", "message": "साझेदारी में रुचि के लिए धन्यवाद। हमारी टीम आपके आवेदन की समीक्षा करेगी और 5–10 कार्य दिवसों में जवाब देगी।"},
            "fields": {"name": "पूरा नाम", "company": "संगठन", "role": "भूमिका / पद", "country": "देश", "email": "ईमेल", "interest": "साझेदारी क्षेत्र", "allocation": "संकेतात्मक दायरा (USD या विवरण)", "message": "साझेदारी प्रस्ताव", "required": "*"},
            "placeholders": {"name": "आपका पूरा नाम", "company": "संगठन का नाम", "role": "आपका पद", "country": "संचालन का देश", "email": "professional@company.com", "interest": "क्षेत्र चुनें", "allocation": "उदा. पायलट परियोजना, $500K सहयोग, प्रौद्योगिकी एकीकरण", "message": "अपने संगठन, रणनीतिक फिट और प्रस्तावित सहयोग का वर्णन करें..."},
            "submit": "साझेदारी आवेदन जमा करें",
        },
        "projects": {"title": "विकास पहल", "subtitle": "TVK Ecosystem के भीतर वर्तमान क्षमता क्षेत्र और विकास-चरण पहल।", "items": make_projects([("ऊर्जा प्रणाली एकीकरण", "विकास में", "नवीकरणीय एकीकरण, औद्योगिक ऊर्जा समाधान और बुद्धिमान ऊर्जा प्रबंधन ढाँचे।"), ("स्मार्ट बुनियादी ढाँचा प्रौद्योगिकियाँ", "अनुसंधान", "डिजिटल बुनियादी ढाँचा प्रणालियाँ, निगरानी प्लेटफ़ॉर्म और महत्वपूर्ण बुनियादी ढाँचा प्रौद्योगिकी विकास।"), ("औद्योगिक AI और विश्लेषण", "सक्रिय अनुसंधान", "जटिल परिचालन वातावरण के लिए औद्योगिक AI, बुनियादी ढाँचा विश्लेषण और बुद्धिमान स्वचालन अनुसंधान।")])},
        "documents": {"title": "क्षमता दस्तावेज़", "subtitle": "कॉर्पोरेट वेबसाइट से आधिकारिक क्षमता ब्रीफ़ और संदर्भ सामग्री।", "openLabel": "दस्तावेज़ खोलें", "items": make_docs([("ऊर्जा प्रणाली क्षमताएँ", "ऊर्जा प्रणाली विकास, नवीकरणीय एकीकरण और Energy Intelligence का अवलोकन।"), ("बुनियादी ढाँचा प्रौद्योगिकियाँ", "स्मार्ट बुनियादी ढाँचा, डिजिटल प्रणालियाँ और महत्वपूर्ण बुनियादी ढाँचा प्रौद्योगिकी विकास।"), ("रणनीतिक साझेदारी", "साझेदारी मॉडल, सहयोग ढाँचे और संलग्नता प्रक्रिया।"), ("अंतर्दृष्टि और अनुसंधान", "ऊर्जा, बुनियादी ढाँचा और औद्योगिक प्रौद्योगिकी पर उद्योग दृष्टिकोण।")])},
        "support": {"title": "पार्टनर सहायता", "subtitle": "साझेदारी, तकनीकी और सामान्य पूछताछ के लिए TVK Infrastructure & Energy Systems टीम से संपर्क करें।", "disclaimer": "तत्काल परिचालन मामलों के लिए अपने निर्दिष्ट साझेदारी प्रतिनिधि से संपर्क करें। सामान्य पूछताछ के लिए प्रतिक्रिया समय: 1–2 कार्य दिवस।", "channels": make_channels([("साझेदारी पूछताछ", "रणनीतिक सहयोग, पायलट अवसर और दीर्घकालिक साझेदारी विकास।"), ("निवेशक संबंध", "TVK Ecosystem के भीतर पूँजी निर्माण और रणनीतिक निवेश चर्चा।"), ("तकनीकी सहायता", "पोर्टल पहुँच, आवेदन स्थिति और तकनीकी प्रश्न।"), ("सामान्य संपर्क", "TVK Infrastructure & Energy Systems के बारे में सामान्य पूछताछ।")])},
        "install": {"eyebrow": "Partner Portal ऐप", "title": "TVK Partner Portal ऐप प्राप्त करें", "subtitle": "अपने फ़ोन पर साझेदारी पोर्टल इंस्टॉल करें — आवेदन करें, पहलों को ट्रैक करें और होम स्क्रीन आइकन से क्षमता दस्तावेज़ों तक पहुँचें। आज होम स्क्रीन में जोड़ें के माध्यम से काम करता है; App Store सूचीकरण चरण 2 के लिए नियोजित।", "openApp": "Partner Portal खोलें", "howToInstall": "इंस्टॉल कैसे करें", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Partner Portal खोलें → साझा करें → होम स्क्रीन में जोड़ें"}, "android": {"title": "Android", "steps": "Chrome → Partner Portal खोलें → मेनू → ऐप इंस्टॉल करें या होम स्क्रीन में जोड़ें"}, "desktop": {"title": "डेस्कटॉप", "steps": "Chrome या Edge → पता पट्टी में इंस्टॉल आइकन, या Partner Portal को बुकमार्क करें"}},
    },
)

LOCALE_BUNDLES["tr"] = bundle(
    "Partner Portal", "Uygulamayı indir", "Partner Portal Uygulaması →",
    {
        "meta": {"title": "Partner Portal", "description": "TVK Infrastructure & Energy Systems iş ortağı portalı — stratejik ortaklıklar için başvurun, geliştirme girişimlerini takip edin ve yetkinlik belgelerine erişin."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Web sitesi",
        "navAria": "İş ortağı portalı navigasyonu",
        "nav": {"dashboard": "Kontrol Paneli", "apply": "Başvur", "projects": "Projeler", "documents": "Belgeler", "support": "Destek"},
        "dashboard": {
            "title": "İş Ortağı Kontrol Paneli",
            "subtitle": "TVK Ecosystem içinde ortaklık talebinizi, geliştirme girişimlerinizi ve sonraki adımlarınızı takip edin.",
            "stats": [{"label": "Ortaklık Aşaması", "value": "Geliştirme"}, {"label": "Aktif Girişimler", "value": "6 Alan"}, {"label": "Talep Durumu", "value": "Açık"}, {"label": "Portal Dilleri", "value": "25"}],
            "partnershipStatus": {"title": "Stratejik Ortaklık Hattı", "badge": "Geliştirme Aşamasında", "description": "TVK Infrastructure & Energy Systems araştırma, geliştirme ve ortaklık oluşturma aşamasındadır. Yapılandırılmış bir iş birliği görüşmesi başlatmak için başvuru gönderin."},
            "nextSteps": {"title": "Önerilen Sonraki Adımlar", "items": ["Kuruluş bilgilerinizle stratejik ortaklık başvurusu gönderin", "Enerji sistemleri ve altyapı teknolojilerindeki yetkinlik alanlarını inceleyin", "Projeler bölümündeki aktif geliştirme girişimlerini keşfedin", "Pilot veya iş birliği fırsatları için ortaklık ekibimizle iletişime geçin"]},
            "cta": "Ortaklık Başvurusu Gönder →",
        },
        "apply": {"title": "Ortaklık Başvurusu", "subtitle": "TVK Infrastructure & Energy Systems ile stratejik iş birliği için başvurun.", "intro": "Kuruluşunuzu tanıtmak ve ortaklık ilginizi açıklamak için bu formu doldurun. Ekibimiz tüm başvuruları inceler ve nitelikli taleplere yanıt verir.", "disclaimer": "Bu başvuru bağlayıcı bir anlaşma oluşturmaz. TVK Infrastructure & Energy Systems LTD geliştirme aşamasındadır — bilgiler operasyonel taahhütler değil, yetkinlik alanlarını açıklar."},
        "applyForm": {
            "interestAreas": ["Enerji Sistemleri", "Altyapı Teknolojileri", "Endüstriyel Çözümler", "Energy Intelligence", "Yapay Zeka Altyapısı", "Stratejik Ortaklıklar", "Genel Talep"],
            "success": {"title": "Başvuru Alındı", "message": "Ortaklık ilginiz için teşekkür ederiz. Ekibimiz başvurunuzu inceleyecek ve 5–10 iş günü içinde yanıt verecektir."},
            "fields": {"name": "Ad Soyad", "company": "Kuruluş", "role": "Görev / Unvan", "country": "Ülke", "email": "E-posta", "interest": "Ortaklık Alanı", "allocation": "Gösterge Kapsam (USD veya açıklama)", "message": "Ortaklık Teklifi", "required": "*"},
            "placeholders": {"name": "Adınız ve soyadınız", "company": "Kuruluş adı", "role": "Pozisyonunuz", "country": "Faaliyet ülkesi", "email": "professional@company.com", "interest": "Alan seçin", "allocation": "örn. Pilot proje, 500 bin USD iş birliği, teknoloji entegrasyonu", "message": "Kuruluşunuzu, stratejik uyumu ve önerilen iş birliğini açıklayın..."},
            "submit": "Ortaklık Başvurusu Gönder",
        },
        "projects": {"title": "Geliştirme Girişimleri", "subtitle": "TVK Ecosystem içindeki mevcut yetkinlik alanları ve geliştirme aşamasındaki girişimler.", "items": make_projects([("Enerji Sistemleri Entegrasyonu", "Geliştirme Aşamasında", "Yenilenebilir entegrasyon, endüstriyel enerji çözümleri ve akıllı enerji yönetimi çerçeveleri."), ("Akıllı Altyapı Teknolojileri", "Araştırma", "Dijital altyapı sistemleri, izleme platformları ve kritik altyapı teknolojisi geliştirme."), ("Endüstriyel Yapay Zeka ve Analitik", "Aktif Araştırma", "Karmaşık operasyonel ortamlar için endüstriyel yapay zeka, altyapı analitiği ve akıllı otomasyon araştırması.")])},
        "documents": {"title": "Yetkinlik Belgeleri", "subtitle": "Kurumsal web sitesinden resmi yetkinlik özetleri ve referans materyalleri.", "openLabel": "Belgeyi aç", "items": make_docs([("Enerji Sistemleri Yetkinlikleri", "Enerji sistemleri geliştirme, yenilenebilir entegrasyon ve Energy Intelligence genel bakışı."), ("Altyapı Teknolojileri", "Akıllı altyapı, dijital sistemler ve kritik altyapı teknolojisi geliştirme."), ("Stratejik Ortaklıklar", "Ortaklık modelleri, iş birliği çerçeveleri ve katılım süreci."), ("Görüşler ve Araştırma", "Enerji, altyapı ve endüstriyel teknoloji hakkında sektör perspektifleri.")])},
        "support": {"title": "İş Ortağı Desteği", "subtitle": "Ortaklık, teknik ve genel talepler için TVK Infrastructure & Energy Systems ekibiyle iletişime geçin.", "disclaimer": "Acil operasyonel konular için atanan ortaklık temsilcinizle iletişime geçin. Genel talepler için yanıt süreleri: 1–2 iş günü.", "channels": make_channels([("Ortaklık Talepleri", "Stratejik iş birliği, pilot fırsatları ve uzun vadeli ortaklık geliştirme."), ("Yatırımcı İlişkileri", "TVK Ecosystem içinde sermaye oluşturma ve stratejik yatırım görüşmeleri."), ("Teknik Destek", "Portal erişimi, başvuru durumu ve teknik sorular."), ("Genel İletişim", "TVK Infrastructure & Energy Systems hakkında genel talepler.")])},
        "install": {"eyebrow": "Partner Portal Uygulaması", "title": "TVK Partner Portal uygulamasını edinin", "subtitle": "Ortaklık portalını telefonunuza yükleyin — başvurun, girişimleri takip edin ve ana ekran simgesinden yetkinlik belgelerine erişin. Bugün Ana Ekrana Ekle ile çalışır; App Store listelemesi Faz 2 için planlandı.", "openApp": "Partner Portal'ı Aç", "howToInstall": "Nasıl yüklenir", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Partner Portal'ı Aç → Paylaş → Ana Ekrana Ekle"}, "android": {"title": "Android", "steps": "Chrome → Partner Portal'ı Aç → menü → Uygulamayı yükle veya Ana ekrana ekle"}, "desktop": {"title": "Masaüstü", "steps": "Chrome veya Edge → adres çubuğundaki yükleme simgesi veya Partner Portal'ı yer imlerine ekleyin"}},
    },
)

LOCALE_BUNDLES["sv"] = bundle(
    "Partner Portal", "Hämta appen", "Partner Portal-app →",
    {
        "meta": {"title": "Partner Portal", "description": "Partnerportal för TVK Infrastructure & Energy Systems — ansök om strategiska partnerskap, följ utvecklingsinitiativ och få tillgång till kapacitetsdokument."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Webbplats",
        "navAria": "Partnerportalnavigering",
        "nav": {"dashboard": "Instrumentpanel", "apply": "Ansök", "projects": "Projekt", "documents": "Dokument", "support": "Support"},
        "dashboard": {
            "title": "Partnerinstrumentpanel",
            "subtitle": "Följ din partnerskapsförfrågan, utvecklingsinitiativ och nästa steg inom TVK Ecosystem.",
            "stats": [{"label": "Partnerskapsfas", "value": "Utveckling"}, {"label": "Aktiva initiativ", "value": "6 områden"}, {"label": "Förfrågningsstatus", "value": "Öppen"}, {"label": "Portalspråk", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline för strategiska partnerskap", "badge": "Under utveckling", "description": "TVK Infrastructure & Energy Systems befinner sig i en fas av forskning, utveckling och partnerskapsuppbyggnad. Skicka in en ansökan för att inleda ett strukturerat samarbetssamtal."},
            "nextSteps": {"title": "Rekommenderade nästa steg", "items": ["Skicka in en ansökan om strategiskt partnerskap med din organisations uppgifter", "Granska kapacitetsområden inom energisystem och infrastrukturteknik", "Utforska aktiva utvecklingsinitiativ i projektsektionen", "Kontakta vårt partnerskapsteam för pilot- eller samarbetsmöjligheter"]},
            "cta": "Skicka partnerskapsansökan →",
        },
        "apply": {"title": "Partnerskapsansökan", "subtitle": "Ansök om strategiskt samarbete med TVK Infrastructure & Energy Systems.", "intro": "Fyll i detta formulär för att presentera din organisation och beskriva ditt partnerskapsintresse. Vårt team granskar alla ansökningar och svarar på kvalificerade förfrågningar.", "disclaimer": "Denna ansökan utgör inte ett bindande avtal. TVK Infrastructure & Energy Systems LTD är i utvecklingsfas — informationen beskriver kapacitetsområden, inte operativa åtaganden."},
        "applyForm": {
            "interestAreas": ["Energisystem", "Infrastrukturteknik", "Industriella lösningar", "Energy Intelligence", "AI-infrastruktur", "Strategiska partnerskap", "Allmän förfrågan"],
            "success": {"title": "Ansökan mottagen", "message": "Tack för ditt partnerskapsintresse. Vårt team granskar din ansökan och svarar inom 5–10 arbetsdagar."},
            "fields": {"name": "Fullständigt namn", "company": "Organisation", "role": "Roll / Titel", "country": "Land", "email": "E-post", "interest": "Partnerskapsområde", "allocation": "Indikativ omfattning (USD eller beskrivning)", "message": "Partnerskapsförslag", "required": "*"},
            "placeholders": {"name": "Ditt fullständiga namn", "company": "Organisationens namn", "role": "Din befattning", "country": "Verksamhetsland", "email": "professional@company.com", "interest": "Välj ett område", "allocation": "t.ex. Pilotprojekt, samarbete på 500 000 USD, teknikintegration", "message": "Beskriv din organisation, strategisk passform och föreslaget samarbete..."},
            "submit": "Skicka partnerskapsansökan",
        },
        "projects": {"title": "Utvecklingsinitiativ", "subtitle": "Aktuella kapacitetsområden och initiativ i utvecklingsfas inom TVK Ecosystem.", "items": make_projects([("Integration av energisystem", "Under utveckling", "Integration av förnybar energi, industriella energilösningar och intelligenta energihanteringsramverk."), ("Smart infrastrukturteknik", "Forskning", "Digitala infrastruktursystem, övervakningsplattformar och utveckling av kritisk infrastrukturteknik."), ("Industriell AI och analys", "Aktiv forskning", "Industriell AI, infrastrukturanalys och forskning om intelligent automatisering för komplexa operativa miljöer.")])},
        "documents": {"title": "Kapacitetsdokument", "subtitle": "Officiella kapacitetsöversikter och referensmaterial från företagets webbplats.", "openLabel": "Öppna dokument", "items": make_docs([("Energisystemskapaciteter", "Översikt över energisystemutveckling, integration av förnybar energi och Energy Intelligence."), ("Infrastrukturteknik", "Smart infrastruktur, digitala system och utveckling av kritisk infrastrukturteknik."), ("Strategiska partnerskap", "Partnerskapsmodeller, samarbetsramverk och engagemangsprocess."), ("Insikter och forskning", "Branschperspektiv om energi, infrastruktur och industriteknik.")])},
        "support": {"title": "Partnersupport", "subtitle": "Kontakta TVK Infrastructure & Energy Systems-teamet för partnerskaps-, tekniska och allmänna förfrågningar.", "disclaimer": "För brådskande operativa frågor, kontakta din tilldelade partnerskapsrepresentant. Svarstider: 1–2 arbetsdagar för allmänna förfrågningar.", "channels": make_channels([("Partnerskapsförfrågningar", "Strategiskt samarbete, pilotmöjligheter och långsiktig partnerskapsutveckling."), ("Investerarrelationer", "Kapitalbildning och strategiska investeringsdiskussioner inom TVK Ecosystem."), ("Teknisk support", "Portalåtkomst, ansökningsstatus och tekniska frågor."), ("Allmän kontakt", "Allmänna förfrågningar om TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Partner Portal-app", "title": "Skaffa TVK Partner Portal-appen", "subtitle": "Installera partnerskapsportalen på din telefon — ansök, följ initiativ och få tillgång till kapacitetsdokument från en hemskärmsikon. Fungerar idag via Lägg till på hemskärmen; App Store-notering planerad för fas 2.", "openApp": "Öppna Partner Portal", "howToInstall": "Så installerar du", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Öppna Partner Portal → Dela → Lägg till på hemskärmen"}, "android": {"title": "Android", "steps": "Chrome → Öppna Partner Portal → meny → Installera app eller Lägg till på startskärmen"}, "desktop": {"title": "Skrivbord", "steps": "Chrome eller Edge → installationsikon i adressfältet, eller bokmärk Partner Portal"}},
    },
)

LOCALE_BUNDLES["no"] = bundle(
    "Partner Portal", "Last ned appen", "Partner Portal-app →",
    {
        "meta": {"title": "Partner Portal", "description": "Partnerportal for TVK Infrastructure & Energy Systems — søk om strategiske partnerskap, følg utviklingsinitiativer og få tilgang til kapasitetsdokumenter."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Nettsted",
        "navAria": "Partnerportalnavigasjon",
        "nav": {"dashboard": "Dashbord", "apply": "Søk", "projects": "Prosjekter", "documents": "Dokumenter", "support": "Support"},
        "dashboard": {
            "title": "Partnerdashbord",
            "subtitle": "Følg partnerskapsforespørselen din, utviklingsinitiativer og neste steg innen TVK Ecosystem.",
            "stats": [{"label": "Partnerskapsfase", "value": "Utvikling"}, {"label": "Aktive initiativer", "value": "6 områder"}, {"label": "Forespørselsstatus", "value": "Åpen"}, {"label": "Portalspråk", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline for strategiske partnerskap", "badge": "Under utvikling", "description": "TVK Infrastructure & Energy Systems er i en fase med forskning, utvikling og partnerskapsbygging. Send inn en søknad for å starte en strukturert samtale om samarbeid."},
            "nextSteps": {"title": "Anbefalte neste steg", "items": ["Send inn en søknad om strategisk partnerskap med organisasjonsdetaljene dine", "Gjennomgå kapasitetsområder innen energisystemer og infrastrukturteknologi", "Utforsk aktive utviklingsinitiativer i prosjektseksjonen", "Kontakt partnerskapsteamet vårt for pilot- eller samarbeidsmuligheter"]},
            "cta": "Send partnerskapssøknad →",
        },
        "apply": {"title": "Partnerskapssøknad", "subtitle": "Søk om strategisk samarbeid med TVK Infrastructure & Energy Systems.", "intro": "Fyll ut dette skjemaet for å presentere organisasjonen din og beskrive partnerskapsinteressen. Teamet vårt vurderer alle søknader og svarer på kvalifiserte forespørsler.", "disclaimer": "Denne søknaden utgjør ikke en bindende avtale. TVK Infrastructure & Energy Systems LTD er i utviklingsfase — informasjonen beskriver kapasitetsområder, ikke operative forpliktelser."},
        "applyForm": {
            "interestAreas": ["Energisystemer", "Infrastrukturteknologi", "Industrielle løsninger", "Energy Intelligence", "AI-infrastruktur", "Strategiske partnerskap", "Generell forespørsel"],
            "success": {"title": "Søknad mottatt", "message": "Takk for partnerskapsinteressen. Teamet vårt vil vurdere søknaden din og svare innen 5–10 virkedager."},
            "fields": {"name": "Fullt navn", "company": "Organisasjon", "role": "Rolle / Tittel", "country": "Land", "email": "E-post", "interest": "Partnerskapsområde", "allocation": "Indikativ omfang (USD eller beskrivelse)", "message": "Partnerskapsforslag", "required": "*"},
            "placeholders": {"name": "Ditt fulle navn", "company": "Organisasjonens navn", "role": "Din stilling", "country": "Driftsland", "email": "professional@company.com", "interest": "Velg et område", "allocation": "f.eks. Pilotprosjekt, samarbeid på 500 000 USD, teknologiintegrasjon", "message": "Beskriv organisasjonen din, strategisk passform og foreslått samarbeid..."},
            "submit": "Send partnerskapssøknad",
        },
        "projects": {"title": "Utviklingsinitiativer", "subtitle": "Aktuelle kapasitetsområder og initiativer i utviklingsfase innen TVK Ecosystem.", "items": make_projects([("Integrasjon av energisystemer", "Under utvikling", "Integrasjon av fornybar energi, industrielle energiløsninger og intelligente energistyringsrammeverk."), ("Smart infrastrukturteknologi", "Forskning", "Digitale infrastruktursystemer, overvåkingsplattformer og utvikling av kritisk infrastrukturteknologi."), ("Industriell AI og analyse", "Aktiv forskning", "Industriell AI, infrastrukturanalyse og forskning på intelligent automatisering for komplekse operative miljøer.")])},
        "documents": {"title": "Kapasitetsdokumenter", "subtitle": "Offisielle kapasitetsoversikter og referansematerialer fra bedriftens nettsted.", "openLabel": "Åpne dokument", "items": make_docs([("Energisystemkapasiteter", "Oversikt over energisystemutvikling, integrasjon av fornybar energi og Energy Intelligence."), ("Infrastrukturteknologi", "Smart infrastruktur, digitale systemer og utvikling av kritisk infrastrukturteknologi."), ("Strategiske partnerskap", "Partnerskapsmodeller, samarbeidsrammeverk og engasjementsprosess."), ("Innsikt og forskning", "Bransjeperspektiver om energi, infrastruktur og industriteknologi.")])},
        "support": {"title": "Partnerstøtte", "subtitle": "Kontakt TVK Infrastructure & Energy Systems-teamet for partnerskaps-, tekniske og generelle forespørsler.", "disclaimer": "For presserende operative saker, kontakt din tildelte partnerskapsrepresentant. Svartider: 1–2 virkedager for generelle forespørsler.", "channels": make_channels([("Partnerskapsforespørsler", "Strategisk samarbeid, pilotmuligheter og langsiktig partnerskapsutvikling."), ("Investor Relations", "Kapitaldannelse og strategiske investeringssamtaler innen TVK Ecosystem."), ("Teknisk støtte", "Portaltilgang, søknadsstatus og tekniske spørsmål."), ("Generell kontakt", "Generelle forespørsler om TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Partner Portal-app", "title": "Skaff TVK Partner Portal-appen", "subtitle": "Installer partnerskapsportalen på telefonen — søk, følg initiativer og få tilgang til kapasitetsdokumenter fra et hjemskjermikon. Fungerer i dag via Legg til på Hjem-skjerm; App Store-notering planlagt for fase 2.", "openApp": "Åpne Partner Portal", "howToInstall": "Slik installerer du", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Åpne Partner Portal → Del → Legg til på Hjem-skjerm"}, "android": {"title": "Android", "steps": "Chrome → Åpne Partner Portal → meny → Installer app eller Legg til på startskjerm"}, "desktop": {"title": "Skrivebord", "steps": "Chrome eller Edge → installeringsikon i adressefeltet, eller bokmerk Partner Portal"}},
    },
)

LOCALE_BUNDLES["da"] = bundle(
    "Partner Portal", "Hent appen", "Partner Portal-app →",
    {
        "meta": {"title": "Partner Portal", "description": "Partnerportal for TVK Infrastructure & Energy Systems — ansøg om strategiske partnerskaber, følg udviklingsinitiativer og få adgang til kapacitetsdokumenter."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Website",
        "navAria": "Partnerportalnavigation",
        "nav": {"dashboard": "Dashboard", "apply": "Ansøg", "projects": "Projekter", "documents": "Dokumenter", "support": "Support"},
        "dashboard": {
            "title": "Partnerdashboard",
            "subtitle": "Følg din partnerskabsforespørgsel, udviklingsinitiativer og næste skridt inden for TVK Ecosystem.",
            "stats": [{"label": "Partnerskabsfase", "value": "Udvikling"}, {"label": "Aktive initiativer", "value": "6 områder"}, {"label": "Forespørgselsstatus", "value": "Åben"}, {"label": "Portalsprog", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline for strategiske partnerskaber", "badge": "Under udvikling", "description": "TVK Infrastructure & Energy Systems er i en fase med forskning, udvikling og opbygning af partnerskaber. Indsend en ansøgning for at starte en struktureret samtale om samarbejde."},
            "nextSteps": {"title": "Anbefalede næste skridt", "items": ["Indsend en ansøgning om strategisk partnerskab med din organisations oplysninger", "Gennemgå kapacitetsområder inden for energisystemer og infrastrukturteknologi", "Udforsk aktive udviklingsinitiativer i projektsektionen", "Kontakt vores partnerskabsteam for pilot- eller samarbejdsmuligheder"]},
            "cta": "Indsend partnerskabsansøgning →",
        },
        "apply": {"title": "Partnerskabsansøgning", "subtitle": "Ansøg om strategisk samarbejde med TVK Infrastructure & Energy Systems.", "intro": "Udfyld denne formular for at præsentere din organisation og beskrive din partnerskabsinteresse. Vores team gennemgår alle ansøgninger og svarer på kvalificerede forespørgsler.", "disclaimer": "Denne ansøgning udgør ikke en bindende aftale. TVK Infrastructure & Energy Systems LTD er i udviklingsfase — oplysningerne beskriver kapacitetsområder, ikke operationelle forpligtelser."},
        "applyForm": {
            "interestAreas": ["Energisystemer", "Infrastrukturteknologi", "Industrielle løsninger", "Energy Intelligence", "AI-infrastruktur", "Strategiske partnerskaber", "Generel forespørgsel"],
            "success": {"title": "Ansøgning modtaget", "message": "Tak for din partnerskabsinteresse. Vores team gennemgår din ansøgning og svarer inden for 5–10 hverdage."},
            "fields": {"name": "Fulde navn", "company": "Organisation", "role": "Rolle / Titel", "country": "Land", "email": "E-mail", "interest": "Partnerskabsområde", "allocation": "Indikativ omfang (USD eller beskrivelse)", "message": "Partnerskabsforslag", "required": "*"},
            "placeholders": {"name": "Dit fulde navn", "company": "Organisationens navn", "role": "Din stilling", "country": "Driftsland", "email": "professional@company.com", "interest": "Vælg et område", "allocation": "f.eks. Pilotprojekt, samarbejde på 500.000 USD, teknologiintegration", "message": "Beskriv din organisation, strategisk pasform og foreslået samarbejde..."},
            "submit": "Indsend partnerskabsansøgning",
        },
        "projects": {"title": "Udviklingsinitiativer", "subtitle": "Aktuelle kapacitetsområder og initiativer i udviklingsfase inden for TVK Ecosystem.", "items": make_projects([("Integration af energisystemer", "Under udvikling", "Integration af vedvarende energi, industrielle energiløsninger og intelligente energistyringssystemer."), ("Smart infrastrukturteknologi", "Forskning", "Digitale infrastruktursystemer, overvågningsplatforme og udvikling af kritisk infrastrukturteknologi."), ("Industriel AI og analyse", "Aktiv forskning", "Industriel AI, infrastrukturanalyse og forskning i intelligent automatisering for komplekse operationelle miljøer.")])},
        "documents": {"title": "Kapacitetsdokumenter", "subtitle": "Officielle kapacitetsoversigter og referencematerialer fra virksomhedens website.", "openLabel": "Åbn dokument", "items": make_docs([("Energisystemkapaciteter", "Oversigt over energisystemudvikling, integration af vedvarende energi og Energy Intelligence."), ("Infrastrukturteknologi", "Smart infrastruktur, digitale systemer og udvikling af kritisk infrastrukturteknologi."), ("Strategiske partnerskaber", "Partnerskabsmodeller, samarbejdsrammer og engagementsproces."), ("Indsigt og forskning", "Brancheperspektiver om energi, infrastruktur og industriteknologi.")])},
        "support": {"title": "Partnersupport", "subtitle": "Kontakt TVK Infrastructure & Energy Systems-teamet for partnerskabs-, tekniske og generelle forespørgsler.", "disclaimer": "For presserende operationelle sager, kontakt din tildelte partnerskabsrepræsentant. Svartider: 1–2 hverdage for generelle forespørgsler.", "channels": make_channels([("Partnerskabsforespørgsler", "Strategisk samarbejde, pilotmuligheder og langsigtet partnerskabsudvikling."), ("Investor Relations", "Kapitaldannelse og strategiske investeringssamtaler inden for TVK Ecosystem."), ("Teknisk support", "Portaladgang, ansøgningsstatus og tekniske spørgsmål."), ("Generel kontakt", "Generelle forespørgsler om TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Partner Portal-app", "title": "Hent TVK Partner Portal-appen", "subtitle": "Installer partnerskabsportalen på din telefon — ansøg, følg initiativer og få adgang til kapacitetsdokumenter fra et startskærmsikon. Fungerer i dag via Føj til startskærm; App Store-notering planlagt til fase 2.", "openApp": "Åbn Partner Portal", "howToInstall": "Sådan installeres", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Åbn Partner Portal → Del → Føj til startskærm"}, "android": {"title": "Android", "steps": "Chrome → Åbn Partner Portal → menu → Installer app eller Føj til startskærm"}, "desktop": {"title": "Desktop", "steps": "Chrome eller Edge → installationsikon i adresselinjen, eller bogmærk Partner Portal"}},
    },
)

LOCALE_BUNDLES["fi"] = bundle(
    "Partner Portal", "Hae sovellus", "Partner Portal -sovellus →",
    {
        "meta": {"title": "Partner Portal", "description": "TVK Infrastructure & Energy Systems -kumppaniportaali — hae strategisia kumppanuuksia, seuraa kehitysaloitteita ja käytä kyvykkyysdokumentteja."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Verkkosivusto",
        "navAria": "Kumppaniportaalin navigointi",
        "nav": {"dashboard": "Hallintapaneeli", "apply": "Hae", "projects": "Hankkeet", "documents": "Asiakirjat", "support": "Tuki"},
        "dashboard": {
            "title": "Kumppanin hallintapaneeli",
            "subtitle": "Seuraa kumppanuuskyselyäsi, kehitysaloitteita ja seuraavia toimenpiteitä TVK Ecosystemissa.",
            "stats": [{"label": "Kumppanuusvaihe", "value": "Kehitys"}, {"label": "Aktiiviset aloitteet", "value": "6 aluetta"}, {"label": "Kyselyn tila", "value": "Avoin"}, {"label": "Portaalin kielet", "value": "25"}],
            "partnershipStatus": {"title": "Strategisten kumppanuuksien putki", "badge": "Kehityksessä", "description": "TVK Infrastructure & Energy Systems on tutkimus-, kehitys- ja kumppanuusrakentamisvaiheessa. Lähetä hakemus aloittaaksesi jäsennellyn yhteistyökeskustelun."},
            "nextSteps": {"title": "Suositellut seuraavat askeleet", "items": ["Lähetä strategisen kumppanuuden hakemus organisaatiosi tiedoilla", "Tutustu energiajärjestelmien ja infrastruktuuriteknologioiden kyvykkyysalueisiin", "Tutki aktiivisia kehitysaloitteita hankkeet-osiossa", "Ota yhteyttä kumppanuustiimiimme pilotti- tai yhteistyömahdollisuuksista"]},
            "cta": "Lähetä kumppanuushakemus →",
        },
        "apply": {"title": "Kumppanuushakemus", "subtitle": "Hae strategista yhteistyötä TVK Infrastructure & Energy Systemsin kanssa.", "intro": "Täytä tämä lomake esitelläksesi organisaatiosi ja kuvataksesi kumppanuuskiinnostuksesi. Tiimimme käy läpi kaikki hakemukset ja vastaa päteviin kyselyihin.", "disclaimer": "Tämä hakemus ei muodosta sitovaa sopimusta. TVK Infrastructure & Energy Systems LTD on kehitysvaiheessa — tiedot kuvaavat kyvykkyysalueita, eivät operatiivisia sitoumuksia."},
        "applyForm": {
            "interestAreas": ["Energiajärjestelmät", "Infrastruktuuriteknologiat", "Teolliset ratkaisut", "Energy Intelligence", "Tekoälyinfrastruktuuri", "Strategiset kumppanuudet", "Yleinen kysely"],
            "success": {"title": "Hakemus vastaanotettu", "message": "Kiitos kumppanuuskiinnostuksestasi. Tiimimme käy hakemuksesi läpi ja vastaa 5–10 arkipäivän kuluessa."},
            "fields": {"name": "Koko nimi", "company": "Organisaatio", "role": "Rooli / Nimike", "country": "Maa", "email": "Sähköposti", "interest": "Kumppanuusalue", "allocation": "Arvioitu laajuus (USD tai kuvaus)", "message": "Kumppanuusehdotus", "required": "*"},
            "placeholders": {"name": "Koko nimesi", "company": "Organisaation nimi", "role": "Asemasi", "country": "Toimintamaa", "email": "professional@company.com", "interest": "Valitse alue", "allocation": "esim. Pilottihanke, 500 000 USD:n yhteistyö, teknologiaintegraatio", "message": "Kuvaile organisaatiosi, strateginen sopivuus ja ehdotettu yhteistyö..."},
            "submit": "Lähetä kumppanuushakemus",
        },
        "projects": {"title": "Kehitysaloitteet", "subtitle": "Nykyiset kyvykkyysalueet ja kehitysvaiheen aloitteet TVK Ecosystemissa.", "items": make_projects([("Energiajärjestelmien integrointi", "Kehityksessä", "Uusiutuvan energian integrointi, teolliset energiaratkaisut ja älykkäät energianhallintakehykset."), ("Älykkäät infrastruktuuriteknologiat", "Tutkimus", "Digitaaliset infrastruktuurijärjestelmät, valvonta-alustat ja kriittisen infrastruktuurin teknologiakehitys."), ("Teollinen tekoäly ja analytiikka", "Aktiivinen tutkimus", "Teollinen tekoäly, infrastruktuurianalytiikka ja älykkään automaation tutkimus monimutkaisissa operatiivisissa ympäristöissä.")])},
        "documents": {"title": "Kyvykkyysasiakirjat", "subtitle": "Viralliset kyvykkyyskatsaukset ja viitemateriaalit yrityksen verkkosivustolta.", "openLabel": "Avaa asiakirja", "items": make_docs([("Energiajärjestelmien kyvykkyydet", "Yleiskatsaus energiajärjestelmien kehityksestä, uusiutuvan energian integroinnista ja Energy Intelligencesta."), ("Infrastruktuuriteknologiat", "Älykäs infrastruktuuri, digitaaliset järjestelmät ja kriittisen infrastruktuurin teknologiakehitys."), ("Strategiset kumppanuudet", "Kumppanuusmallit, yhteistyökehykset ja osallistumisprosessi."), ("Näkemykset ja tutkimus", "Toimialan näkökulmia energiasta, infrastruktuurista ja teollisuusteknologiasta.")])},
        "support": {"title": "Kumppanituki", "subtitle": "Ota yhteyttä TVK Infrastructure & Energy Systems -tiimiin kumppanuus-, teknisiä ja yleisiä kyselyitä varten.", "disclaimer": "Kiireellisissä operatiivisissa asioissa ota yhteyttä nimettyyn kumppanuusedustajaasi. Vastausajat: 1–2 arkipäivää yleisiin kyselyihin.", "channels": make_channels([("Kumppanuuskyselyt", "Strateginen yhteistyö, pilottimahdollisuudet ja pitkäaikainen kumppanuuskehitys."), ("Sijoittajasuhteet", "Pääoman muodostus ja strategiset sijoituskeskustelut TVK Ecosystemissa."), ("Tekninen tuki", "Portaalin käyttö, hakemuksen tila ja tekniset kysymykset."), ("Yleinen yhteystieto", "Yleiset kyselyt TVK Infrastructure & Energy Systemsistä.")])},
        "install": {"eyebrow": "Partner Portal -sovellus", "title": "Hanki TVK Partner Portal -sovellus", "subtitle": "Asenna kumppanuusportaali puhelimeesi — hae, seuraa aloitteita ja käytä kyvykkyysdokumentteja kotinäytön kuvakkeesta. Toimii tänään Lisää kotinäytölle -toiminnolla; App Store -julkaisu suunniteltu vaiheeseen 2.", "openApp": "Avaa Partner Portal", "howToInstall": "Asennusohjeet", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Avaa Partner Portal → Jaa → Lisää kotinäytölle"}, "android": {"title": "Android", "steps": "Chrome → Avaa Partner Portal → valikko → Asenna sovellus tai Lisää aloitusnäytölle"}, "desktop": {"title": "Työpöytä", "steps": "Chrome tai Edge → asennuskuvake osoitepalkissa tai lisää Partner Portal kirjanmerkkeihin"}},
    },
)

LOCALE_BUNDLES["cs"] = bundle(
    "Partner Portal", "Stáhnout aplikaci", "Aplikace Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Partnerský portál TVK Infrastructure & Energy Systems — žádejte o strategická partnerství, sledujte rozvojové iniciativy a přistupujte k dokumentům o kompetencích."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Web",
        "navAria": "Navigace partnerského portálu",
        "nav": {"dashboard": "Přehled", "apply": "Přihlásit se", "projects": "Projekty", "documents": "Dokumenty", "support": "Podpora"},
        "dashboard": {
            "title": "Partnerský přehled",
            "subtitle": "Sledujte svůj partnerský dotaz, rozvojové iniciativy a další kroky v rámci TVK Ecosystem.",
            "stats": [{"label": "Fáze partnerství", "value": "Vývoj"}, {"label": "Aktivní iniciativy", "value": "6 oblastí"}, {"label": "Stav dotazu", "value": "Otevřený"}, {"label": "Jazyky portálu", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline strategických partnerství", "badge": "Ve vývoji", "description": "TVK Infrastructure & Energy Systems je ve fázi výzkumu, vývoje a budování partnerství. Odešlete přihlášku a zahajte strukturovanou spolupracující konverzaci."},
            "nextSteps": {"title": "Doporučené další kroky", "items": ["Odešlete přihlášku ke strategickému partnerství s údaji o vaší organizaci", "Prostudujte oblasti kompetencí v energetických systémech a infrastrukturních technologiích", "Prozkoumejte aktivní rozvojové iniciativy v sekci projektů", "Kontaktujte náš partnerský tým ohledně pilotních nebo spolupracujících příležitostí"]},
            "cta": "Odeslat partnerskou přihlášku →",
        },
        "apply": {"title": "Partnerská přihláška", "subtitle": "Přihlaste se ke strategické spolupráci s TVK Infrastructure & Energy Systems.", "intro": "Vyplňte tento formulář, abyste představili svou organizaci a popsali zájem o partnerství. Náš tým posoudí všechny přihlášky a odpoví na kvalifikované dotazy.", "disclaimer": "Tato přihláška nepředstavuje závaznou smlouvu. TVK Infrastructure & Energy Systems LTD je ve fázi vývoje — informace popisují oblasti kompetencí, nikoli provozní závazky."},
        "applyForm": {
            "interestAreas": ["Energetické systémy", "Infrastrukturní technologie", "Průmyslová řešení", "Energy Intelligence", "AI infrastruktura", "Strategická partnerství", "Obecný dotaz"],
            "success": {"title": "Přihláška přijata", "message": "Děkujeme za váš zájem o partnerství. Náš tým posoudí vaši přihlášku a odpoví do 5–10 pracovních dnů."},
            "fields": {"name": "Celé jméno", "company": "Organizace", "role": "Role / Titul", "country": "Země", "email": "E-mail", "interest": "Oblast partnerství", "allocation": "Orientační rozsah (USD nebo popis)", "message": "Návrh partnerství", "required": "*"},
            "placeholders": {"name": "Vaše celé jméno", "company": "Název organizace", "role": "Vaše pozice", "country": "Země působení", "email": "professional@company.com", "interest": "Vyberte oblast", "allocation": "např. Pilotní projekt, spolupráce 500 tis. USD, integrace technologií", "message": "Popište svou organizaci, strategickou shodu a navrhovanou spolupráci..."},
            "submit": "Odeslat partnerskou přihlášku",
        },
        "projects": {"title": "Rozvojové iniciativy", "subtitle": "Aktuální oblasti kompetencí a iniciativy ve fázi vývoje v rámci TVK Ecosystem.", "items": make_projects([("Integrace energetických systémů", "Ve vývoji", "Integrace obnovitelných zdrojů, průmyslová energetická řešení a inteligentní rámce pro řízení energie."), ("Technologie chytré infrastruktury", "Výzkum", "Digitální infrastrukturní systémy, monitorovací platformy a vývoj technologií kritické infrastruktury."), ("Průmyslová AI a analytika", "Aktivní výzkum", "Průmyslová AI, infrastrukturní analytika a výzkum inteligentní automatizace pro složitá provozní prostředí.")])},
        "documents": {"title": "Dokumenty kompetencí", "subtitle": "Oficiální přehledy kompetencí a referenční materiály z firemního webu.", "openLabel": "Otevřít dokument", "items": make_docs([("Kompetence v energetických systémech", "Přehled vývoje energetických systémů, integrace obnovitelných zdrojů a Energy Intelligence."), ("Infrastrukturní technologie", "Chytrá infrastruktura, digitální systémy a vývoj technologií kritické infrastruktury."), ("Strategická partnerství", "Modely partnerství, rámce spolupráce a proces zapojení."), ("Pohledy a výzkum", "Oborové perspektivy k energii, infrastruktuře a průmyslovým technologiím.")])},
        "support": {"title": "Partnerská podpora", "subtitle": "Kontaktujte tým TVK Infrastructure & Energy Systems ohledně partnerských, technických a obecných dotazů.", "disclaimer": "V naléhavých provozních záležitostech kontaktujte svého přiděleného partnerského zástupce. Doba odpovědi: 1–2 pracovní dny pro obecné dotazy.", "channels": make_channels([("Partnerské dotazy", "Strategická spolupráce, pilotní příležitosti a dlouhodobý rozvoj partnerství."), ("Vztahy s investory", "Formování kapitálu a strategické investiční diskuse v rámci TVK Ecosystem."), ("Technická podpora", "Přístup k portálu, stav přihlášky a technické otázky."), ("Obecný kontakt", "Obecné dotazy týkající se TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Aplikace Partner Portal", "title": "Získejte aplikaci TVK Partner Portal", "subtitle": "Nainstalujte partnerský portál do telefonu — přihlaste se, sledujte iniciativy a přistupujte k dokumentům kompetencí z ikony na domovské obrazovce. Funguje dnes přes Přidat na plochu; uvedení v App Store plánováno pro fázi 2.", "openApp": "Otevřít Partner Portal", "howToInstall": "Jak nainstalovat", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Otevřít Partner Portal → Sdílet → Přidat na plochu"}, "android": {"title": "Android", "steps": "Chrome → Otevřít Partner Portal → menu → Nainstalovat aplikaci nebo Přidat na plochu"}, "desktop": {"title": "Počítač", "steps": "Chrome nebo Edge → ikona instalace v adresním řádku nebo uložte Partner Portal do záložek"}},
    },
)

LOCALE_BUNDLES["ro"] = bundle(
    "Partner Portal", "Descarcă aplicația", "Aplicația Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Portal parteneri TVK Infrastructure & Energy Systems — aplicați pentru parteneriate strategice, urmăriți inițiativele de dezvoltare și accesați documentele de competențe."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Site web",
        "navAria": "Navigare portal parteneri",
        "nav": {"dashboard": "Panou", "apply": "Aplică", "projects": "Proiecte", "documents": "Documente", "support": "Suport"},
        "dashboard": {
            "title": "Panou partener",
            "subtitle": "Urmăriți solicitarea de parteneriat, inițiativele de dezvoltare și pașii următori în cadrul TVK Ecosystem.",
            "stats": [{"label": "Etapa parteneriatului", "value": "Dezvoltare"}, {"label": "Inițiative active", "value": "6 domenii"}, {"label": "Starea solicitării", "value": "Deschis"}, {"label": "Limbi portal", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline parteneriate strategice", "badge": "În dezvoltare", "description": "TVK Infrastructure & Energy Systems se află într-o etapă de cercetare, dezvoltare și construire a parteneriatelor. Trimiteți o aplicație pentru a începe o conversație structurată de colaborare."},
            "nextSteps": {"title": "Pași următori recomandați", "items": ["Trimiteți o aplicație de parteneriat strategic cu detaliile organizației dvs.", "Revizuiți domeniile de competențe în sisteme energetice și tehnologii de infrastructură", "Explorați inițiativele active de dezvoltare în secțiunea proiecte", "Contactați echipa noastră de parteneriate pentru oportunități pilot sau de colaborare"]},
            "cta": "Trimite aplicația de parteneriat →",
        },
        "apply": {"title": "Aplicație de parteneriat", "subtitle": "Aplicați pentru colaborare strategică cu TVK Infrastructure & Energy Systems.", "intro": "Completați acest formular pentru a vă prezenta organizația și a descrie interesul pentru parteneriat. Echipa noastră analizează toate aplicațiile și răspunde solicitărilor calificate.", "disclaimer": "Această aplicație nu constituie un acord obligatoriu. TVK Infrastructure & Energy Systems LTD se află într-o etapă de dezvoltare — informațiile descriu domenii de competențe, nu angajamente operaționale."},
        "applyForm": {
            "interestAreas": ["Sisteme energetice", "Tehnologii de infrastructură", "Soluții industriale", "Energy Intelligence", "Infrastructură AI", "Parteneriate strategice", "Solicitare generală"],
            "success": {"title": "Aplicație primită", "message": "Vă mulțumim pentru interesul față de parteneriat. Echipa noastră va analiza aplicația și va răspunde în 5–10 zile lucrătoare."},
            "fields": {"name": "Nume complet", "company": "Organizație", "role": "Rol / Titlu", "country": "Țară", "email": "E-mail", "interest": "Domeniu de parteneriat", "allocation": "Domeniu indicativ (USD sau descriere)", "message": "Propunere de parteneriat", "required": "*"},
            "placeholders": {"name": "Numele dvs. complet", "company": "Numele organizației", "role": "Poziția dvs.", "country": "Țara de operare", "email": "professional@company.com", "interest": "Selectați un domeniu", "allocation": "de ex. Proiect pilot, colaborare de 500.000 USD, integrare tehnologică", "message": "Descrieți organizația, potrivirea strategică și colaborarea propusă..."},
            "submit": "Trimite aplicația de parteneriat",
        },
        "projects": {"title": "Inițiative de dezvoltare", "subtitle": "Domenii actuale de competențe și inițiative în etapa de dezvoltare în cadrul TVK Ecosystem.", "items": make_projects([("Integrarea sistemelor energetice", "În dezvoltare", "Integrarea energiei regenerabile, soluții energetice industriale și cadre inteligente de management al energiei."), ("Tehnologii de infrastructură inteligentă", "Cercetare", "Sisteme de infrastructură digitală, platforme de monitorizare și dezvoltarea tehnologiilor de infrastructură critică."), ("AI industrial și analitică", "Cercetare activă", "AI industrial, analitică de infrastructură și cercetare în automatizare inteligentă pentru medii operaționale complexe.")])},
        "documents": {"title": "Documente de competențe", "subtitle": "Rezumate oficiale de competențe și materiale de referință de pe site-ul corporativ.", "openLabel": "Deschide documentul", "items": make_docs([("Competențe în sisteme energetice", "Prezentare generală a dezvoltării sistemelor energetice, integrării regenerabile și Energy Intelligence."), ("Tehnologii de infrastructură", "Infrastructură inteligentă, sisteme digitale și dezvoltarea tehnologiilor de infrastructură critică."), ("Parteneriate strategice", "Modele de parteneriat, cadre de colaborare și proces de implicare."), ("Perspective și cercetare", "Perspective de industrie privind energia, infrastructura și tehnologia industrială.")])},
        "support": {"title": "Suport parteneri", "subtitle": "Contactați echipa TVK Infrastructure & Energy Systems pentru solicitări de parteneriat, tehnice și generale.", "disclaimer": "Pentru probleme operaționale urgente, contactați reprezentantul de parteneriat desemnat. Timp de răspuns: 1–2 zile lucrătoare pentru solicitări generale.", "channels": make_channels([("Solicitări de parteneriat", "Colaborare strategică, oportunități pilot și dezvoltarea parteneriatelor pe termen lung."), ("Relații cu investitorii", "Formarea capitalului și discuții despre investiții strategice în cadrul TVK Ecosystem."), ("Suport tehnic", "Acces la portal, starea aplicației și întrebări tehnice."), ("Contact general", "Solicitări generale despre TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Aplicația Partner Portal", "title": "Obțineți aplicația TVK Partner Portal", "subtitle": "Instalați portalul de parteneriat pe telefon — aplicați, urmăriți inițiativele și accesați documentele de competențe dintr-o pictogramă pe ecranul principal. Funcționează astăzi prin Adaugă pe ecranul principal; listare în App Store planificată pentru faza 2.", "openApp": "Deschide Partner Portal", "howToInstall": "Cum se instalează", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Deschide Partner Portal → Partajare → Adaugă pe ecranul principal"}, "android": {"title": "Android", "steps": "Chrome → Deschide Partner Portal → meniu → Instalează aplicația sau Adaugă pe ecranul principal"}, "desktop": {"title": "Desktop", "steps": "Chrome sau Edge → pictograma de instalare în bara de adrese sau salvați Partner Portal la favorite"}},
    },
)

LOCALE_BUNDLES["hu"] = bundle(
    "Partner Portal", "Alkalmazás letöltése", "Partner Portal alkalmazás →",
    {
        "meta": {"title": "Partner Portal", "description": "A TVK Infrastructure & Energy Systems partnerportálja — jelentkezzen stratégiai partnerségekre, kövesse a fejlesztési kezdeményezéseket és férjen hozzá a kompetencia-dokumentumokhoz."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Weboldal",
        "navAria": "Partnerportál navigáció",
        "nav": {"dashboard": "Irányítópult", "apply": "Jelentkezés", "projects": "Projektek", "documents": "Dokumentumok", "support": "Támogatás"},
        "dashboard": {
            "title": "Partner irányítópult",
            "subtitle": "Kövesse partnerségi megkeresését, fejlesztési kezdeményezéseit és a következő lépéseket a TVK Ecosystem-en belül.",
            "stats": [{"label": "Partnerségi szakasz", "value": "Fejlesztés"}, {"label": "Aktív kezdeményezések", "value": "6 terület"}, {"label": "Megkeresés állapota", "value": "Nyitott"}, {"label": "Portál nyelvei", "value": "25"}],
            "partnershipStatus": {"title": "Stratégiai partnerségi folyamat", "badge": "Fejlesztés alatt", "description": "A TVK Infrastructure & Energy Systems kutatási, fejlesztési és partnerségépítési szakaszban van. Küldjön be jelentkezést a strukturált együttműködési beszélgetés megkezdéséhez."},
            "nextSteps": {"title": "Ajánlott következő lépések", "items": ["Küldjön be stratégiai partnerségi jelentkezést szervezete adataival", "Tekintse át az energiarendszerek és infrastruktúra-technológiák kompetencia-területeit", "Fedezze fel az aktív fejlesztési kezdeményezéseket a projektek szekcióban", "Lépjen kapcsolatba partnerségi csapatunkkal pilot vagy együttműködési lehetőségekért"]},
            "cta": "Partnerségi jelentkezés beküldése →",
        },
        "apply": {"title": "Partnerségi jelentkezés", "subtitle": "Jelentkezzen stratégiai együttműködésre a TVK Infrastructure & Energy Systems-szel.", "intro": "Töltse ki ezt az űrlapot szervezete bemutatásához és partnerségi érdeklődése leírásához. Csapatunk minden jelentkezést elbírál és válaszol a minősített megkeresésekre.", "disclaimer": "Ez a jelentkezés nem minősül kötelező érvényű megállapodásnak. A TVK Infrastructure & Energy Systems LTD fejlesztési szakaszban van — az információk kompetencia-területeket írnak le, nem operatív kötelezettségeket."},
        "applyForm": {
            "interestAreas": ["Energiarendszerek", "Infrastruktúra-technológiák", "Ipari megoldások", "Energy Intelligence", "MI-infrastruktúra", "Stratégiai partnerségek", "Általános megkeresés"],
            "success": {"title": "Jelentkezés beérkezett", "message": "Köszönjük partnerségi érdeklődését. Csapatunk elbírálja jelentkezését és 5–10 munkanapon belül válaszol."},
            "fields": {"name": "Teljes név", "company": "Szervezet", "role": "Szerepkör / Beosztás", "country": "Ország", "email": "E-mail", "interest": "Partnerségi terület", "allocation": "Tájékoztató jellegű terjedelem (USD vagy leírás)", "message": "Partnerségi javaslat", "required": "*"},
            "placeholders": {"name": "Teljes neve", "company": "Szervezet neve", "role": "Beosztása", "country": "Működési ország", "email": "professional@company.com", "interest": "Válasszon területet", "allocation": "pl. Pilot projekt, 500 ezer USD együttműködés, technológiai integráció", "message": "Írja le szervezetét, stratégiai illeszkedését és javasolt együttműködését..."},
            "submit": "Partnerségi jelentkezés beküldése",
        },
        "projects": {"title": "Fejlesztési kezdeményezések", "subtitle": "Jelenlegi kompetencia-területek és fejlesztési szakaszban lévő kezdeményezések a TVK Ecosystem-en belül.", "items": make_projects([("Energiarendszerek integrációja", "Fejlesztés alatt", "Megújuló integráció, ipari energia-megoldások és intelligens energiamenedzsment-keretrendszerek."), ("Okos infrastruktúra-technológiák", "Kutatás", "Digitális infrastruktúra-rendszerek, monitorozó platformok és kritikus infrastruktúra-technológia fejlesztése."), ("Ipari MI és analitika", "Aktív kutatás", "Ipari MI, infrastruktúra-analitika és intelligens automatizálási kutatás összetett operatív környezetekhez.")])},
        "documents": {"title": "Kompetencia-dokumentumok", "subtitle": "Hivatalos kompetencia-összefoglalók és referenciaanyagok a vállalati weboldalról.", "openLabel": "Dokumentum megnyitása", "items": make_docs([("Energiarendszerek kompetenciái", "Az energiarendszerek fejlesztésének, a megújulók integrációjának és az Energy Intelligence áttekintése."), ("Infrastruktúra-technológiák", "Okos infrastruktúra, digitális rendszerek és kritikus infrastruktúra-technológia fejlesztése."), ("Stratégiai partnerségek", "Partnerségi modellek, együttműködési keretrendszerek és részvételi folyamat."), ("Betekintések és kutatás", "Iparági perspektívák az energiáról, infrastruktúráról és ipari technológiáról.")])},
        "support": {"title": "Partner támogatás", "subtitle": "Lépjen kapcsolatba a TVK Infrastructure & Energy Systems csapatával partnerségi, technikai és általános megkeresések esetén.", "disclaimer": "Sürgős operatív ügyekben forduljon a kijelölt partnerségi képviselőjéhez. Válaszidő: 1–2 munkanap általános megkeresések esetén.", "channels": make_channels([("Partnerségi megkeresések", "Stratégiai együttműködés, pilot lehetőségek és hosszú távú partnerségfejlesztés."), ("Befektetői kapcsolatok", "Tőkeformálás és stratégiai befektetési megbeszélések a TVK Ecosystem-en belül."), ("Technikai támogatás", "Portál-hozzáférés, jelentkezés állapota és technikai kérdések."), ("Általános kapcsolat", "Általános megkeresések a TVK Infrastructure & Energy Systems-szel kapcsolatban.")])},
        "install": {"eyebrow": "Partner Portal alkalmazás", "title": "Szerezze be a TVK Partner Portal alkalmazást", "subtitle": "Telepítse a partnerségi portált telefonjára — jelentkezzen, kövesse a kezdeményezéseket és érjen el kompetencia-dokumentumokat a kezdőképernyő ikonjáról. Ma már működik a Főképernyőhöz adás funkcióval; App Store-listázás a 2. fázisban tervezett.", "openApp": "Partner Portal megnyitása", "howToInstall": "Telepítés módja", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Partner Portal megnyitása → Megosztás → Főképernyőhöz adás"}, "android": {"title": "Android", "steps": "Chrome → Partner Portal megnyitása → menü → Alkalmazás telepítése vagy Hozzáadás a kezdőképernyőhöz"}, "desktop": {"title": "Asztali", "steps": "Chrome vagy Edge → telepítés ikon a címsorban, vagy mentse a Partner Portal-t a könyvjelzők közé"}},
    },
)

LOCALE_BUNDLES["el"] = bundle(
    "Partner Portal", "Λήψη εφαρμογής", "Εφαρμογή Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Πύλη συνεργατών TVK Infrastructure & Energy Systems — υποβάλετε αίτηση για στρατηγικές συνεργασίες, παρακολουθήστε πρωτοβουλίες ανάπτυξης και αποκτήστε πρόσβαση σε έγγραφα ικανοτήτων."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Ιστότοπος",
        "navAria": "Πλοήγηση πύλης συνεργατών",
        "nav": {"dashboard": "Πίνακας ελέγχου", "apply": "Αίτηση", "projects": "Έργα", "documents": "Έγγραφα", "support": "Υποστήριξη"},
        "dashboard": {
            "title": "Πίνακας ελέγχου συνεργάτη",
            "subtitle": "Παρακολουθήστε το αίτημα συνεργασίας, τις πρωτοβουλίες ανάπτυξης και τα επόμενα βήματα εντός του TVK Ecosystem.",
            "stats": [{"label": "Στάδιο συνεργασίας", "value": "Ανάπτυξη"}, {"label": "Ενεργές πρωτοβουλίες", "value": "6 τομείς"}, {"label": "Κατάσταση αιτήματος", "value": "Ανοιχτό"}, {"label": "Γλώσσες πύλης", "value": "25"}],
            "partnershipStatus": {"title": "Αγωγός στρατηγικών συνεργασιών", "badge": "Σε ανάπτυξη", "description": "Η TVK Infrastructure & Energy Systems βρίσκεται σε στάδιο έρευνας, ανάπτυξης και δημιουργίας συνεργασιών. Υποβάλετε αίτηση για να ξεκινήσετε μια δομημένη συζήτηση συνεργασίας."},
            "nextSteps": {"title": "Προτεινόμενα επόμενα βήματα", "items": ["Υποβάλετε αίτηση στρατηγικής συνεργασίας με τα στοιχεία του οργανισμού σας", "Εξετάστε τους τομείς ικανοτήτων σε ενεργειακά συστήματα και τεχνολογίες υποδομών", "Εξερευνήστε ενεργές πρωτοβουλίες ανάπτυξης στην ενότητα έργων", "Επικοινωνήστε με την ομάδα συνεργασιών μας για ευκαιρίες πιλοτικών ή συνεργασίας"]},
            "cta": "Υποβολή αίτησης συνεργασίας →",
        },
        "apply": {"title": "Αίτηση συνεργασίας", "subtitle": "Υποβάλετε αίτηση για στρατηγική συνεργασία με την TVK Infrastructure & Energy Systems.", "intro": "Συμπληρώστε αυτή τη φόρμα για να παρουσιάσετε τον οργανισμό σας και να περιγράψετε το ενδιαφέρον σας για συνεργασία. Η ομάδα μας εξετάζει όλες τις αιτήσεις και απαντά σε αξιολογημένα αιτήματα.", "disclaimer": "Αυτή η αίτηση δεν αποτελεί δεσμευτική συμφωνία. Η TVK Infrastructure & Energy Systems LTD βρίσκεται σε στάδιο ανάπτυξης — οι πληροφορίες περιγράφουν τομείς ικανοτήτων, όχι λειτουργικές δεσμεύσεις."},
        "applyForm": {
            "interestAreas": ["Ενεργειακά συστήματα", "Τεχνολογίες υποδομών", "Βιομηχανικές λύσεις", "Energy Intelligence", "Υποδομή AI", "Στρατηγικές συνεργασίες", "Γενικό αίτημα"],
            "success": {"title": "Η αίτηση ελήφθη", "message": "Σας ευχαριστούμε για το ενδιαφέρον σας για συνεργασία. Η ομάδα μας θα εξετάσει την αίτησή σας και θα απαντήσει εντός 5–10 εργάσιμων ημερών."},
            "fields": {"name": "Πλήρες όνομα", "company": "Οργανισμός", "role": "Ρόλος / Τίτλος", "country": "Χώρα", "email": "E-mail", "interest": "Τομέας συνεργασίας", "allocation": "Ενδεικτικό εύρος (USD ή περιγραφή)", "message": "Πρόταση συνεργασίας", "required": "*"},
            "placeholders": {"name": "Το πλήρες όνομά σας", "company": "Όνομα οργανισμού", "role": "Η θέση σας", "country": "Χώρα λειτουργίας", "email": "professional@company.com", "interest": "Επιλέξτε τομέα", "allocation": "π.χ. Πιλοτικό έργο, συνεργασία 500 χιλ. USD, ενσωμάτωση τεχνολογίας", "message": "Περιγράψτε τον οργανισμό σας, τη στρατηγική συμβατότητα και την προτεινόμενη συνεργασία..."},
            "submit": "Υποβολή αίτησης συνεργασίας",
        },
        "projects": {"title": "Πρωτοβουλίες ανάπτυξης", "subtitle": "Τρέχοντες τομείς ικανοτήτων και πρωτοβουλίες σε στάδιο ανάπτυξης εντός του TVK Ecosystem.", "items": make_projects([("Ενσωμάτωση ενεργειακών συστημάτων", "Σε ανάπτυξη", "Ενσωμάτωση ΑΠΕ, βιομηχανικές ενεργειακές λύσεις και έξυπνα πλαίσια διαχείρισης ενέργειας."), ("Τεχνολογίες έξυπνης υποδομής", "Έρευνα", "Ψηφιακά συστήματα υποδομών, πλατφόρμες παρακολούθησης και ανάπτυξη τεχνολογιών κρίσιμης υποδομής."), ("Βιομηχανική AI και αναλυτική", "Ενεργή έρευνα", "Βιομηχανική AI, αναλυτική υποδομών και έρευνα έξυπνης αυτοματοποίησης για σύνθετα λειτουργικά περιβάλλοντα.")])},
        "documents": {"title": "Έγγραφα ικανοτήτων", "subtitle": "Επίσημα ενημερωτικά ικανοτήτων και υλικό αναφοράς από τον εταιρικό ιστότοπο.", "openLabel": "Άνοιγμα εγγράφου", "items": make_docs([("Ικανότητες ενεργειακών συστημάτων", "Επισκόπηση ανάπτυξης ενεργειακών συστημάτων, ενσωμάτωσης ΑΠΕ και Energy Intelligence."), ("Τεχνολογίες υποδομών", "Έξυπνη υποδομή, ψηφιακά συστήματα και ανάπτυξη τεχνολογιών κρίσιμης υποδομής."), ("Στρατηγικές συνεργασίες", "Μοντέλα συνεργασίας, πλαίσια συνεργασίας και διαδικασία εμπλοκής."), ("Αναλύσεις και έρευνα", "Επιχειρησιακές προοπτικές για ενέργεια, υποδομές και βιομηχανική τεχνολογία.")])},
        "support": {"title": "Υποστήριξη συνεργατών", "subtitle": "Επικοινωνήστε με την ομάδα TVK Infrastructure & Energy Systems για αιτήματα συνεργασίας, τεχνικά και γενικά.", "disclaimer": "Για επείγοντα λειτουργικά θέματα, επικοινωνήστε με τον ανατεθειμένο εκπρόσωπο συνεργασίας. Χρόνοι απόκρισης: 1–2 εργάσιμες ημέρες για γενικά αιτήματα.", "channels": make_channels([("Αιτήματα συνεργασίας", "Στρατηγική συνεργασία, ευκαιρίες πιλοτικών και μακροπρόθεσμη ανάπτυξη συνεργασιών."), ("Σχέσεις με επενδυτές", "Δημιουργία κεφαλαίου και στρατηγικές συζητήσεις επένδυσης εντός του TVK Ecosystem."), ("Τεχνική υποστήριξη", "Πρόσβαση στην πύλη, κατάσταση αίτησης και τεχνικά ερωτήματα."), ("Γενική επικοινωνία", "Γενικά αιτήματα σχετικά με την TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Εφαρμογή Partner Portal", "title": "Αποκτήστε την εφαρμογή TVK Partner Portal", "subtitle": "Εγκαταστήστε την πύλη συνεργατών στο τηλέφωνό σας — υποβάλετε αίτηση, παρακολουθήστε πρωτοβουλίες και αποκτήστε πρόσβαση σε έγγραφα ικανοτήτων από εικονίδιο αρχικής οθόνης. Λειτουργεί σήμερα μέσω Προσθήκη στην αρχική οθόνη· καταχώριση στο App Store προγραμματισμένη για τη φάση 2.", "openApp": "Άνοιγμα Partner Portal", "howToInstall": "Πώς να εγκαταστήσετε", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Άνοιγμα Partner Portal → Κοινοποίηση → Προσθήκη στην αρχική οθόνη"}, "android": {"title": "Android", "steps": "Chrome → Άνοιγμα Partner Portal → μενού → Εγκατάσταση εφαρμογής ή Προσθήκη στην αρχική οθόνη"}, "desktop": {"title": "Επιτραπέζιος", "steps": "Chrome ή Edge → εικονίδιο εγκατάστασης στη γραμμή διευθύνσεων ή αποθηκεύστε το Partner Portal στους σελιδοδείκτες"}},
    },
)

LOCALE_BUNDLES["id"] = bundle(
    "Partner Portal", "Dapatkan aplikasi", "Aplikasi Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Portal mitra TVK Infrastructure & Energy Systems — ajukan kemitraan strategis, lacak inisiatif pengembangan, dan akses dokumen kapabilitas."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Situs web",
        "navAria": "Navigasi portal mitra",
        "nav": {"dashboard": "Dasbor", "apply": "Ajukan", "projects": "Proyek", "documents": "Dokumen", "support": "Dukungan"},
        "dashboard": {
            "title": "Dasbor Mitra",
            "subtitle": "Lacak permintaan kemitraan, inisiatif pengembangan, dan langkah selanjutnya dalam TVK Ecosystem.",
            "stats": [{"label": "Tahap Kemitraan", "value": "Pengembangan"}, {"label": "Inisiatif Aktif", "value": "6 Bidang"}, {"label": "Status Permintaan", "value": "Terbuka"}, {"label": "Bahasa Portal", "value": "25"}],
            "partnershipStatus": {"title": "Pipeline Kemitraan Strategis", "badge": "Dalam Pengembangan", "description": "TVK Infrastructure & Energy Systems berada dalam tahap penelitian, pengembangan, dan pembangunan kemitraan. Kirim aplikasi untuk memulai percakapan kolaborasi terstruktur."},
            "nextSteps": {"title": "Langkah Selanjutnya yang Direkomendasikan", "items": ["Kirim aplikasi kemitraan strategis dengan detail organisasi Anda", "Tinjau bidang kapabilitas di sistem energi dan teknologi infrastruktur", "Jelajahi inisiatif pengembangan aktif di bagian proyek", "Hubungi tim kemitraan kami untuk peluang pilot atau kolaborasi"]},
            "cta": "Kirim Aplikasi Kemitraan →",
        },
        "apply": {"title": "Aplikasi Kemitraan", "subtitle": "Ajukan kolaborasi strategis dengan TVK Infrastructure & Energy Systems.", "intro": "Lengkapi formulir ini untuk memperkenalkan organisasi Anda dan menjelaskan minat kemitraan. Tim kami meninjau semua aplikasi dan merespons permintaan yang memenuhi syarat.", "disclaimer": "Aplikasi ini bukan perjanjian yang mengikat. TVK Infrastructure & Energy Systems LTD berada dalam tahap pengembangan — informasi menjelaskan bidang kapabilitas, bukan komitmen operasional."},
        "applyForm": {
            "interestAreas": ["Sistem Energi", "Teknologi Infrastruktur", "Solusi Industri", "Energy Intelligence", "Infrastruktur AI", "Kemitraan Strategis", "Permintaan Umum"],
            "success": {"title": "Aplikasi Diterima", "message": "Terima kasih atas minat kemitraan Anda. Tim kami akan meninjau aplikasi Anda dan merespons dalam 5–10 hari kerja."},
            "fields": {"name": "Nama Lengkap", "company": "Organisasi", "role": "Peran / Jabatan", "country": "Negara", "email": "Email", "interest": "Bidang Kemitraan", "allocation": "Cakupan Indikatif (USD atau deskripsi)", "message": "Proposal Kemitraan", "required": "*"},
            "placeholders": {"name": "Nama lengkap Anda", "company": "Nama organisasi", "role": "Posisi Anda", "country": "Negara operasi", "email": "professional@company.com", "interest": "Pilih bidang", "allocation": "mis. Proyek pilot, kolaborasi $500K, integrasi teknologi", "message": "Jelaskan organisasi, kesesuaian strategis, dan kolaborasi yang diusulkan..."},
            "submit": "Kirim Aplikasi Kemitraan",
        },
        "projects": {"title": "Inisiatif Pengembangan", "subtitle": "Bidang kapabilitas saat ini dan inisiatif tahap pengembangan dalam TVK Ecosystem.", "items": make_projects([("Integrasi Sistem Energi", "Dalam Pengembangan", "Integrasi energi terbarukan, solusi energi industri, dan kerangka manajemen energi cerdas."), ("Teknologi Infrastruktur Cerdas", "Penelitian", "Sistem infrastruktur digital, platform pemantauan, dan pengembangan teknologi infrastruktur kritis."), ("AI Industri & Analitik", "Penelitian Aktif", "AI industri, analitik infrastruktur, dan penelitian otomasi cerdas untuk lingkungan operasional kompleks.")])},
        "documents": {"title": "Dokumen Kapabilitas", "subtitle": "Ringkasan kapabilitas resmi dan materi referensi dari situs korporat.", "openLabel": "Buka dokumen", "items": make_docs([("Kapabilitas Sistem Energi", "Ikhtisar pengembangan sistem energi, integrasi energi terbarukan, dan Energy Intelligence."), ("Teknologi Infrastruktur", "Infrastruktur cerdas, sistem digital, dan pengembangan teknologi infrastruktur kritis."), ("Kemitraan Strategis", "Model kemitraan, kerangka kolaborasi, dan proses keterlibatan."), ("Wawasan & Penelitian", "Perspektif industri tentang energi, infrastruktur, dan teknologi industri.")])},
        "support": {"title": "Dukungan Mitra", "subtitle": "Hubungi tim TVK Infrastructure & Energy Systems untuk pertanyaan kemitraan, teknis, dan umum.", "disclaimer": "Untuk urusan operasional mendesak, hubungi perwakilan kemitraan yang ditugaskan. Waktu respons: 1–2 hari kerja untuk pertanyaan umum.", "channels": make_channels([("Pertanyaan Kemitraan", "Kolaborasi strategis, peluang pilot, dan pengembangan kemitraan jangka panjang."), ("Hubungan Investor", "Pembentukan modal dan diskusi investasi strategis dalam TVK Ecosystem."), ("Dukungan Teknis", "Akses portal, status aplikasi, dan pertanyaan teknis."), ("Kontak Umum", "Pertanyaan umum tentang TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Aplikasi Partner Portal", "title": "Dapatkan aplikasi TVK Partner Portal", "subtitle": "Instal portal kemitraan di ponsel Anda — ajukan, lacak inisiatif, dan akses dokumen kapabilitas dari ikon layar utama. Berfungsi hari ini melalui Tambahkan ke Layar Utama; listing App Store direncanakan untuk Fase 2.", "openApp": "Buka Partner Portal", "howToInstall": "Cara menginstal", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Buka Partner Portal → Bagikan → Tambahkan ke Layar Utama"}, "android": {"title": "Android", "steps": "Chrome → Buka Partner Portal → menu → Instal aplikasi atau Tambahkan ke layar utama"}, "desktop": {"title": "Desktop", "steps": "Chrome atau Edge → ikon instal di bilah alamat, atau tandai Partner Portal"}},
    },
)

LOCALE_BUNDLES["vi"] = bundle(
    "Partner Portal", "Tải ứng dụng", "Ứng dụng Partner Portal →",
    {
        "meta": {"title": "Partner Portal", "description": "Cổng đối tác TVK Infrastructure & Energy Systems — đăng ký quan hệ đối tác chiến lược, theo dõi các sáng kiến phát triển và truy cập tài liệu năng lực."},
        "brand": "TVK Partner Portal", "tagline": "Infrastructure & Energy Systems", "backToSite": "Trang web",
        "navAria": "Điều hướng cổng đối tác",
        "nav": {"dashboard": "Bảng điều khiển", "apply": "Đăng ký", "projects": "Dự án", "documents": "Tài liệu", "support": "Hỗ trợ"},
        "dashboard": {
            "title": "Bảng điều khiển đối tác",
            "subtitle": "Theo dõi yêu cầu quan hệ đối tác, các sáng kiến phát triển và các bước tiếp theo trong TVK Ecosystem.",
            "stats": [{"label": "Giai đoạn đối tác", "value": "Phát triển"}, {"label": "Sáng kiến đang hoạt động", "value": "6 lĩnh vực"}, {"label": "Trạng thái yêu cầu", "value": "Mở"}, {"label": "Ngôn ngữ cổng", "value": "25"}],
            "partnershipStatus": {"title": "Quy trình quan hệ đối tác chiến lược", "badge": "Đang phát triển", "description": "TVK Infrastructure & Energy Systems đang ở giai đoạn nghiên cứu, phát triển và xây dựng quan hệ đối tác. Gửi đơn đăng ký để bắt đầu cuộc trao đổi hợp tác có cấu trúc."},
            "nextSteps": {"title": "Các bước tiếp theo được đề xuất", "items": ["Gửi đơn đăng ký quan hệ đối tác chiến lược với thông tin tổ chức của bạn", "Xem xét các lĩnh vực năng lực về hệ thống năng lượng và công nghệ hạ tầng", "Khám phá các sáng kiến phát triển đang hoạt động trong phần dự án", "Liên hệ nhóm quan hệ đối tác của chúng tôi để biết cơ hội thí điểm hoặc hợp tác"]},
            "cta": "Gửi đơn đăng ký quan hệ đối tác →",
        },
        "apply": {"title": "Đơn đăng ký quan hệ đối tác", "subtitle": "Đăng ký hợp tác chiến lược với TVK Infrastructure & Energy Systems.", "intro": "Hoàn thành biểu mẫu này để giới thiệu tổ chức của bạn và mô tả mối quan tâm về quan hệ đối tác. Nhóm của chúng tôi xem xét tất cả đơn đăng ký và phản hồi các yêu cầu đủ điều kiện.", "disclaimer": "Đơn đăng ký này không cấu thành thỏa thuận ràng buộc. TVK Infrastructure & Energy Systems LTD đang ở giai đoạn phát triển — thông tin mô tả các lĩnh vực năng lực, không phải cam kết vận hành."},
        "applyForm": {
            "interestAreas": ["Hệ thống năng lượng", "Công nghệ hạ tầng", "Giải pháp công nghiệp", "Energy Intelligence", "Hạ tầng AI", "Quan hệ đối tác chiến lược", "Yêu cầu chung"],
            "success": {"title": "Đã nhận đơn đăng ký", "message": "Cảm ơn bạn quan tâm đến quan hệ đối tác. Nhóm của chúng tôi sẽ xem xét đơn đăng ký và phản hồi trong 5–10 ngày làm việc."},
            "fields": {"name": "Họ và tên", "company": "Tổ chức", "role": "Vai trò / Chức danh", "country": "Quốc gia", "email": "Email", "interest": "Lĩnh vực đối tác", "allocation": "Phạm vi tham khảo (USD hoặc mô tả)", "message": "Đề xuất quan hệ đối tác", "required": "*"},
            "placeholders": {"name": "Họ và tên của bạn", "company": "Tên tổ chức", "role": "Chức vụ của bạn", "country": "Quốc gia hoạt động", "email": "professional@company.com", "interest": "Chọn lĩnh vực", "allocation": "vd. Dự án thí điểm, hợp tác 500 nghìn USD, tích hợp công nghệ", "message": "Mô tả tổ chức, sự phù hợp chiến lược và hợp tác đề xuất..."},
            "submit": "Gửi đơn đăng ký quan hệ đối tác",
        },
        "projects": {"title": "Sáng kiến phát triển", "subtitle": "Các lĩnh vực năng lực hiện tại và sáng kiến ở giai đoạn phát triển trong TVK Ecosystem.", "items": make_projects([("Tích hợp hệ thống năng lượng", "Đang phát triển", "Tích hợp năng lượng tái tạo, giải pháp năng lượng công nghiệp và khung quản lý năng lượng thông minh."), ("Công nghệ hạ tầng thông minh", "Nghiên cứu", "Hệ thống hạ tầng số, nền tảng giám sát và phát triển công nghệ hạ tầng quan trọng."), ("AI công nghiệp & phân tích", "Nghiên cứu đang hoạt động", "AI công nghiệp, phân tích hạ tầng và nghiên cứu tự động hóa thông minh cho môi trường vận hành phức tạp.")])},
        "documents": {"title": "Tài liệu năng lực", "subtitle": "Tóm tắt năng lực chính thức và tài liệu tham khảo từ trang web doanh nghiệp.", "openLabel": "Mở tài liệu", "items": make_docs([("Năng lực hệ thống năng lượng", "Tổng quan về phát triển hệ thống năng lượng, tích hợp năng lượng tái tạo và Energy Intelligence."), ("Công nghệ hạ tầng", "Hạ tầng thông minh, hệ thống số và phát triển công nghệ hạ tầng quan trọng."), ("Quan hệ đối tác chiến lược", "Mô hình đối tác, khung hợp tác và quy trình tham gia."), ("Thông tin chi tiết & nghiên cứu", "Góc nhìn ngành về năng lượng, hạ tầng và công nghệ công nghiệp.")])},
        "support": {"title": "Hỗ trợ đối tác", "subtitle": "Liên hệ nhóm TVK Infrastructure & Energy Systems để được hỗ trợ về quan hệ đối tác, kỹ thuật và các yêu cầu chung.", "disclaimer": "Đối với các vấn đề vận hành khẩn cấp, hãy liên hệ đại diện quan hệ đối tác được chỉ định. Thời gian phản hồi: 1–2 ngày làm việc cho yêu cầu chung.", "channels": make_channels([("Yêu cầu quan hệ đối tác", "Hợp tác chiến lược, cơ hội thí điểm và phát triển quan hệ đối tác dài hạn."), ("Quan hệ nhà đầu tư", "Hình thành vốn và thảo luận đầu tư chiến lược trong TVK Ecosystem."), ("Hỗ trợ kỹ thuật", "Truy cập cổng, trạng thái đơn đăng ký và câu hỏi kỹ thuật."), ("Liên hệ chung", "Yêu cầu chung về TVK Infrastructure & Energy Systems.")])},
        "install": {"eyebrow": "Ứng dụng Partner Portal", "title": "Tải ứng dụng TVK Partner Portal", "subtitle": "Cài đặt cổng quan hệ đối tác trên điện thoại — đăng ký, theo dõi sáng kiến và truy cập tài liệu năng lực từ biểu tượng màn hình chính. Hoạt động ngay hôm nay qua Thêm vào Màn hình chính; đăng ký App Store dự kiến cho Giai đoạn 2.", "openApp": "Mở Partner Portal", "howToInstall": "Cách cài đặt", "iphone": {"title": "iPhone / iPad", "steps": "Safari → Mở Partner Portal → Chia sẻ → Thêm vào Màn hình chính"}, "android": {"title": "Android", "steps": "Chrome → Mở Partner Portal → menu → Cài đặt ứng dụng hoặc Thêm vào màn hình chính"}, "desktop": {"title": "Máy tính", "steps": "Chrome hoặc Edge → biểu tượng cài đặt trên thanh địa chỉ, hoặc đánh dấu Partner Portal"}},
    },
)
