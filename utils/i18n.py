from __future__ import annotations
from typing import Any, Dict

locales: Dict[str, Dict[str, str]] = {
    "ru": {
        "pet_info_message": (
            "Это страничка питомца: {pet_name}. Возраст питомца: {age} лет.\n\n"
            "Если вы читаете мою страницу, значит я потерялся. Я очень хочу домой, к своему хозяину. "
            "Он очень любит меня и скучает.\n"
            "Пожалуйста, свяжитесь с ним по кнопке ниже и помогите мне вернуться домой."
        ),
        "contact_owner": "Связаться с владельцем",
        "owner_alerted": "Владелец оповещён, сейчас он отреагирует.",
        "contact_action": "Связаться",
        "owner_found_pet": "Здравствуйте! Я нашёл вашего питомца, свяжитесь со мной, и я с радостью его вам верну.",
        "location_instruction": "Запросите локацию собеседника, чтобы встретиться.",
        "request_pet_location": "Узнать локацию питомца",
        "location_requested": "Здравствуйте! Отправьте пожалуйста локацию, где Вы находитесь, чтобы мы могли встретиться.",
        "location_requested_from_owner": "Локация запрошена, ожидайте ответа.",
        "share_location": "Поделиться локацией",
        "live_location_howto": (
            "Отправьте, пожалуйста, трансляцию вашей live-локации боту.\n\n"
            "📎 → «Геопозиция» → «Трансляция геопозиции в реальном времени» → "
            "выбор времени → отправить."
        ),
        "request_location": "Пожалуйста, сообщите мне, где вы находитесь с помощью отправки вашей локации.",
        "location_shared_response": "Локация отправлена, ожидайте ответа. Не отходите далеко до встречи с собеседником. Когда вы окажитесь рядом, получите оповещение.",
        "finder_live_received": "Бот получил локацию от Вашего собеседника. Пожалуйста, отправьте так же свою трансляцию локации, для того, чтоб получать звуковые уведомления о приближении к месту встречи.",
        "alert_error_location": "Похоже, трансляция локации остановилась. Пожалуйста, отправьте live-локацию ещё раз.",
        "navigation_hint_owner": (
            "Перейдите в режим навигации, вы сможете оценить время в пути, "
            "после чего сообщите время прибытия нашедшему питомца."
        ),
        "navigation_hint_user": "Сообщите, когда вы прибудете, или пригласите собеседника в чат, если нужно обсудить иные варианты",
        "arrive_10": "Прибуду в течение 10 минут",
        "arrive_20": "Прибуду в течение 20 минут",
        "arrive_30": "Прибуду в течение 30 минут",
        "arrive_60": "Прибуду в течение одного часа",
        "start_chat": "Начать чат",
        "arrival_owner_10": "Прибуду в течение 10 минут, пожалуйста, дождитесь меня в точке вашей локации.",
        "arrival_owner_20": "Прибуду в течение 20 минут, пожалуйста, дождитесь меня в точке вашей локации.",
        "arrival_owner_30": "Прибуду в течение 30 минут, пожалуйста, дождитесь меня в точке вашей локации.",
        "arrival_owner_60": "Прибуду в течение одного часа, пожалуйста, дождитесь меня в точке вашей локации.",
        "arrival_timer_warning": (
            "Вы должны прибыть к указанной точке в течение {select_time}. "
            "Если опаздываете или планы изменились, сообщите актуальное время прибытия через это меню."
        ),
        "back": "Назад",
        "language_warning": "Внимание! Язык общения собеседника может отличаться от вашего",
        "accept_chat": "Принимаю",
        "invite_text": "Перейдите по ссылке {invite_link}, чтобы продолжить общение в группе {group_name}.",
        "owner_chat_offer": (
            "Владелец питомца предлагает вам перейти в чат для обсуждения иных вариантов встречи.\n"
            "Кнопка ниже перебросит вас в чат с владельцем питомца."
        ),
        "open_chat": "Открыть чат",
        "chat_partner_joined_owner": "Собеседник успешно присоединился к чату. Перейдите также в чат для обсуждения деталей.",
        "proximity_notification": "Вы находитесь рядом, включите звуковой пароль, оглянитесь по сторонам и вы встретитесь!",
        "sound_password": "Звуковой пароль",
        "playing_sound_password": "Воспроизводится звуковой пароль (30 секунд)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Миссия выполнена!",
        "check_owner_location": "Проверить локацию владельца",
        "check_finder_location": "Проверить локацию нашедшего",
        "owner_location_unavailable": "Извините, текущая локация владельца пока недоступна.",
        "finder_location_unavailable": "Извините, текущая локация нашедшего пока недоступна.",
    },
    "en": {
        "pet_info_message": (
            "This is the pet's page: {pet_name}. Age: {age} years.\n\n"
            "If you're reading this, I'm lost. I really want to go home to my owner. "
            "They love me very much and are missing me.\n"
            "Please contact them using the button below and help me get back home."
        ),
        "contact_owner": "Contact Owner",
        "owner_alerted": "Owner has been notified and will respond shortly.",
        "contact_action": "Contact",
        "owner_found_pet": "Hello! I found your pet. Please contact me and I'll be happy to return them to you.",
        "location_instruction": "Request the other person's location to arrange a meeting.",
        "request_pet_location": "Get Pet Location",
        "location_requested": "Hello! Please share your location so we can meet up.",
        "location_requested_from_owner": "Location requested. Waiting for response.",
        "share_location": "Share Location",
        "live_location_howto": (
            "Please share your live location with the bot.\n\n"
            "📎 → «Location» → «Share Live Location» → "
            "select duration → send."
        ),
        "request_location": "Please let me know where you are by sharing your location.",
        "location_shared_response": "Location shared. Please wait for response. Stay nearby until meeting. You'll get a notification when close.",
        "finder_live_received": "Bot received location from your contact. Please also share your live location to get audio notifications when approaching meeting point.",
        "alert_error_location": "Live location seems to have stopped. Please share live location again.",
        "navigation_hint_owner": (
            "Switch to navigation mode to estimate travel time, "
            "then inform the finder of your arrival time."
        ),
        "navigation_hint_user": "Notify when you arrive or invite to chat if other arrangements needed",
        "arrive_10": "Arrive in 10 minutes",
        "arrive_20": "Arrive in 20 minutes",
        "arrive_30": "Arrive in 30 minutes",
        "arrive_60": "Arrive in one hour",
        "start_chat": "Start Chat",
        "arrival_owner_10": "I'll arrive within 10 minutes, please wait at your location.",
        "arrival_owner_20": "I'll arrive within 20 minutes, please wait at your location.",
        "arrival_owner_30": "I'll arrive within 30 minutes, please wait at your location.",
        "arrival_owner_60": "I'll arrive within one hour, please wait at your location.",
        "arrival_timer_warning": (
            "You should arrive at the specified point within {select_time}. "
            "If delayed or plans changed, update your arrival time through this menu."
        ),
        "back": "Back",
        "language_warning": "Warning! Your conversation partner may speak a different language",
        "accept_chat": "Accept",
        "invite_text": "Follow {invite_link} to continue communication in {group_name} group.",
        "owner_chat_offer": (
            "The pet owner invites you to a chat to discuss alternative meeting options.\n"
            "The button below will take you to chat with the pet owner."
        ),
        "open_chat": "Open Chat",
        "chat_partner_joined_owner": "Partner joined chat successfully. Please join the chat to discuss details.",
        "proximity_notification": "You're nearby! Enable sound password, look around and you'll meet!",
        "sound_password": "Sound Password",
        "playing_sound_password": "Playing sound password (30 seconds)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Mission accomplished!",
        "check_owner_location": "Check owner's location",
        "check_finder_location": "Check finder's location",
        "owner_location_unavailable": "Sorry, owner's current location is temporarily unavailable.",
        "finder_location_unavailable": "Sorry, finder's current location is temporarily unavailable.",
    },
    "es": {
        "pet_info_message": (
            "Esta es la página de la mascota: {pet_name}. Edad: {age} años.\n\n"
            "Si estás leyendo esto, estoy perdido. Realmente quiero volver a casa con mi dueño. "
            "Me quiere mucho y me echa de menos.\n"
            "Por favor, ponte en contacto con él mediante el botón de abajo y ayúdame a volver a casa."
        ),
        "contact_owner": "Contactar con el propietario",
        "owner_alerted": "El propietario ha sido notificado y responderá en breve.",
        "contact_action": "Contactar",
        "owner_found_pet": "¡Hola! Encontré a tu mascota. Por favor, contáctame y estaré encantado de devolvértela.",
        "location_instruction": "Solicita la ubicación de la otra persona para quedar.",
        "request_pet_location": "Obtener ubicación de la mascota",
        "location_requested": "¡Hola! Por favor, comparte tu ubicación para que podamos quedar.",
        "location_requested_from_owner": "Ubicación solicitada. Esperando respuesta.",
        "share_location": "Compartir ubicación",
        "live_location_howto": (
            "Por favor, comparte tu ubicación en vivo con el bot.\n\n"
            "📎 → «Ubicación» → «Compartir ubicación en vivo» → "
            "seleccionar duración → enviar."
        ),
        "request_location": "Por favor, hágame saber dónde se encuentra compartiendo su ubicación.",
        "location_shared_response": "Ubicación compartida. Por favor, espere respuesta. Permanezca cerca hasta la reunión. Recibirás una notificación cuando estés cerca.",
        "finder_live_received": "El bot recibió la ubicación de tu contacto. Por favor, comparte también tu ubicación en vivo para recibir notificaciones de audio al acercarte al punto de encuentro.",
        "alert_error_location": "Parece que la ubicación en vivo se ha detenido. Por favor, comparte tu ubicación en vivo nuevamente.",
        "navigation_hint_owner": (
            "Cambia al modo de navegación para estimar el tiempo de viaje, "
            "luego informa al finder de tu hora de llegada."
        ),
        "navigation_hint_user": "Notifica cuando llegues o invita a chatear si se necesitan otros arreglos",
        "arrive_10": "Llegaré en 10 minutos",
        "arrive_20": "Llegaré en 20 minutos",
        "arrive_30": "Llegaré en 30 minutos",
        "arrive_60": "Llegaré en una hora",
        "start_chat": "Iniciar chat",
        "arrival_owner_10": "Llegaré dentro de 10 minutos, por favor espera en tu ubicación.",
        "arrival_owner_20": "Llegaré dentro de 20 minutos, por favor espera en tu ubicación.",
        "arrival_owner_30": "Llegaré dentro de 30 minutos, por favor espera en tu ubicación.",
        "arrival_owner_60": "Llegaré dentro de una hora, por favor espera en tu ubicación.",
        "arrival_timer_warning": (
            "Debes llegar al punto especificado dentro de {select_time}. "
            "Si hay retrasos o cambios de planes, actualiza tu hora de llegada a través de este menú."
        ),
        "back": "Atrás",
        "language_warning": "¡Advertencia! Tu interlocutor puede hablar un idioma diferente",
        "accept_chat": "Aceptar",
        "invite_text": "Sigue {invite_link} para continuar la comunicación en el grupo {group_name}.",
        "owner_chat_offer": (
            "El dueño de la mascota te invita a un chat para discutir opciones alternativas de reunión.\n"
            "El botón siguiente te llevará a chatear con el dueño de la mascota."
        ),
        "open_chat": "Abrir chat",
        "chat_partner_joined_owner": "El interlocutor se unió al chat con éxito. Por favor, únete también al chat para discutir detalles.",
        "proximity_notification": "¡Estás cerca! Activa la contraseña de sonido, mira alrededor y ¡te encontrarás!",
        "sound_password": "Contraseña de sonido",
        "playing_sound_password": "Reproduciendo contraseña de sonido (30 segundos)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "¡Misión cumplida!",
        "check_owner_location": "Verificar ubicación del propietario",
        "check_finder_location": "Verificar ubicación del finder",
        "owner_location_unavailable": "Lo sentimos, la ubicación actual del propietario no está disponible temporalmente.",
        "finder_location_unavailable": "Lo sentimos, la ubicación actual del finder no está disponible temporalmente.",
    },
    "fr": {
        "pet_info_message": (
            "Ceci est la page de l'animal: {pet_name}. Âge: {age} ans.\n\n"
            "Si vous lisez ceci, je suis perdu. Je veux vraiment rentrer chez moi auprès de mon propriétaire. "
            "Il m'aime beaucoup et me manque.\n"
            "Veuillez le contacter en utilisant le bouton ci-dessous et aidez-moi à rentrer à la maison."
        ),
        "contact_owner": "Contacter le propriétaire",
        "owner_alerted": "Le propriétaire a été informé et répondra sous peu.",
        "contact_action": "Contacter",
        "owner_found_pet": "Bonjour! J'ai trouvé votre animal. Veuillez me contacter et je serai heureux de vous le rendre.",
        "location_instruction": "Demandez la localisation de l'autre personne pour organiser une rencontre.",
        "request_pet_location": "Obtenir la localisation de l'animal",
        "location_requested": "Bonjour! Veuillez partager votre localisation afin que nous puissions nous rencontrer.",
        "location_requested_from_owner": "Localisation demandée. En attente de réponse.",
        "share_location": "Partager la localisation",
        "live_location_howto": (
            "Veuillez partager votre localisation en direct avec le bot.\n\n"
            "📎 → «Localisation» → «Partager la localisation en direct» → "
            "sélectionner la durée → envoyer."
        ),
        "request_location": "Veuillez me faire savoir où vous êtes en partageant votre localisation.",
        "location_shared_response": "Localisation partagée. Veuillez patienter pour une réponse. Restez à proximité jusqu'à la rencontre. Vous recevrez une notification lorsque vous serez proche.",
        "finder_live_received": "Le bot a reçu la localisation de votre contact. Veuillez également partager votre localisation en direct pour recevoir des notifications audio lorsque vous approchez du point de rencontre.",
        "alert_error_location": "La localisation en direct semble s'être arrêtée. Veuillez partager à nouveau votre localisation en direct.",
        "navigation_hint_owner": (
            "Passez en mode navigation pour estimer le temps de trajet, "
            "puis informez le trouveur de votre heure d'arrivée."
        ),
        "navigation_hint_user": "Signalez quand vous arrivez ou invitez à discuter si d'autres arrangements sont nécessaires",
        "arrive_10": "J'arrive dans 10 minutes",
        "arrive_20": "J'arrive dans 20 minutes",
        "arrive_30": "J'arrive dans 30 minutes",
        "arrive_60": "J'arrive dans une heure",
        "start_chat": "Commencer le chat",
        "arrival_owner_10": "J'arriverai dans 10 minutes, veuillez m'attendre à votre emplacement.",
        "arrival_owner_20": "J'arriverai dans 20 minutes, veuillez m'attendre à votre emplacement.",
        "arrival_owner_30": "J'arriverai dans 30 minutes, veuillez m'attendre à votre emplacement.",
        "arrival_owner_60": "J'arriverai dans une heure, veuillez m'attendre à votre emplacement.",
        "arrival_timer_warning": (
            "Vous devez arriver au point spécifié dans {select_time}. "
            "Si vous êtes retardé ou si les plans changent, mettez à jour votre heure d'arrivée via ce menu."
        ),
        "back": "Retour",
        "language_warning": "Attention! Votre interlocuteur peut parler une langue différente",
        "accept_chat": "Accepter",
        "invite_text": "Suivez {invite_link} pour continuer la communication dans le groupe {group_name}.",
        "owner_chat_offer": (
            "Le propriétaire de l'animal vous invite à discuter pour envisager d'autres options de rencontre.\n"
            "Le bouton ci-dessous vous mènera à une conversation avec le propriétaire de l'animal."
        ),
        "open_chat": "Ouvrir le chat",
        "chat_partner_joined_owner": "L'interlocuteur a rejoint le chat avec succès. Veuillez également rejoindre le chat pour discuter des détails.",
        "proximity_notification": "Vous êtes à proximité! Activez le mot de passe sonore, regardez autour de vous et vous vous rencontrerez!",
        "sound_password": "Mot de passe sonore",
        "playing_sound_password": "Lecture du mot de passe sonore (30 secondes)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Mission accomplie!",
        "check_owner_location": "Vérifier la localisation du propriétaire",
        "check_finder_location": "Vérifier la localisation du trouveur",
        "owner_location_unavailable": "Désolé, la localisation actuelle du propriétaire est temporairement indisponible.",
        "finder_location_unavailable": "Désolé, la localisation actuelle du trouveur est temporairement indisponible.",
    },
    "de": {
        "pet_info_message": (
            "Dies ist die Seite des Haustieres: {pet_name}. Alter: {age} Jahre.\n\n"
            "Wenn Sie dies lesen, bin ich verloren. Ich möchte wirklich nach Hause zu meinem Besitzer. "
            "Er liebt mich sehr und vermisst mich.\n"
            "Bitte kontaktieren Sie ihn über die Schaltfläche unten und helfen Sie mir, nach Hause zu kommen."
        ),
        "contact_owner": "Besitzer kontaktieren",
        "owner_alerted": "Der Besitzer wurde benachrichtigt und wird in Kürze antworten.",
        "contact_action": "Kontakt",
        "owner_found_pet": "Hallo! Ich habe Ihr Haustier gefunden. Bitte kontaktieren Sie mich und ich gebe es Ihnen gerne zurück.",
        "location_instruction": "Fordern Sie den Standort der anderen Person an, um ein Treffen zu vereinbaren.",
        "request_pet_location": "Haustierstandort abrufen",
        "location_requested": "Hallo! Bitte teilen Sie Ihren Standort mit, damit wir uns treffen können.",
        "location_requested_from_owner": "Standort angefordert. Warte auf Antwort.",
        "share_location": "Standort teilen",
        "live_location_howto": (
            "Bitte teilen Sie Ihren Live-Standort mit dem Bot.\n\n"
            "📎 → «Standort» → «Live-Standort teilen» → "
            "Dauer auswählen → senden."
        ),
        "request_location": "Bitte teilen Sie mir mit, wo Sie sind, indem Sie Ihren Standort teilen.",
        "location_shared_response": "Standort geteilt. Bitte warten Sie auf eine Antwort. Bleiben Sie in der Nähe, bis zum Treffen. Sie erhalten eine Benachrichtigung, wenn Sie in der Nähe sind.",
        "finder_live_received": "Bot hat Standort von Ihrem Kontakt erhalten. Bitte teilen Sie auch Ihren Live-Standort, um Audio-Benachrichtigungen zu erhalten, wenn Sie sich dem Treffpunkt nähern.",
        "alert_error_location": "Live-Standort scheint angehalten worden zu sein. Bitte teilen Sie erneut Ihren Live-Standort.",
        "navigation_hint_owner": (
            "Wechseln Sie in den Navigationsmodus, um die Reisezeit zu schätzen, "
            "und informieren Sie dann den Finder über Ihre Ankunftszeit."
        ),
        "navigation_hint_user": "Melden Sie sich, wenn Sie ankommen, oder laden Sie zum Chat ein, wenn andere Arrangements benötigt werden",
        "arrive_10": "Komme in 10 Minuten an",
        "arrive_20": "Komme in 20 Minuten an",
        "arrive_30": "Komme in 30 Minuten an",
        "arrive_60": "Komme in einer Stunde an",
        "start_chat": "Chat starten",
        "arrival_owner_10": "Ich komme innerhalb von 10 Minuten an, bitte warten Sie an Ihrem Standort auf mich.",
        "arrival_owner_20": "Ich komme innerhalb von 20 Minuten an, bitte warten Sie an Ihrem Standort auf mich.",
        "arrival_owner_30": "Ich komme innerhalb von 30 Minuten an, bitte warten Sie an Ihrem Standort auf mich.",
        "arrival_owner_60": "Ich komme innerhalb einer Stunde an, bitte warten Sie an Ihrem Standort auf mich.",
        "arrival_timer_warning": (
            "Sie sollten innerhalb von {select_time} am angegebenen Punkt ankommen. "
            "Wenn Sie Verspätung haben oder sich Pläne ändern, aktualisieren Sie Ihre Ankunftszeit über dieses Menü."
        ),
        "back": "Zurück",
        "language_warning": "Warnung! Ihr Gesprächspartner spricht möglicherweise eine andere Sprache",
        "accept_chat": "Akzeptieren",
        "invite_text": "Folgen Sie {invite_link}, um die Kommunikation in der Gruppe {group_name} fortzusetzen.",
        "owner_chat_offer": (
            "Der Haustierbesitzer lädt Sie zu einem Chat ein, um alternative Treffoptionen zu besprechen.\n"
            "Die Schaltfläche unten bringt Sie zum Chat mit dem Haustierbesitzer."
        ),
        "open_chat": "Chat öffnen",
        "chat_partner_joined_owner": "Gesprächspartner erfolgreich dem Chat beigetreten. Bitte treten Sie auch dem Chat bei, um Details zu besprechen.",
        "proximity_notification": "Sie sind in der Nähe! Aktivieren Sie das Sound-Passwort, schauen Sie sich um und Sie werden sich treffen!",
        "sound_password": "Sound-Passwort",
        "playing_sound_password": "Sound-Passwort wird abgespielt (30 Sekunden)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Mission erfüllt!",
        "check_owner_location": "Standort des Besitzers überprüfen",
        "check_finder_location": "Standort des Finders überprüfen",
        "owner_location_unavailable": "Entschuldigung, der aktuelle Standort des Besitzers ist vorübergehend nicht verfügbar.",
        "finder_location_unavailable": "Entschuldigung, der aktuelle Standort des Finders ist vorübergehend nicht verfügbar.",
    },
    "it": {
        "pet_info_message": (
            "Questa è la pagina dell'animale: {pet_name}. Età: {age} anni.\n\n"
            "Se stai leggendo questo, mi sono perso. Voglio davvero tornare a casa dal mio proprietario. "
            "Mi ama molto e gli manco.\n"
            "Per favore, contattalo usando il pulsante in basso e aiutami a tornare a casa."
        ),
        "contact_owner": "Contatta il proprietario",
        "owner_alerted": "Il proprietario è stato avvisato e risponderà a breve.",
        "contact_action": "Contatta",
        "owner_found_pet": "Ciao! Ho trovato il tuo animale domestico. Per favore, contattami e sarò felice di restituirtelo.",
        "location_instruction": "Richiedi la posizione dell'altra persona per organizzare un incontro.",
        "request_pet_location": "Ottieni posizione animale",
        "location_requested": "Ciao! Per favore, condividi la tua posizione così possiamo incontrarci.",
        "location_requested_from_owner": "Posizione richiesta. In attesa di risposta.",
        "share_location": "Condividi posizione",
        "live_location_howto": (
            "Per favore, condividi la tua posizione in tempo reale con il bot.\n\n"
            "📎 → «Posizione» → «Condividi posizione in tempo reale» → "
            "seleziona durata → invia."
        ),
        "request_location": "Per favore, fammi sapere dove sei condividendo la tua posizione.",
        "location_shared_response": "Posizione condivisa. Attendere una risposta. Rimanere nelle vicinanze fino all'incontro. Riceverai una notifica quando sei vicino.",
        "finder_live_received": "Il bot ha ricevuto la posizione dal tuo contatto. Per favore, condividi anche la tua posizione in tempo reale per ricevere notifiche audio quando ti avvicini al punto d'incontro.",
        "alert_error_location": "La posizione in tempo reale sembra essersi fermata. Per favore, condividi di nuovo la tua posizione in tempo reale.",
        "navigation_hint_owner": (
            "Passa alla modalità navigazione per stimare il tempo di percorrenza, "
            "poi informa il finder del tuo orario di arrivo."
        ),
        "navigation_hint_user": "Comunica quando arrivi o invita a chattare se sono necessari altri accordi",
        "arrive_10": "Arrivo tra 10 minuti",
        "arrive_20": "Arrivo tra 20 minuti",
        "arrive_30": "Arrivo tra 30 minuti",
        "arrive_60": "Arrivo tra un'ora",
        "start_chat": "Inizia chat",
        "arrival_owner_10": "Arriverò entro 10 minuti, per favore aspettami nella tua posizione.",
        "arrival_owner_20": "Arriverò entro 20 minuti, per favore aspettami nella tua posizione.",
        "arrival_owner_30": "Arriverò entro 30 minuti, per favore aspettami nella tua posizione.",
        "arrival_owner_60": "Arriverò entro un'ora, per favore aspettami nella tua posizione.",
        "arrival_timer_warning": (
            "Dovresti arrivare al punto specificato entro {select_time}. "
            "Se sei in ritardo o i piani cambiano, aggiorna il tuo orario di arrivo tramite questo menu."
        ),
        "back": "Indietro",
        "language_warning": "Attenzione! Il tuo interlocutore potrebbe parlare una lingua diversa",
        "accept_chat": "Accetta",
        "invite_text": "Segui {invite_link} per continuare la comunicazione nel gruppo {group_name}.",
        "owner_chat_offer": (
            "Il proprietario dell'animale ti invita a una chat per discutere opzioni alternative d'incontro.\n"
            "Il pulsante qui sotto ti porterà a chattare con il proprietario dell'animale."
        ),
        "open_chat": "Apri chat",
        "chat_partner_joined_owner": "L'interlocutore si è unito alla chat con successo. Per favore, unisciti anche tu alla chat per discutere i dettagli.",
        "proximity_notification": "Sei nelle vicinanze! Attiva la password sonora, guardati intorno e ti incontrerai!",
        "sound_password": "Password sonora",
        "playing_sound_password": "Riproduzione password sonora (30 secondi)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Missione compiuta!",
        "check_owner_location": "Controlla posizione proprietario",
        "check_finder_location": "Controlla posizione finder",
        "owner_location_unavailable": "Spiacenti, la posizione attuale del proprietario non è temporaneamente disponibile.",
        "finder_location_unavailable": "Spiacenti, la posizione attuale del finder non è temporaneamente disponibile.",
    },
    "pt": {
        "pet_info_message": (
            "Esta é a página do animal de estimação: {pet_name}. Idade: {age} anos.\n\n"
            "Se você está lendo isso, estou perdido. Eu realmente quero voltar para casa para o meu dono. "
            "Ele me ama muito e sente minha falta.\n"
            "Por favor, entre em contato com ele usando o botão abaixo e me ajude a voltar para casa."
        ),
        "contact_owner": "Contatar proprietário",
        "owner_alerted": "O proprietário foi notificado e responderá em breve.",
        "contact_action": "Contatar",
        "owner_found_pet": "Olá! Encontrei seu animal de estimação. Por favor, entre em contato comigo e terei prazer em devolvê-lo a você.",
        "location_instruction": "Solicite a localização da outra pessoa para marcar um encontro.",
        "request_pet_location": "Obter localização do animal",
        "location_requested": "Olá! Por favor, compartilhe sua localização para que possamos nos encontrar.",
        "location_requested_from_owner": "Localização solicitada. Aguardando resposta.",
        "share_location": "Compartilhar localização",
        "live_location_howto": (
            "Por favor, compartilhe sua localização ao vivo com o bot.\n\n"
            "📎 → «Localização» → «Compartilhar localização ao vivo» → "
            "selecionar duração → enviar."
        ),
        "request_location": "Por favor, me informe onde você está compartilhando sua localização.",
        "location_shared_response": "Localização compartilhada. Aguarde uma resposta. Fique por perto até a reunião. Você receberá uma notificação quando estiver perto.",
        "finder_live_received": "O bot recebeu a localização do seu contato. Por favor, compartilhe também sua localização ao vivo para receber notificações de áudio ao se aproximar do ponto de encontro.",
        "alert_error_location": "A localização ao vivo parece ter parado. Por favor, compartilhe novamente sua localização ao vivo.",
        "navigation_hint_owner": (
            "Mude para o modo de navegação para estimar o tempo de viagem, "
            "depois informe o finder do seu horário de chegada."
        ),
        "navigation_hint_user": "Notifique quando chegar ou convide para conversar se outros arranjos forem necessários",
        "arrive_10": "Chego em 10 minutos",
        "arrive_20": "Chego em 20 minutos",
        "arrive_30": "Chego em 30 minutos",
        "arrive_60": "Chego em uma hora",
        "start_chat": "Iniciar conversa",
        "arrival_owner_10": "Chegarei em 10 minutos, por favor espere por mim em sua localização.",
        "arrival_owner_20": "Chegarei em 20 minutos, por favor espere por mim em sua localização.",
        "arrival_owner_30": "Chegarei em 30 minutos, por favor espere por mim em sua localização.",
        "arrival_owner_60": "Chegarei em uma hora, por favor espere por mim em sua localização.",
        "arrival_timer_warning": (
            "Você deve chegar ao ponto especificado dentro de {select_time}. "
            "Se atrasado ou os planos mudarem, atualize seu horário de chegada através deste menu."
        ),
        "back": "Voltar",
        "language_warning": "Aviso! Seu interlocutor pode falar um idioma diferente",
        "accept_chat": "Aceitar",
        "invite_text": "Siga {invite_link} para continuar a comunicação no grupo {group_name}.",
        "owner_chat_offer": (
            "O dono do animal convida você para um chat para discutir opções alternativas de encontro.\n"
            "O botão abaixo o levará para conversar com o dono do animal."
        ),
        "open_chat": "Abrir chat",
        "chat_partner_joined_owner": "Interlocutor entrou no chat com sucesso. Por favor, entre também no chat para discutir detalhes.",
        "proximity_notification": "Você está por perto! Ative a senha sonora, olhe ao redor e você se encontrará!",
        "sound_password": "Senha sonora",
        "playing_sound_password": "Reproduzindo senha sonora (30 segundos)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Missão cumprida!",
        "check_owner_location": "Verificar localização do proprietário",
        "check_finder_location": "Verificar localização do finder",
        "owner_location_unavailable": "Desculpe, a localização atual do proprietário não está disponível temporariamente.",
        "finder_location_unavailable": "Desculpe, a localização atual do finder não está disponível temporariamente.",
    },
    "nl": {
        "pet_info_message": (
            "Dit is de pagina van het huisdier: {pet_name}. Leeftijd: {age} jaar.\n\n"
            "Als je dit leest, ben ik verdwaald. Ik wil echt naar huis naar mijn eigenaar. "
            "Hij houdt veel van me en mist me.\n"
            "Neem contact met hem op via de onderstaande knop en help me naar huis terug te keren."
        ),
        "contact_owner": "Eigenaar contacteren",
        "owner_alerted": "De eigenaar is op de hoogte gebracht en zal spoedig reageren.",
        "contact_action": "Contact",
        "owner_found_pet": "Hallo! Ik heb uw huisdier gevonden. Neem contact met me op en ik geef het graag aan u terug.",
        "location_instruction": "Vraag de locatie van de andere persoon om een ontmoeting te regelen.",
        "request_pet_location": "Huisdierlocatie opvragen",
        "location_requested": "Hallo! Deel uw locatie zodat we kunnen afspreken.",
        "location_requested_from_owner": "Locatie aangevraagd. Wachten op reactie.",
        "share_location": "Locatie delen",
        "live_location_howto": (
            "Deel alstublieft uw live locatie met de bot.\n\n"
            "📎 → «Locatie» → «Live locatie delen» → "
            "selecteer duur → verzenden."
        ),
        "request_location": "Laat me alsjeblieft weten waar je bent door je locatie te delen.",
        "location_shared_response": "Locatie gedeeld. Wacht op reactie. Blijf in de buurt tot de ontmoeting. U krijgt een melding wanneer u dichtbij bent.",
        "finder_live_received": "Bot heeft locatie van uw contact ontvangen. Deel ook uw live locatie om audio meldingen te krijgen wanneer u het ontmoetingspunt nadert.",
        "alert_error_location": "Live locatie lijkt te zijn gestopt. Deel alstublieft opnieuw uw live locatie.",
        "navigation_hint_owner": (
            "Schakel over naar navigatiemodus om de reistijd in te schatten, "
            "informeer vervolgens de vinder over uw aankomsttijd."
        ),
        "navigation_hint_user": "Meld wanneer u arriveert of nodig uit om te chatten als andere regelingen nodig zijn",
        "arrive_10": "Kom over 10 minuten aan",
        "arrive_20": "Kom over 20 minuten aan",
        "arrive_30": "Kom over 30 minuten aan",
        "arrive_60": "Kom over een uur aan",
        "start_chat": "Chat starten",
        "arrival_owner_10": "Ik kom binnen 10 minuten aan, wacht alsjeblieft op me op uw locatie.",
        "arrival_owner_20": "Ik kom binnen 20 minuten aan, wacht alsjeblieft op me op uw locatie.",
        "arrival_owner_30": "Ik kom binnen 30 minuten aan, wacht alsjeblieft op me op uw locatie.",
        "arrival_owner_60": "Ik kom binnen een uur aan, wacht alsjeblieft op me op uw locatie.",
        "arrival_timer_warning": (
            "U moet binnen {select_time} op het opgegeven punt arriveren. "
            "Als u vertraging heeft of plannen veranderen, werk dan uw aankomsttijd bij via dit menu."
        ),
        "back": "Terug",
        "language_warning": "Waarschuwing! Uw gesprekspartner spreekt mogelijk een andere taal",
        "accept_chat": "Accepteren",
        "invite_text": "Volg {invite_link} om de communicatie voort te zetten in de groep {group_name}.",
        "owner_chat_offer": (
            "De eigenaar van het huisdier nodigt u uit voor een chat om alternatieve ontmoetingsopties te bespreken.\n"
            "De onderstaande knop brengt u naar de chat met de eigenaar van het huisdier."
        ),
        "open_chat": "Chat openen",
        "chat_partner_joined_owner": "Gesprekspartner succesvol toegetreden tot de chat. Ga ook naar de chat om details te bespreken.",
        "proximity_notification": "U bent in de buurt! Activeer het geluidswachtwoord, kijk om u heen en u zult elkaar ontmoeten!",
        "sound_password": "Geluidswachtwoord",
        "playing_sound_password": "Geluidswachtwoord afspelen (30 seconden)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Missie volbracht!",
        "check_owner_location": "Locatie eigenaar controleren",
        "check_finder_location": "Locatie vinder controleren",
        "owner_location_unavailable": "Sorry, de huidige locatie van de eigenaar is tijdelijk niet beschikbaar.",
        "finder_location_unavailable": "Sorry, de huidige locatie van de vinder is tijdelijk niet beschikbaar.",
    },
    "pl": {
        "pet_info_message": (
            "To jest strona zwierzaka: {pet_name}. Wiek: {age} lat.\n\n"
            "Jeśli to czytasz, zgubiłem się. Naprawdę chcę wrócić do domu do swojego właściciela. "
            "On bardzo mnie kocha i tęskni.\n"
            "Proszę, skontaktuj się z nim za pomocą przycisku poniżej i pomóż mi wrócić do domu."
        ),
        "contact_owner": "Skontaktuj się z właścicielem",
        "owner_alerted": "Właściciel został powiadomiony i wkrótce odpowie.",
        "contact_action": "Kontakt",
        "owner_found_pet": "Cześć! Znalazłem twoje zwierzę. Proszę, skontaktuj się ze mną, a chętnie je tobie zwrócę.",
        "location_instruction": "Poproś o lokalizację drugiej osoby, aby umówić spotkanie.",
        "request_pet_location": "Uzyskaj lokalizację zwierzaka",
        "location_requested": "Cześć! Proszę, udostępnij swoją lokalizację, żebyśmy mogli się spotkać.",
        "location_requested_from_owner": "Lokalizacja requested. Oczekiwanie na odpowiedź.",
        "share_location": "Udostępnij lokalizację",
        "live_location_howto": (
            "Proszę, udostępnij swoją lokalizację na żywo botowi.\n\n"
            "📎 → «Lokalizacja» → «Udostępnij lokalizację na żywo» → "
            "wybierz czas → wyślij."
        ),
        "request_location": "Proszę, poinformuj mnie, gdzie jesteś, udostępniając swoją lokalizację.",
        "location_shared_response": "Lokalizacja udostępniona. Proszę czekać na odpowiedź. Pozostań w pobliżu do spotkania. Otrzymasz powiadomienie, gdy będziesz blisko.",
        "finder_live_received": "Bot otrzymał lokalizację od twojego kontaktu. Proszę, również udostępnij swoją lokalizację na żywo, aby otrzymywać powiadomienia dźwiękowe przy zbliżaniu się do miejsca spotkania.",
        "alert_error_location": "Wygląda na to, że transmisja lokalizacji na żywo zatrzymała się. Proszę udostępnić ponownie lokalizację na żywo.",
        "navigation_hint_owner": (
            "Przejdź do trybu nawigacji, aby oszacować czas podróży, "
            "następnie poinformuj znalazcę o swoim czasie przybycia."
        ),
        "navigation_hint_user": "Powiadom, kiedy przybędziesz lub zaproś do czatu, jeśli potrzebne są inne ustalenia",
        "arrive_10": "Przyjadę za 10 minut",
        "arrive_20": "Przyjadę za 20 minut",
        "arrive_30": "Przyjadę za 30 minut",
        "arrive_60": "Przyjadę za godzinę",
        "start_chat": "Rozpocznij czat",
        "arrival_owner_10": "Przyjadę w ciągu 10 minut, proszę czekać na mnie w swojej lokalizacji.",
        "arrival_owner_20": "Przyjadę w ciągu 20 minut, proszę czekać na mnie w swojej lokalizacji.",
        "arrival_owner_30": "Przyjadę w ciągu 30 minut, proszę czekać na mnie w swojej lokalizacji.",
        "arrival_owner_60": "Przyjadę w ciągu godziny, proszę czekać na mnie w swojej lokalizacji.",
        "arrival_timer_warning": (
            "Powinieneś przybyć do wskazanego punktu w ciągu {select_time}. "
            "Jeśli się spóźniasz lub plany się zmieniają, zaktualizuj czas przybycia przez to menu."
        ),
        "back": "Powrót",
        "language_warning": "Uwaga! Twój rozmówca może mówić w innym języku",
        "accept_chat": "Akceptuj",
        "invite_text": "Śledź {invite_link}, aby kontynuować komunikację w grupie {group_name}.",
        "owner_chat_offer": (
            "Właściciel zwierzęcia zaprasza cię na czat, aby omówić alternatywne opcje spotkania.\n"
            "Przycisk poniżej przeniesie cię do czatu z właścicielem zwierzęcia."
        ),
        "open_chat": "Otwórz czat",
        "chat_partner_joined_owner": "Rozmówca pomyślnie dołączył do czatu. Proszę również dołączyć do czatu, aby omówić szczegóły.",
        "proximity_notification": "Jesteś w pobliżu! Włącz hasło dźwiękowe, rozejrzyj się i spotkasz!",
        "sound_password": "Hasło dźwiękowe",
        "playing_sound_password": "Odtwarzanie hasła dźwiękowego (30 sekund)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Misja wykonana!",
        "check_owner_location": "Sprawdź lokalizację właściciela",
        "check_finder_location": "Sprawdź lokalizację znalazcy",
        "owner_location_unavailable": "Przepraszam, obecna lokalizacja właściciela jest tymczasowo niedostępna.",
        "finder_location_unavailable": "Przepraszam, obecna lokalizacja znalazcy jest tymczasowo niedostępna.",
    },
    "tr": {
        "pet_info_message": (
            "Bu evcil hayvanın sayfası: {pet_name}. Yaş: {age} yaş.\n\n"
            "Bunu okuyorsanız, kayboldum. Gerçekten eve, sahibime dönmek istiyorum. "
            "Beni çok seviyor ve özlüyor.\n"
            "Lütfen aşağıdaki düğmeyi kullanarak onunla iletişime geçin ve eve dönmeme yardım edin."
        ),
        "contact_owner": "Sahibiyle İletişime Geç",
        "owner_alerted": "Sahibi bilgilendirildi ve kısa süre içinde yanıt verecek.",
        "contact_action": "İletişim",
        "owner_found_pet": "Merhaba! Evcil hayvanınızı buldum. Lütfen benimle iletişime geçin ve size memnuniyetle iade ederim.",
        "location_instruction": "Buluşmak için diğer kişinin konumunu isteyin.",
        "request_pet_location": "Evcil Hayvan Konumunu Al",
        "location_requested": "Merhaba! Buluşabilmemiz için lütfen konumunuzu paylaşın.",
        "location_requested_from_owner": "Konum istendi. Yanıt bekleniyor.",
        "share_location": "Konumu Paylaş",
        "live_location_howto": (
            "Lütfen canlı konumunuzu bot ile paylaşın.\n\n"
            "📎 → «Konum» → «Canlı konum paylaş» → "
            "süre seç → gönder."
        ),
        "request_location": "Lütfen konumunuzu paylaşarak nerede olduğunuzu bana bildirin.",
        "location_shared_response": "Konum paylaşıldı. Lütfen yanıt bekleyin. Buluşana kadar yakınlarda kalın. Yakın olduğunuzda bir bildirim alacaksınız.",
        "finder_live_received": "Bot kişinizden konum aldı. Lütfen buluşma noktasına yaklaştığınızda sesli bildirimler almak için canlı konumunuzu da paylaşın.",
        "alert_error_location": "Canlı konum durmuş görünüyor. Lütfen canlı konumunuzu tekrar paylaşın.",
        "navigation_hint_owner": (
            "Yol süresini tahmin etmek için navigasyon moduna geçin, "
            "ardından bulucuya varış saatinizi bildirin."
        ),
        "navigation_hint_user": "Varış zamanını bildirin veya başka düzenlemeler gerekiyorsa sohbet için davet edin",
        "arrive_10": "10 dakika içinde varırım",
        "arrive_20": "20 dakika içinde varırım",
        "arrive_30": "30 dakika içinde varırım",
        "arrive_60": "Bir saat içinde varırım",
        "start_chat": "Sohbet Başlat",
        "arrival_owner_10": "10 dakika içinde varacağım, lütfen beni konumunuzda bekleyin.",
        "arrival_owner_20": "20 dakika içinde varacağım, lütfen beni konumunuzda bekleyin.",
        "arrival_owner_30": "30 dakika içinde varacağım, lütfen beni konumunuzda bekleyin.",
        "arrival_owner_60": "Bir saat içinde varacağım, lütfen beni konumunuzda bekleyin.",
        "arrival_timer_warning": (
            "Belirtilen noktaya {select_time} içinde varmalısınız. "
            "Geciktiyseniz veya planlar değiştiyse, varış saatinizi bu menü aracılığıyla güncelleyin."
        ),
        "back": "Geri",
        "language_warning": "Uyarı! Görüşme partneriniz farklı bir dil konuşuyor olabilir",
        "accept_chat": "Kabul Et",
        "invite_text": "{group_name} grubundaki iletişime devam etmek için {invite_link} bağlantısını takip edin.",
        "owner_chat_offer": (
            "Evcil hayvan sahibi, alternatif buluşma seçeneklerini tartışmak için sizi bir sohbete davet ediyor.\n"
            "Aşağıdaki düğme sizi evcil hayvan sahibiyle sohbet etmeye götürecek."
        ),
        "open_chat": "Sohbeti Aç",
        "chat_partner_joined_owner": "Görüşme partneri sohbete başarıyla katıldı. Lütfen detayları tartışmak için siz de sohbete katılın.",
        "proximity_notification": "Yakındasınız! Ses şifresini etkinleştirin, etrafa bakın ve buluşacaksınız!",
        "sound_password": "Ses Şifresi",
        "playing_sound_password": "Ses şifresi çalınıyor (30 saniye)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Görev tamamlandı!",
        "check_owner_location": "Sahibin konumunu kontrol et",
        "check_finder_location": "Bulucunun konumunu kontrol et",
        "owner_location_unavailable": "Üzgünüz, sahibin mevcut konumu geçici olarak kullanılamıyor.",
        "finder_location_unavailable": "Üzgünüz, bulucunun mevcut konumu geçici olarak kullanılamıyor.",
    },
    "uk": {
        "pet_info_message": (
            "Це сторінка вихованця: {pet_name}. Вік вихованця: {age} років.\n\n"
            "Якщо ви читаєте мою сторінку, значить, я загубився. Я дуже хочу додому, до свого господаря. "
            "Він дуже любить мене і сумує.\n"
            "Будь ласка, зв'яжіться з ним за кнопкою нижче і допоможіть мені повернутися додому."
        ),
        "contact_owner": "Зв'язатися з власником",
        "owner_alerted": "Власника сповіщено, зараз він відреагує.",
        "contact_action": "Зв'язатися",
        "owner_found_pet": "Вітаю! Я знайшов вашого вихованця, зв'яжіться зі мною, і я з радістю його вам поверну.",
        "location_instruction": "Запитуйте локацію співрозмовника, щоб зустрітися.",
        "request_pet_location": "Дізнатися локацію вихованця",
        "location_requested": "Вітаю! Надішліть, будь ласка, локацію, де Ви знаходитесь, щоб ми могли зустрітися.",
        "location_requested_from_owner": "Локацію запрошено, очікуйте відповіді.",
        "share_location": "Поділитися локацією",
        "live_location_howto": (
            "Надішліть, будь ласка, трансляцію вашої live-локації боту.\n\n"
            "📎 → «Геопозиція» → «Трансляція геопозиції в реальному часі» → "
            "вибір часу → надіслати."
        ),
        "request_location": "Будь ласка, повідомте мені, де ви знаходитесь за допомогою відправки вашої локації.",
        "location_shared_response": "Локацію відправлено, очікуйте відповіді. Не відходьте далеко до зустрічі з співрозмовником. Коли ви опинитесь поруч, отримаєте сповіщення.",
        "finder_live_received": "Бот отримав локацію від Вашого співрозмовника. Будь ласка, відправте так само свою трансляцію локації, для того, щоб отримувати звукові сповіщення про наближення до місця зустрічі.",
        "alert_error_location": "Схоже, трансляція локації зупинилася. Будь ласка, відправте live-локацію ще раз.",
        "navigation_hint_owner": (
            "Перейдіть в режим навігації, ви зможете оцінити час в дорозі, "
            "після чого повідомте час прибуття тому, хто знайшов вихованця."
        ),
        "navigation_hint_user": "Повідомте, коли ви прибудете, або запросіть співрозмовника в чат, якщо потрібно обговорити інші варіанти",
        "arrive_10": "Прибуду протягом 10 хвилин",
        "arrive_20": "Прибуду протягом 20 хвилин",
        "arrive_30": "Прибуду протягом 30 хвилин",
        "arrive_60": "Прибуду протягом однієї години",
        "start_chat": "Почати чат",
        "arrival_owner_10": "Прибуду протягом 10 хвилин, будь ласка, зачекайте на мене в точці вашої локації.",
        "arrival_owner_20": "Прибуду протягом 20 хвилин, будь ласка, зачекайте на мене в точці вашої локації.",
        "arrival_owner_30": "Прибуду протягом 30 хвилин, будь ласка, зачекайте на мене в точці вашої локації.",
        "arrival_owner_60": "Прибуду протягом однієї години, будь ласка, зачекайте на мене в точці вашої локації.",
        "arrival_timer_warning": (
            "Ви повинні прибути до вказаної точки протягом {select_time}. "
            "Якщо запізнюєтеся або плани змінилися, повідомте актуальний час прибуття через це меню."
        ),
        "back": "Назад",
        "language_warning": "Увага! Мова спілкування співрозмовника може відрізнятися від вашої",
        "accept_chat": "Приймаю",
        "invite_text": "Перейдіть за посиланням {invite_link}, щоб продовжити спілкування в групі {group_name}.",
        "owner_chat_offer": (
            "Власник вихованця пропонує вам перейти в чат для обговорення інших варіантів зустрічі.\n"
            "Кнопка нижче перекине вас в чат з власником вихованця."
        ),
        "open_chat": "Відкрити чат",
        "chat_partner_joined_owner": "Співрозмовник успішно приєднався до чату. Перейдіть також в чат для обговорення деталей.",
        "proximity_notification": "Ви знаходитесь поруч, увімкніть звуковий пароль, озирніться по сторонах і ви зустрінетеся!",
        "sound_password": "Звуковий пароль",
        "playing_sound_password": "Відтворюється звуковий пароль (30 секунд)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Місія виконана!",
        "check_owner_location": "Перевірити локацію власника",
        "check_finder_location": "Перевірити локацію того, хто знайшов",
        "owner_location_unavailable": "Вибачте, поточна локація власника поки недоступна.",
        "finder_location_unavailable": "Вибачте, поточна локація того, хто знайшов, поки недоступна.",
    },
    "id": {
        "pet_info_message": (
            "Ini adalah halaman hewan peliharaan: {pet_name}. Usia: {age} tahun.\n\n"
            "Jika Anda membaca ini, saya tersesat. Saya sangat ingin pulang ke pemilik saya. "
            "Dia sangat mencintai saya dan merindukan saya.\n"
            "Silakan hubungi dia menggunakan tombol di bawah dan bantu saya pulang."
        ),
        "contact_owner": "Hubungi Pemilik",
        "owner_alerted": "Pemilik telah diberitahu dan akan segera merespons.",
        "contact_action": "Hubungi",
        "owner_found_pet": "Halo! Saya menemukan hewan peliharaan Anda. Silakan hubungi saya dan dengan senang hati saya akan mengembalikannya kepada Anda.",
        "location_instruction": "Minta lokasi orang lain untuk mengatur pertemuan.",
        "request_pet_location": "Dapatkan Lokasi Hewan Peliharaan",
        "location_requested": "Halo! Silakan bagikan lokasi Anda agar kita dapat bertemu.",
        "location_requested_from_owner": "Lokasi diminta. Menunggu respons.",
        "share_location": "Bagikan Lokasi",
        "live_location_howto": (
            "Silakan bagikan lokasi langsung Anda dengan bot.\n\n"
            "📎 → «Lokasi» → «Bagikan Lokasi Langsung» → "
            "pilih durasi → kirim."
        ),
        "request_location": "Silakan beri tahu saya di mana Anda berada dengan membagikan lokasi Anda.",
        "location_shared_response": "Lokasi dibagikan. Silakan tunggu respons. Tetap di dekat sampai pertemuan. Anda akan mendapat notifikasi ketika dekat.",
        "finder_live_received": "Bot menerima lokasi dari kontak Anda. Silakan juga bagikan lokasi langsung Anda untuk mendapatkan notifikasi audio saat mendekati titik pertemuan.",
        "alert_error_location": "Tampaknya lokasi langsung telah berhenti. Harap bagikan lokasi langsung lagi.",
        "navigation_hint_owner": (
            "Beralih ke mode navigasi untuk memperkirakan waktu perjalanan, "
            "lalu beri tahu finder tentang waktu kedatangan Anda."
        ),
        "navigation_hint_user": "Beri tahu ketika tiba atau undang untuk mengobrol jika pengaturan lain diperlukan",
        "arrive_10": "Tiba dalam 10 menit",
        "arrive_20": "Tiba dalam 20 menit",
        "arrive_30": "Tiba dalam 30 menit",
        "arrive_60": "Tiba dalam satu jam",
        "start_chat": "Mulai Obrolan",
        "arrival_owner_10": "Saya akan tiba dalam 10 menit, silakan tunggu saya di lokasi Anda.",
        "arrival_owner_20": "Saya akan tiba dalam 20 menit, silakan tunggu saya di lokasi Anda.",
        "arrival_owner_30": "Saya akan tiba dalam 30 menit, silakan tunggu saya di lokasi Anda.",
        "arrival_owner_60": "Saya akan tiba dalam satu jam, silakan tunggu saya di lokasi Anda.",
        "arrival_timer_warning": (
            "Anda harus tiba di titik yang ditentukan dalam {select_time}. "
            "Jika terlambat atau rencana berubah, perbarui waktu kedatangan Anda melalui menu ini."
        ),
        "back": "Kembali",
        "language_warning": "Peringatan! Partner percakapan Anda mungkin berbicara bahasa yang berbeda",
        "accept_chat": "Terima",
        "invite_text": "Ikuti {invite_link} untuk melanjutkan komunikasi di grup {group_name}.",
        "owner_chat_offer": (
            "Pemilik hewan peliharaan mengundang Anda ke obrolan untuk membahas opsi pertemuan alternatif.\n"
            "Tombol di bawah akan membawa Anda ke obrolan dengan pemilik hewan peliharaan."
        ),
        "open_chat": "Buka Obrolan",
        "chat_partner_joined_owner": "Partner obrolan berhasil bergabung dengan obrolan. Silakan juga bergabung dengan obrolan untuk membahas detail.",
        "proximity_notification": "Anda berada di dekatnya! Aktifkan kata sandi suara, lihat sekeliling dan Anda akan bertemu!",
        "sound_password": "Kata Sandi Suara",
        "playing_sound_password": "Memutar kata sandi suara (30 detik)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Misi selesai!",
        "check_owner_location": "Periksa lokasi pemilik",
        "check_finder_location": "Periksa lokasi finder",
        "owner_location_unavailable": "Maaf, lokasi pemilik saat ini untuk sementara tidak tersedia.",
        "finder_location_unavailable": "Maaf, lokasi finder saat ini untuk sementara tidak tersedia.",
    },
    "ca": {
        "pet_info_message": (
            "Aquesta és la pàgina de la mascota: {pet_name}. Edat: {age} anys.\n\n"
            "Si estàs llegint això, m'he perdut. Realment vull tornar a casa amb el meu amo. "
            "M'estima molt i em troba a faltar.\n"
            "Si us plau, posa't en contacte amb ell mitjançant el botó de sota i ajuda'm a tornar a casa."
        ),
        "contact_owner": "Contactar amb el propietari",
        "owner_alerted": "El propietari ha estat notificat i respondrà aviat.",
        "contact_action": "Contactar",
        "owner_found_pet": "Hola! He trobat la teva mascota. Si us plau, posa't en contacte amb mi i estaré encantat de retornar-te-la.",
        "location_instruction": "Demana la ubicació de l'altra persona per concertar una trobada.",
        "request_pet_location": "Obtenir ubicació de la mascota",
        "location_requested": "Hola! Si us plau, comparteix la teva ubicació perquè puguem quedar.",
        "location_requested_from_owner": "Ubicació sol·licitada. Esperant resposta.",
        "share_location": "Compartir ubicació",
        "live_location_howto": (
            "Si us plau, comparteix la teva ubicació en viu amb el bot.\n\n"
            "📎 → «Ubicació» → «Compartir ubicació en viu» → "
            "seleccionar durada → enviar."
        ),
        "request_location": "Si us plau, fes-me saber on ets compartint la teva ubicació.",
        "location_shared_response": "Ubicació compartida. Si us plau, espera una resposta. Roman a prop fins a la trobada. Rebràs una notificació quan estiguis a prop.",
        "finder_live_received": "El bot ha rebut la ubicació del teu contacte. Si us plau, comparteix també la teva ubicació en viu per rebre notificacions d'àudio quan t'apropis al punt de trobada.",
        "alert_error_location": "Sembla que la ubicació en viu s'ha aturat. Si us plau, comparteixi la ubicació en viu de nou.",
        "navigation_hint_owner": (
            "Canvia al mode de navegació per estimar el temps de viatge, "
            "després informa al finder de la teva hora d'arribada."
        ),
        "navigation_hint_user": "Notifica quan arribis o convida a xatejar si es necessiten altres arranjaments",
        "arrive_10": "Arribo en 10 minuts",
        "arrive_20": "Arribo en 20 minuts",
        "arrive_30": "Arribo en 30 minuts",
        "arrive_60": "Arribo en una hora",
        "start_chat": "Iniciar xat",
        "arrival_owner_10": "Arribaré dins de 10 minuts, si us plau espera'm a la teva ubicació.",
        "arrival_owner_20": "Arribaré dins de 20 minuts, si us plau espera'm a la teva ubicació.",
        "arrival_owner_30": "Arribaré dins de 30 minuts, si us plau espera'm a la teva ubicació.",
        "arrival_owner_60": "Arribaré dins d'una hora, si us plau espera'm a la teva ubicació.",
        "arrival_timer_warning": (
            "Has d'arribar al punt especificat dins de {select_time}. "
            "Si et retrases o els plans canvien, actualitza la teva hora d'arribada a través d'aquest menú."
        ),
        "back": "Enrere",
        "language_warning": "Advertència! El teu interlocutor pot parlar un idioma diferent",
        "accept_chat": "Acceptar",
        "invite_text": "Segueix {invite_link} per continuar la comunicació al grup {group_name}.",
        "owner_chat_offer": (
            "El propietari de la mascota t'invita a un xat per discutir opcions alternatives de trobada.\n"
            "El botó de sota et portarà a xatejar amb el propietari de la mascota."
        ),
        "open_chat": "Obrir xat",
        "chat_partner_joined_owner": "L'interlocutor s'ha unit al xat amb èxit. Si us plau, uneix-te també al xat per discutir detalls.",
        "proximity_notification": "Ets a prop! Activa la contrasenya de so, mira al teu voltant i et trobaràs!",
        "sound_password": "Contrasenya de so",
        "playing_sound_password": "Reproduint contrasenya de so (30 segons)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Missió acomplida!",
        "check_owner_location": "Verificar ubicació del propietari",
        "check_finder_location": "Verificar ubicació del finder",
        "owner_location_unavailable": "Ho sentim, la ubicació actual del propietari no està disponible temporalment.",
        "finder_location_unavailable": "Ho sentim, la ubicació actual del finder no està disponible temporalment.",
    },
    "ro": {
        "pet_info_message": (
            "Aceasta este pagina animalului de companie: {pet_name}. Vârstă: {age} ani.\n\n"
            "Dacă citești asta, m-am rătăcit. Chiar vreau să mă întorc acasă la stăpânul meu. "
            "Mă iubește foarte mult și îi lipsește.\n"
            "Vă rugăm să luați legătura cu el folosind butonul de mai jos și să mă ajutați să mă întorc acasă."
        ),
        "contact_owner": "Contactează proprietarul",
        "owner_alerted": "Proprietarul a fost notificat și va răspunde în curând.",
        "contact_action": "Contact",
        "owner_found_pet": "Bună! Am găsit animalul tău de companie. Te rog, ia legătura cu mine și cu plăcere ți-l voi returna.",
        "location_instruction": "Solicită locația celeilalte persoane pentru a aranja o întâlnire.",
        "request_pet_location": "Obține locația animalului",
        "location_requested": "Bună! Te rog, partajează-ți locația ca să ne putem întâlni.",
        "location_requested_from_owner": "Locație solicitată. Se așteaptă răspuns.",
        "share_location": "Partajează locația",
        "live_location_howto": (
            "Vă rugăm să partajați locația dvs. live cu botul.\n\n"
            "📎 → «Locație» → «Partajează locație live» → "
            "selectați durata → trimite."
        ),
        "request_location": "Vă rugăm să-mi spuneți unde sunteți partajându-și locația.",
        "location_shared_response": "Locație partajată. Vă rugăm să așteptați un răspuns. Rămâneți în apropiere până la întâlnire. Veți primi o notificare când sunteți aproape.",
        "finder_live_received": "Botul a primit locația de la contactul dvs. Vă rugăm să partajați și locația dvs. live pentru a primi notificări audio atunci când vă apropiați de punctul de întâlnire.",
        "alert_error_location": "Se pare că locația live s-a oprit. Vă rugăm să partajați din nou locația live.",
        "navigation_hint_owner": (
            "Comutați în modul de navigare pentru a estima timpul de călătorie, "
            "apoi informați finder-ul despre ora de sosire."
        ),
        "navigation_hint_user": "Anunțați când ajungeți sau invitați la chat dacă sunt necesare alte aranjamente",
        "arrive_10": "Ajung în 10 minute",
        "arrive_20": "Ajung în 20 minute",
        "arrive_30": "Ajung în 30 minute",
        "arrive_60": "Ajung într-o oră",
        "start_chat": "Începe chat",
        "arrival_owner_10": "Voi ajunge în 10 minute, te rog așteaptă-mă la locația ta.",
        "arrival_owner_20": "Voi ajunge în 20 minute, te rog așteaptă-mă la locația ta.",
        "arrival_owner_30": "Voi ajunge în 30 minute, te rog așteaptă-mă la locația ta.",
        "arrival_owner_60": "Voi ajunge într-o oră, te rog așteaptă-mă la locația ta.",
        "arrival_timer_warning": (
            "Ar trebui să ajungi la punctul specificat în {select_time}. "
            "Dacă întârzii sau planurile se schimbă, actualizează-ți ora de sosire prin acest meniu."
        ),
        "back": "Înapoi",
        "language_warning": "Atenție! Partenerul dvs. de conversație poate vorbi o limbă diferită",
        "accept_chat": "Acceptă",
        "invite_text": "Urmează {invite_link} pentru a continua comunicarea în grupul {group_name}.",
        "owner_chat_offer": (
            "Proprietarul animalului vă invită la un chat pentru a discuta opțiuni alternative de întâlnire.\n"
            "Butonul de mai jos vă va duce la chat cu proprietarul animalului."
        ),
        "open_chat": "Deschide chat",
        "chat_partner_joined_owner": "Partenerul de chat s-a alăturat cu succes. Vă rugăm să vă alăturați și dvs. chatului pentru a discuta detalii.",
        "proximity_notification": "Ești aproape! Activează parola sonoră, uită-te în jur și te vei întâlni!",
        "sound_password": "Parolă sonoră",
        "playing_sound_password": "Se redă parola sonoră (30 de secunde)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Misiune îndeplinită!",
        "check_owner_location": "Verifică locația proprietarului",
        "check_finder_location": "Verifică locația finder-ului",
        "owner_location_unavailable": "Ne pare rău, locația actuală a proprietarului nu este disponibilă temporar.",
        "finder_location_unavailable": "Ne pare rău, locația actuală a finder-ului nu este disponibilă temporar.",
    },
    "hu": {
        "pet_info_message": (
            "Ez a háziállat oldala: {pet_name}. Kor: {age} év.\n\n"
            "Ha ezt olvasod, eltévedtem. Nagyon szeretnék hazamenni a gazdámhoz. "
            "Nagyon szeret és hiányol.\n"
            "Kérlek, lépj kapcsolatba vele az alábbi gombbal, és segíts nekem hazajutni."
        ),
        "contact_owner": "Kapcsolatfelvétel a tulajdonossal",
        "owner_alerted": "A tulajdonost értesítettük, és hamarosan válaszol.",
        "contact_action": "Kapcsolat",
        "owner_found_pet": "Szia! Megtaláltam a háziállatodat. Kérlek, lépj kapcsolatba velem, és örömmel visszaadom neked.",
        "location_instruction": "Kérje meg a másik személy helyzetét egy találkozó megbeszélése érdekében.",
        "request_pet_location": "Háziállat helyének lekérése",
        "location_requested": "Szia! Kérlek, oszd meg a helyzeted, hogy találkozhassunk.",
        "location_requested_from_owner": "Helyszín kérve. Válaszra vár.",
        "share_location": "Helymegosztás",
        "live_location_howto": (
            "Kérjük, ossza meg élő helyzetét a bottal.\n\n"
            "📎 → «Hely» → «Élő helymegosztás» → "
            "válassza ki az időtartamot → küldés."
        ),
        "request_location": "Kérjük, jelezze, hol van a helymegosztással.",
        "location_shared_response": "Hely megosztva. Kérjük, várjon választ. Maradjon a közelben a találkozóig. Értesítést kap, amikor közel van.",
        "finder_live_received": "A bot megkapta a helyet a kapcsolatától. Kérjük, ossza meg élő helyzetét is, hogy hangértesítéseket kapjon a találkozási ponthoz közeledve.",
        "alert_error_location": "Az élő helymeghatározás leállt. Kérjük, ossza meg újra az élő helyzetét.",
        "navigation_hint_owner": (
            "Váltson navigációs módra az utazási idő becsléséhez, "
            "majd értesítse a findert az érkezési idejéről."
        ),
        "navigation_hint_user": "Értesítsen érkezéskor vagy hívjon meg csevegésre, ha más megállapodásokra van szükség",
        "arrive_10": "10 perc múlva érkezem",
        "arrive_20": "20 perc múlva érkezem",
        "arrive_30": "30 perc múlva érkezem",
        "arrive_60": "Egy óra múlva érkezem",
        "start_chat": "Csevegés indítása",
        "arrival_owner_10": "10 percen belül érkezem, kérlek várj rám a helyzetednél.",
        "arrival_owner_20": "20 percen belül érkezem, kérlek várj rám a helyzetednél.",
        "arrival_owner_30": "30 percen belül érkezem, kérlek várj rám a helyzetednél.",
        "arrival_owner_60": "Egy órán belül érkezem, kérlek várj rám a helyzetednél.",
        "arrival_timer_warning": (
            "A megadott pontra {select_time} belül kell megérkeznie. "
            "Ha késik vagy a tervek változnak, frissítse érkezési idejét ezen a menüön keresztül."
        ),
        "back": "Vissza",
        "language_warning": "Figyelem! A társalgási partner más nyelven beszélhet",
        "accept_chat": "Elfogad",
        "invite_text": "Kövesse {invite_link} linket a {group_name} csoportban való kommunikáció folytatásához.",
        "owner_chat_offer": (
            "A háziállat tulajdonosa meghív egy chatre, ahol alternatív találkozási lehetőségeket beszélhettek meg.\n"
            "Az alábbi gomb a háziállat tulajdonosával való csevegéshez vezet."
        ),
        "open_chat": "Chat megnyitása",
        "chat_partner_joined_owner": "A partner sikeresen csatlakozott a chathez. Kérjük, lépjen be a chatbe a részletek megbeszéléséhez.",
        "proximity_notification": "A közelben van! Engedélyezze a hangjelszót, nézzen körül és találkoznak!",
        "sound_password": "Hangjelszó",
        "playing_sound_password": "Hangjelszó lejátszása (30 másodperc)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Küldetés teljesítve!",
        "check_owner_location": "Tulajdonos helyének ellenőrzése",
        "check_finder_location": "Meglelő helyének ellenőrzése",
        "owner_location_unavailable": "Sajnos a tulajdonos jelenlegi helye ideiglenesen nem elérhető.",
        "finder_location_unavailable": "Sajnos a meglelő jelenlegi helye ideiglenesen nem elérhető.",
    },
    "cs": {
        "pet_info_message": (
            "Toto je stránka mazlíčka: {pet_name}. Věk: {age} let.\n\n"
            "Pokud toto čtete, ztratil jsem se. Opravdu se chci vrátit domů ke svému majiteli. "
            "Moc mě miluje a chybím mu.\n"
            "Prosím, kontaktujte jej pomocí tlačítka níže a pomozte mi vrátit se domů."
        ),
        "contact_owner": "Kontaktovat majitele",
        "owner_alerted": "Majitel byl upozorněn a brzy odpoví.",
        "contact_action": "Kontakt",
        "owner_found_pet": "Dobrý den! Našel jsem vašeho mazlíčka. Prosím, kontaktujte mě a rád vám ho vrátím.",
        "location_instruction": "Požádejte o polohu druhé osoby, abyste si mohli domluvit setkání.",
        "request_pet_location": "Získat polohu mazlíčka",
        "location_requested": "Dobrý den! Prosím, sdílejte svou polohu, abychom se mohli setkat.",
        "location_requested_from_owner": "Poloha byla požadována. Čeká se na odpověď.",
        "share_location": "Sdílet polohu",
        "live_location_howto": (
            "Prosím, sdílejte svou živou polohu s botem.\n\n"
            "📎 → «Poloha» → «Sdílet živou polohu» → "
            "vyberte dobu trvání → odešlete."
        ),
        "request_location": "Prosím, dejte mi vědět, kde jste, sdílením své polohy.",
        "location_shared_response": "Poloha sdílena. Počkejte prosím na odpověď. Zůstaňte poblíž do setkání. Až budete blízko, dostanete upozornění.",
        "finder_live_received": "Bot obdržel polohu od vašeho kontaktu. Prosím, sdílejte také svou živou polohu, abyste dostávali zvuková upozornění při přiblížení k místu setkání.",
        "alert_error_location": "Zdá se, že živé vysílání polohy bylo přerušeno. Prosím, sdílejte živou polohu znovu.",
        "navigation_hint_owner": (
            "Přepněte do režimu navigace k odhadu doby cestování, "
            "pak informujte nálezce o svém času příjezdu."
        ),
        "navigation_hint_user": "Informujte, když přijedete, nebo pozvěte do chatu, pokud jsou potřebná jiná uspořádání",
        "arrive_10": "Přijedu za 10 minut",
        "arrive_20": "Přijedu za 20 minut",
        "arrive_30": "Přijedu za 30 minut",
        "arrive_60": "Přijedu za hodinu",
        "start_chat": "Začít chat",
        "arrival_owner_10": "Přijedu do 10 minut, prosím, počkejte na mě na svém místě.",
        "arrival_owner_20": "Přijedu do 20 minut, prosím, počkejte na mě na svém místě.",
        "arrival_owner_30": "Přijedu do 30 minut, prosím, počkejte na mě na svém místě.",
        "arrival_owner_60": "Přijedu do hodiny, prosím, počkejte na mě na svém místě.",
        "arrival_timer_warning": (
            "Měli byste dorazit do určeného bodu do {select_time}. "
            "Pokud máte zpoždění nebo se plány změnily, aktualizujte svůj čas příjezdu prostřednictvím této nabídky."
        ),
        "back": "Zpět",
        "language_warning": "Upozornění! Váš konverzační partner může mluvit jiným jazykem",
        "accept_chat": "Přijmout",
        "invite_text": "Sledujte {invite_link} pro pokračování v komunikaci ve skupině {group_name}.",
        "owner_chat_offer": (
            "Vlastník mazlíčka vás zve do chatu k prodiskutování alternativních možností setkání.\n"
            "Tlačítko níže vás přenese do chatu s vlastníkem mazlíčka."
        ),
        "open_chat": "Otevřít chat",
        "chat_partner_joined_owner": "Konverzační partner úspěšně vstoupil do chatu. Připojte se také k chatu k prodiskutování detailů.",
        "proximity_notification": "Jste poblíž! Zapněte zvukové heslo, rozhlédněte se kolem a setkáte se!",
        "sound_password": "Zvukové heslo",
        "playing_sound_password": "Přehrává se zvukové heslo (30 sekund)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Mise splněna!",
        "check_owner_location": "Zkontrolovat polohu majitele",
        "check_finder_location": "Zkontrolovat polohu nálezce",
        "owner_location_unavailable": "Omlouváme se, aktuální poloha majitele je dočasně nedostupná.",
        "finder_location_unavailable": "Omlouváme se, aktuální poloha nálezce je dočasně nedostupná.",
    },
    "sk": {
        "pet_info_message": (
            "Toto je stránka vášho maznáčika: {pet_name}. Vek: {age} rokov.\n\n"
            "Ak toto čítate, stratil som sa. Naozaj sa chcem vrátiť domov k svojmu majiteľovi. "
            "Veľmi ma miluje a chýbam mu.\n"
            "Prosím, kontaktujte ho pomocou tlačidla nižšie a pomôžte mi vrátiť sa domov."
        ),
        "contact_owner": "Kontaktovať majiteľa",
        "owner_alerted": "Majiteľ bol upozornený a čoskoro odpovie.",
        "contact_action": "Kontakt",
        "owner_found_pet": "Dobrý deň! Našiel som vášho maznáčika. Prosím, kontaktujte ma a rád vám ho vrátim.",
        "location_instruction": "Požiadajte o polohu druhej osoby, aby ste si mohli dohodnúť stretnutie.",
        "request_pet_location": "Získať polohu maznáčika",
        "location_requested": "Dobrý deň! Prosím, zdieľajte svoju polohu, aby sme sa mohli stretnúť.",
        "location_requested_from_owner": "Poloha bola požadovaná. Čaká sa na odpoveď.",
        "share_location": "Zdieľať polohu",
        "live_location_howto": (
            "Prosím, zdieľajte svoju živú polohu s botom.\n\n"
            "📎 → «Poloha» → «Zdieľať živú polohu» → "
            "vyberte dĺžku trvania → odošlite."
        ),
        "request_location": "Prosím, dajte mi vedieť, kde ste, zdieľaním svojej polohy.",
        "location_shared_response": "Poloha zdieľaná. Čakajte prosím na odpoveď. Zostaňte poblíž do stretnutia. Keď budete blízko, dostanete upozornenie.",
        "finder_live_received": "Bot dostal polohu od vášho kontaktu. Prosím, zdieľajte aj svoju živú polohu, aby ste dostávali zvukové upozornenia pri približovaní sa k miestu stretnutia.",
        "alert_error_location": "Zdá sa, že živé vysielanie polohy bolo prerušené. Prosím, zdieľajte živú polohu znova.",
        "navigation_hint_owner": (
            "Prepnite do režimu navigácie na odhad doby cesty, "
            "potom informujte nájdeného o svojom čase príchodu."
        ),
        "navigation_hint_user": "Informujte, keď prídete, alebo pozvite do chatu, ak sú potrebné iné dohody",
        "arrive_10": "Prídem za 10 minút",
        "arrive_20": "Prídem za 20 minút",
        "arrive_30": "Prídem za 30 minút",
        "arrive_60": "Prídem za hodinu",
        "start_chat": "Začať chat",
        "arrival_owner_10": "Prídem do 10 minút, prosím, počkajte na ma na svojom mieste.",
        "arrival_owner_20": "Prídem do 20 minút, prosím, počkajte na ma na svojom mieste.",
        "arrival_owner_30": "Prídem do 30 minút, prosím, počkajte na ma na svojom mieste.",
        "arrival_owner_60": "Prídem do hodiny, prosím, počkajte na ma na svojom mieste.",
        "arrival_timer_warning": (
            "Mali by ste doraziť do určeného bodu do {select_time}. "
            "Ak meškate alebo sa plány zmenili, aktualizujte svoj čas príchodu prostredníctvom tohto menu."
        ),
        "back": "Späť",
        "language_warning": "Upozornenie! Váš konverzačný partner môže hovoriť iným jazykom",
        "accept_chat": "Prijať",
        "invite_text": "Sledujte {invite_link} pre pokračovanie v komunikácii v skupine {group_name}.",
        "owner_chat_offer": (
            "Vlastník maznáčika vás pozýva do chatu na prediskutovanie alternatívnych možností stretnutia.\n"
            "Tlačidlo nižšie vás prenesie do chatu s vlastníkom maznáčika."
        ),
        "open_chat": "Otvoriť chat",
        "chat_partner_joined_owner": "Konverzačný partner úspešne vstúpil do chatu. Pripojte sa tiež do chatu na prediskutovanie detailov.",
        "proximity_notification": "Ste poblíž! Zapnite zvukové heslo, obzrite sa okolo a stretnete sa!",
        "sound_password": "Zvukové heslo",
        "playing_sound_password": "Prehráva sa zvukové heslo (30 sekúnd)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Misia splnená!",
        "check_owner_location": "Skontrolovať polohu majiteľa",
        "check_finder_location": "Skontrolovať polohu nájdeného",
        "owner_location_unavailable": "Ospravedlňujeme sa, aktuálna poloha majiteľa je dočasne nedostupná.",
        "finder_location_unavailable": "Ospravedlňujeme sa, aktuálna poloha nájdeného je dočasne nedostupná.",
    },
    "bg": {
        "pet_info_message": (
            "Това е страницата на домашния любимец: {pet_name}. Възраст: {age} години.\n\n"
            "Ако четете това, аз съм се изгубил. Много искам да се върна у дома при стопанина си. "
            "Той много ме обича и му липсвам.\n"
            "Моля, свържете се с него чрез бутона по-долу и ми помогнете да се върна у дома."
        ),
        "contact_owner": "Свържете се със стопанина",
        "owner_alerted": "Стопанинът е уведомен и ще отговори скоро.",
        "contact_action": "Контакт",
        "owner_found_pet": "Здравейте! Намерих вашето домашно животно. Моля, свържете се с мен и с удоволствие ще ви го върна.",
        "location_instruction": "Поискайте местоположението на другия човек, за да организирате среща.",
        "request_pet_location": "Вземете местоположение на домашния любимец",
        "location_requested": "Здравейте! Моля, споделете вашето местоположение, за да можем да се срещнем.",
        "location_requested_from_owner": "Местоположението е поискано. В очакване на отговор.",
        "share_location": "Споделете местоположение",
        "live_location_howto": (
            "Моля, споделете вашето текущо местоположение с бота.\n\n"
            "📎 → «Местоположение» → «Споделяне на текущо местоположение» → "
            "изберете продължителност → изпратете."
        ),
        "request_location": "Моля, уведомете ме къде сте, като споделите вашето местоположение.",
        "location_shared_response": "Местоположението е споделено. Моля, изчакайте отговор. Оставете наблизо до срещата. Ще получите известие, когато сте близо.",
        "finder_live_received": "Ботът получи местоположение от вашия контакт. Моля, също споделете вашето текущо местоположение, за да получавате звукови известия при приближаване към мястото на срещата.",
        "alert_error_location": "Изглежда текущото местоположение е спряло. Моля, споделете отново вашето текущо местоположение.",
        "navigation_hint_owner": (
            "Превключете в режим на навигация, за да оцените времето за пътуване, "
            "след което уведомете намерилия за вашето време на пристигане."
        ),
        "navigation_hint_user": "Уведомете, когато пристигнете, или поканете в чат, ако са необходими други споразумения",
        "arrive_10": "Пристигам след 10 минути",
        "arrive_20": "Пристигам след 20 минути",
        "arrive_30": "Пристигам след 30 минути",
        "arrive_60": "Пристигам след час",
        "start_chat": "Започнете чат",
        "arrival_owner_10": "Ще пристигна в рамките на 10 минути, моля, чакайте ме на вашето местоположение.",
        "arrival_owner_20": "Ще пристигна в рамките на 20 минути, моля, чакайте ме на вашето местоположение.",
        "arrival_owner_30": "Ще пристигна в рамките на 30 минути, моля, чакайте ме на вашето местоположение.",
        "arrival_owner_60": "Ще пристигна в рамките на час, моля, чакайте ме на вашето местоположение.",
        "arrival_timer_warning": (
            "Трябва да пристигнете в указаната точка в рамките на {select_time}. "
            "Ако закъснявате или плановете са се променили, актуализирайте времето си за пристигане чрез това меню."
        ),
        "back": "Назад",
        "language_warning": "Внимание! Вашият събеседник може да говори на различен език",
        "accept_chat": "Приемам",
        "invite_text": "Следвайте {invite_link}, за да продължите комуникацията в групата {group_name}.",
        "owner_chat_offer": (
            "Стопанинът на домашния любимец ви кани в чат, за да обсъди алтернативни опции за среща.\n"
            "Бутонът по-долу ще ви отведе до чат със стопанина на домашния любимец."
        ),
        "open_chat": "Отворете чат",
        "chat_partner_joined_owner": "Събеседникът се присъедини успешно към чата. Моля, присъединете се и вие към чата, за да обсъдите подробности.",
        "proximity_notification": "Вие сте наблизо! Активирайте звуковата парола, огледайте се и ще се срещнете!",
        "sound_password": "Звукова парола",
        "playing_sound_password": "Възпроизвеждане на звукова парола (30 секунди)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Мисията е изпълнена!",
        "check_owner_location": "Проверете местоположението на стопанина",
        "check_finder_location": "Проверете местоположението на намерилия",
        "owner_location_unavailable": "Съжаляваме, текущото местоположение на стопанина е временно недостъпно.",
        "finder_location_unavailable": "Съжаляваме, текущото местоположение на намерилия е временно недостъпно.",
    },
    "et": {
        "pet_info_message": (
            "See on lemmiklooma lehekülg: {pet_name}. Vanus: {age} aastat.\n\n"
            "Kui te seda loete, olen ma ära eksinud. Ma tahan väga tagasi oma omaniku juurde. "
            "Ta armastab mind väga ja igatseb mind.\n"
            "Palun võtke temaga ühendust alloleva nupuga ja aidake mul koju tagasi saada."
        ),
        "contact_owner": "Võtke ühendust omanikuga",
        "owner_alerted": "Omanik on teavitatud ja vastab peagi.",
        "contact_action": "Kontakt",
        "owner_found_pet": "Tere! Ma leidsin teie lemmiklooma. Palun võtke minuga ühendust ja ma annan selle teile rõõmuga tagasi.",
        "location_instruction": "Paluge teise inimese asukohta, et kohtumine korraldada.",
        "request_pet_location": "Hankige lemmiklooma asukoht",
        "location_requested": "Tere! Palun jagage oma asukohta, et saaksime kohtuda.",
        "location_requested_from_owner": "Asukoht on küsitud. Ootame vastust.",
        "share_location": "Jagage asukohta",
        "live_location_howto": (
            "Palun jagage oma reaalajas asukohta botiga.\n\n"
            "📎 → «Asukoht» → «Jaga reaalajas asukohta» → "
            "valige kestus → saada."
        ),
        "request_location": "Palun andke mulle teada, kus te olete, jagades oma asukohta.",
        "location_shared_response": "Asukoht on jagatud. Palun oodake vastust. Jääge lähedale kuni kohtumiseni. Saate teate, kui olete lähedal.",
        "finder_live_received": "Bot sai teie kontakti asukoha. Palun jagage ka oma reaalajas asukohta, et saada heliteateid kohtumispunktile lähenedes.",
        "alert_error_location": "Reaalajas asukoha edastamine on peatanud. Palun jagage oma reaalajas asukohta uuesti.",
        "navigation_hint_owner": (
            "Lülituge navigeerimisrežiimi, et hinnata teekonna aega, "
            "seejärel teatage leidjale oma saabumisaeg."
        ),
        "navigation_hint_user": "Teatage saabumisest või kutsuge vestlusse, kui on vaja muid kokkuleppeid",
        "arrive_10": "Saabun 10 minuti pärast",
        "arrive_20": "Saabun 20 minuti pärast",
        "arrive_30": "Saabun 30 minuti pärast",
        "arrive_60": "Saabun tunni pärast",
        "start_chat": "Alusta vestlust",
        "arrival_owner_10": "Saabun 10 minuti jooksul, palun oodake mind oma asukohas.",
        "arrival_owner_20": "Saabun 20 minuti jooksul, palun oodake mind oma asukohas.",
        "arrival_owner_30": "Saabun 30 minuti jooksul, palun oodake mind oma asukohas.",
        "arrival_owner_60": "Saabun tunni jooksul, palun oodake mind oma asukohas.",
        "arrival_timer_warning": (
            "Peaksite jõudma määratud punkti {select_time} jooksul. "
            "Kui hilinete või plaanid on muutunud, uuendage oma saabumisaega selle menüü kaudu."
        ),
        "back": "Tagasi",
        "language_warning": "Hoiatus! Teie vestluspartner võib rääkida teist keelt",
        "accept_chat": "Nõustun",
        "invite_text": "Järgige linki {invite_link}, et jätkata suhtlemist grupiga {group_name}.",
        "owner_chat_offer": (
            "Lemmiklooma omanik kutsub teid vestlusse, et arutada alternatiivseid kohtumisvõimalusi.\n"
            "Allolev nupp viib teid vestlusele lemmiklooma omanikuga."
        ),
        "open_chat": "Ava vestlus",
        "chat_partner_joined_owner": "Vestluspartner liitus vestlusega edukalt. Palun liituge ka teie vestlusega, et arutada üksikasju.",
        "proximity_notification": "Olete lähedal! Aktiveerige heliparool, vaadake ringi ja kohtute!",
        "sound_password": "Heliparool",
        "playing_sound_password": "Heliparooli esitamine (30 sekundit)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Missioon täidetud!",
        "check_owner_location": "Kontrollige omaniku asukohta",
        "check_finder_location": "Kontrollige leidja asukohta",
        "owner_location_unavailable": "Vabandame, omaniku praegune asukoht on ajutiselt kättesaamatu.",
        "finder_location_unavailable": "Vabandame, leidja praegune asukoht on ajutiselt kättesaamatu.",
    },
    "lv": {
        "pet_info_message": (
            "Šī ir mājdzīvnieka lapa: {pet_name}. Vecums: {age} gadi.\n\n"
            "Ja jūs to lasāt, esmu apmaldījies. Es ļoti gribu atgriezties mājās pie savas saimnieka. "
            "Viņš mani ļoti mīl un manī trūkst.\n"
            "Lūdzu, sazinieties ar viņu, izmantojot zemāk redzamo pogu, un palīdziet man atgriezties mājās."
        ),
        "contact_owner": "Sazināties ar īpašnieku",
        "owner_alerted": "Īpašnieks ir informēts un drīz atbildēs.",
        "contact_action": "Kontakts",
        "owner_found_pet": "Sveiki! Es atradu jūsu mājdzīvnieku. Lūdzu, sazinieties ar mani, un es ar prieku jums to atdošu.",
        "location_instruction": "Pieprasiet otras personas atrašanās vietu, lai organizētu tikšanos.",
        "request_pet_location": "Iegūt mājdzīvnieka atrašanās vietu",
        "location_requested": "Sveiki! Lūdzu, koplietojiet savu atrašanās vietu, lai mēs varētu satikties.",
        "location_requested_from_owner": "Atrašanās vieta ir pieprasīta. Gaida atbildi.",
        "share_location": "Koplietot atrašanās vietu",
        "live_location_howto": (
            "Lūdzu, koplietojiet savu tiešsaistes atrašanās vietu ar botu.\n\n"
            "📎 → «Atrašanās vieta» → «Koplietot tiešsaistes atrašanās vietu» → "
            "atlasiet ilgumu → sūtīt."
        ),
        "request_location": "Lūdzu, dariet man zināmu, kur atrodaties, koplietojot savu atrašanās vietu.",
        "location_shared_response": "Atrašanās vieta koplietota. Lūdzu, gaidiet atbildi. Palieciet tuvumā līdz tikšanās brīdim. Jūs saņemsit paziņojumu, kad būsiet tuvu.",
        "finder_live_received": "Bots saņēma atrašanās vietu no jūsu kontakta. Lūdzu, koplietojiet arī savu tiešsaistes atrašanās vietu, lai saņemtu audio paziņojumus, tuvojoties tikšanās vietai.",
        "alert_error_location": "Šķiet, ka tiešraides atrašanās vieta ir apstājusies. Lūdzu, vēlreiz koplietojiet savu tiešsaistes atrašanās vietu.",
        "navigation_hint_owner": (
            "Pārslēgties uz navigācijas režīmu, lai novērtētu ceļa laiku, "
            "pēc tam informējiet atradēju par ierašanās laiku."
        ),
        "navigation_hint_user": "Paziņojiet, kad ierodaties, vai uzaiciniet tērzēšanā, ja nepieciešami citi norādījumi",
        "arrive_10": "Ierodas pēc 10 minūtēm",
        "arrive_20": "Ierodas pēc 20 minūtēm",
        "arrive_30": "Ierodas pēc 30 minūtēm",
        "arrive_60": "Ierodas pēc stundas",
        "start_chat": "Sākt tērzēšanu",
        "arrival_owner_10": "Ierodšos 10 minūšu laikā, lūdzu, gaidiet mani savā atrašanās vietā.",
        "arrival_owner_20": "Ierodšos 20 minūšu laikā, lūdzu, gaidiet mani savā atrašanās vietā.",
        "arrival_owner_30": "Ierodšos 30 minūšu laikā, lūdzu, gaidiet mani savā atrašanās vietā.",
        "arrival_owner_60": "Ierodšos stundas laikā, lūdzu, gaidiet mani savā atrašanās vietā.",
        "arrival_timer_warning": (
            "Jums vajadzētu ierasties norādītajā punktā {select_time} laikā. "
            "Ja kavējaties vai plāni mainījušies, atjauniniet ierašanās laiku, izmantojot šo izvēlni."
        ),
        "back": "Atpakaļ",
        "language_warning": "Brīdinājums! Jūsu sarunas partneris var runāt citu valodu",
        "accept_chat": "Pieņemt",
        "invite_text": "Sekojiet {invite_link}, lai turpinātu saziņu grupā {group_name}.",
        "owner_chat_offer": (
            "Mājdzīvnieka īpašnieks aicina jūs uz tērzēšanu, lai apspriestu alternatīvas tikšanās iespējas.\n"
            "Zemāk redzamā poga aizvedīs jūs uz tērzēšanu ar mājdzīvnieka īpašnieku."
        ),
        "open_chat": "Atvērt tērzēšanu",
        "chat_partner_joined_owner": "Sarunas partneris veiksmīgi pievienojās tērzēšanai. Lūdzu, pievienojieties arī jūs tērzēšanai, lai apspriestu detaļas.",
        "proximity_notification": "Jūs esat tuvumā! Ieslēdziet skaņas paroli, paskatieties apkārt un jūs satiksities!",
        "sound_password": "Skaņas parole",
        "playing_sound_password": "Atskaņo skaņas paroli (30 sekundes)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Misija izpildīta!",
        "check_owner_location": "Pārbaudīt īpašnieka atrašanās vietu",
        "check_finder_location": "Pārbaudīt atradēja atrašanās vietu",
        "owner_location_unavailable": "Atvainojiet, īpašnieka pašreizējā atrašanās vieta īslaicīgi nav pieejama.",
        "finder_location_unavailable": "Atvainojiet, atradēja pašreizējā atrašanās vieta īslaicīgi nav pieejama.",
    },
    "lt": {
        "pet_info_message": (
            "Tai yra naminio gyvūno puslapis: {pet_name}. Amžius: {age} metai.\n\n"
            "Jei jūs tai skaitote, aš pasiklydau. Aš labai noriu grįžti namo pas savo šeimininką. "
            "Jis mane labai myli ir pasiilgo.\n"
            "Prašome susisiekti su juo naudojant mygtuką žemiau ir padėkite man grįžti namo."
        ),
        "contact_owner": "Susisiekti su savininku",
        "owner_alerted": "Savininkas buvo informuotas ir netrukus atsakys.",
        "contact_action": "Kontaktas",
        "owner_found_pet": "Sveiki! Aš radau jūsų naminį gyvūną. Prašome susisiekti su manimi, ir aš su malonumu jums jį grąžinsiu.",
        "location_instruction": "Paprašykite kito asmens vietos, kad suorganizuotumėte susitikimą.",
        "request_pet_location": "Gauti naminio gyvūno vietą",
        "location_requested": "Sveiki! Prašome pasidalinti savo vieta, kad galėtume susitikti.",
        "location_requested_from_owner": "Vieta užklausta. Laukiama atsakymo.",
        "share_location": "Pasidalinti vieta",
        "live_location_howto": (
            "Prašome pasidalinti savo tiesiogine vieta su botu.\n\n"
            "📎 → «Vieta» → «Pasidalinti tiesiogine vieta» → "
            "pasirinkite trukmę → siųsti."
        ),
        "request_location": "Prašome pranešti man, kur esate, pasidalinant savo vieta.",
        "location_shared_response": "Vieta pasidalinta. Prašome laukti atsakymo. Likite arti iki susitikimo. Gausite pranešimą, kai būsite arti.",
        "finder_live_received": "Botas gavo vietą iš jūsų kontakto. Prašome taip pat pasidalinti savo tiesiogine vieta, kad gautumėte garso pranešimus artėjant prie susitikimo vietos.",
        "alert_error_location": "Atrodo, tiesioginės vietos transliacija sustojo. Prašome dar kartą pasidalinti savo tiesiogine vieta.",
        "navigation_hint_owner": (
            "Perjunkite į navigacijos režimą, kad įvertintumėte kelionės laiką, "
            "tada praneškite radusiajam savo atvykimo laiką."
        ),
        "navigation_hint_user": "Praneškite, kada atvyksite, arba pakvieskite į pokalbį, jei reikia kitų susitarimų",
        "arrive_10": "Atvyksiu per 10 minučių",
        "arrive_20": "Atvyksiu per 20 minučių",
        "arrive_30": "Atvyksiu per 30 minučių",
        "arrive_60": "Atvyksiu per valandą",
        "start_chat": "Pradėti pokalbį",
        "arrival_owner_10": "Atvyksiu per 10 minučių, prašome palaukti manęs savo vietoje.",
        "arrival_owner_20": "Atvyksiu per 20 minučių, prašome palaukti manęs savo vietoje.",
        "arrival_owner_30": "Atvyksiu per 30 minučių, prašome palaukti manęs savo vietoje.",
        "arrival_owner_60": "Atvyksiu per valandą, prašome palaukti manęs savo vietoje.",
        "arrival_timer_warning": (
            "Jūs turėtumėte atvykti į nurodytą vietą per {select_time}. "
            "Jei vėluojate arba planai pasikeitė, atnaujinkite savo atvykimo laiką per šį meniu."
        ),
        "back": "Atgal",
        "language_warning": "Įspėjimas! Jūsų pokalbio partneris gali kalbėti kita kalba",
        "accept_chat": "Priimti",
        "invite_text": "Sekite {invite_link}, kad tęstumėte bendravimą grupėje {group_name}.",
        "owner_chat_offer": (
            "Naminio gyvūno savininkas kviečia jus į pokalbį aptarti alternatyvių susitikimo galimybių.\n"
            "Žemiau esantis mygtukas nuves jus į pokalbį su naminio gyvūno savininku."
        ),
        "open_chat": "Atidaryti pokalbį",
        "chat_partner_joined_owner": "Pokalbio partneris sėkmingai prisijungė prie pokalbio. Prašome ir jūs prisijungti prie pokalbio aptarti detales.",
        "proximity_notification": "Jūs esate netoliese! Įjunkite garso slaptažodį, apsidairykite ir susitiksite!",
        "sound_password": "Garso slaptažodis",
        "playing_sound_password": "Atkuriamas garso slaptažodis (30 sekundžių)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Misija įvykdyta!",
        "check_owner_location": "Patikrinti savininko vietą",
        "check_finder_location": "Patikrinti radėjo vietą",
        "owner_location_unavailable": "Atsiprašome, savininko dabartinė vieta laikinai nepasiekiama.",
        "finder_location_unavailable": "Atsiprašome, radėjo dabartinė vieta laikinai nepasiekiama.",
    },
    "fi": {
        "pet_info_message": "Tämä on lemmikin sivu: {pet_name}. Ikä: {age} vuotta.\n\nJos luet tätä, olen eksynyt. Haluan todella kotiin omistajani luo. Hän rakastaa minua erittäin paljon ja kaipaa minua.\nOta yhteyttä häneseen alla olevasta painikkeesta ja auta minua kotiin.",
        "contact_owner": "Ota yhteyttä omistajaan",
        "owner_alerted": "Omistaja on ilmoitettu ja vastaa pian.",
        "contact_action": "Yhteys",
        "owner_found_pet": "Hei! Löysin lemmikkisi. Ota yhteyttä minuun, ja annan sen mielelläni takaisin sinulle.",
        "location_instruction": "Pyydä toisen henkilön sijaintia tapaamisen järjestämiseksi.",
        "request_pet_location": "Hae lemmikin sijainti",
        "location_requested": "Hei! Jaa sijaintisi, jotta voimme tavata.",
        "location_requested_from_owner": "Sijainti pyydetty. Odotetaan vastausta.",
        "share_location": "Jaa sijainti",
        "live_location_howto": "Ole hyvä ja jaa reaaliaikainen sijaintisi botille.\n\n📎 → «Sijainti» → «Jaa reaaliaikainen sijainti» → valitse kesto → lähetä.",
        "request_location": "Kerro minulle, missä olet, jakamalla sijaintisi.",
        "location_shared_response": "Sijainti jaettu. Odota vastausta. Pysy lähellä tapaamiseen saakka. Saat ilmoituksen, kun olet lähellä.",
        "finder_live_received": "Botti vastaanotti sijainnin yhteystiedostasi. Ole hyvä ja jaa myös reaaliaikainen sijaintisi saadaksesi äänilmoituksia lähestyessäsi tapaamispaikkaa.",
        "alert_error_location": "Reaaliaikainen sijaintijako näyttää pysähtyneen. Ole hyvä ja jaa reaaliaikainen sijaintisi uudelleen.",
        "navigation_hint_owner": "Vaihda navigointitilaan arvioidaksesi matka-ajan, sitten ilmoita löytäjälle saapumisaikasi.",
        "navigation_hint_user": "Ilmoita saapuessasi tai kutsu chattiin, jos muita järjestelyitä tarvitaan",
        "arrive_10": "Saavun 10 minuutissa",
        "arrive_20": "Saavun 20 minuutissa",
        "arrive_30": "Saavun 30 minuutissa",
        "arrive_60": "Saavun tunnin kuluttua",
        "start_chat": "Aloita keskustelu",
        "arrival_owner_10": "Saavun 10 minuutin kuluessa, odota minua sijainnissasi.",
        "arrival_owner_20": "Saavun 20 minuutin kuluessa, odota minua sijainnissasi.",
        "arrival_owner_30": "Saavun 30 minuutin kuluessa, odota minua sijainnissasi.",
        "arrival_owner_60": "Saavun tunnin kuluessa, odota minua sijainnissasi.",
        "arrival_timer_warning": "Sinun tulisi saapua määrättyyn pisteeseen {select_time} kuluessa. Jos myöhästyt tai suunnitelmat muuttuvat, päivitä saapumisaikasi tämän valikon kautta.",
        "back": "Takaisin",
        "language_warning": "Varoitus! Keskustelukumppanisi saattaa puhua eri kieltä",
        "accept_chat": "Hyväksy",
        "invite_text": "Seuraa {invite_link} jatkaaksesi viestintää ryhmässä {group_name}.",
        "owner_chat_offer": "Lemmikin omistaja kutsuu sinut chattiin keskustelemaan vaihtoehtoisista tapaamismahdollisuuksista.\nAlla oleva painike vie sinut chattiin lemmikin omistajan kanssa.",
        "open_chat": "Avaa chat",
        "chat_partner_joined_owner": "Keskustelukumppani liittyi onnistuneesti chattiin. Liity sinäkin chattiin keskustellaksesi yksityiskohdista.",
        "proximity_notification": "Olet lähellä! Ota äänisalasana käyttöön, katso ympärille ja tapaat!",
        "sound_password": "Äänisalasana",
        "playing_sound_password": "Toistetaan äänisalasanaa (30 sekuntia)…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Tehtävä suoritettu!",
        "check_owner_location": "Tarkista omistajan sijainti",
        "check_finder_location": "Tarkista löytäjän sijainti",
        "owner_location_unavailable": "Valitettavasti omistajan nykyinen sijainti on tilapäisesti pois käytöstä.",
        "finder_location_unavailable": "Valitettavasti löytäjän nykyinen sijainti on tilapäisesti pois käytöstä.",
    },
    "sv": {
        "pet_info_message": "Det här är sidan för husdjuret: {pet_name}. Ålder: {age} år.\n\nOm du läser detta har jag gått vilse. Jag vill verkligen återvända hem till min ägare. Han älskar mig väldigt mycket och saknar mig.\nVänligen kontakta honom via knappen nedan och hjälp mig att komma hem.",
        "contact_owner": "Kontakta ägaren",
        "owner_alerted": "Ägaren har meddelats och kommer att svara snart.",
        "contact_action": "Kontakt",
        "owner_found_pet": "Hej! Jag hittade ditt husdjur. Vänligen kontakta mig så återlämnar jag det med glädje.",
        "location_instruction": "Begär den andra personens plats för att ordna ett möte.",
        "request_pet_location": "Hämta husdjurets plats",
        "location_requested": "Hej! Vänligen dela din plats så vi kan mötas.",
        "location_requested_from_owner": "Plats efterfrågad. Väntar på svar.",
        "share_location": "Dela plats",
        "live_location_howto": "Vänligen dela din live-plats med boten.\n\n📎 → «Plats» → «Dela live-plats» → välj varaktighet → skicka.",
        "request_location": "Vänligen meddela mig var du är genom att dela din plats.",
        "location_shared_response": "Plats delad. Vänta på svar. Stanna i närheten till mötet. Du får ett meddelande när du är nära.",
        "finder_live_received": "Botten mottog plats från din kontakt. Vänligen dela också din live-plats för att få ljudmeddelanden när du närmar dig mötesplatsen.",
        "alert_error_location": "Live-platsdelning verkar ha stoppats. Vänligen dela din live-plats igen.",
        "navigation_hint_owner": "Växla till navigeringsläge för att uppskatta restid, meddela sedan hittaren om din ankomsttid.",
        "navigation_hint_user": "Meddela när du anländer eller bjud in till chatt om andra arrangemang behövs",
        "arrive_10": "Ankommer om 10 minuter",
        "arrive_20": "Ankommer om 20 minuter",
        "arrive_30": "Ankommer om 30 minuter",
        "arrive_60": "Ankommer om en timme",
        "start_chat": "Starta chatt",
        "arrival_owner_10": "Jag anländer inom 10 minuter, vänta på mig på din plats.",
        "arrival_owner_20": "Jag anländer inom 20 minuter, vänta på mig på din plats.",
        "arrival_owner_30": "Jag anländer inom 30 minuter, vänta på mig på din plats.",
        "arrival_owner_60": "Jag anländer inom en timme, vänta på mig på din plats.",
        "arrival_timer_warning": "Du bör anlända till den angivna punkten inom {select_time}. Om du är försenad eller planerna ändras, uppdatera din ankomsttid via denna meny.",
        "back": "Tillbaka",
        "language_warning": "Varning! Din samtalspartner kan tala ett annat språk",
        "accept_chat": "Acceptera",
        "invite_text": "Följ {invite_link} för att fortsätta kommunikationen i gruppen {group_name}.",
        "owner_chat_offer": "Husdjursägaren bjuder in dig till en chatt för att diskutera alternativa mötesalternativ.\nKnappen nedan tar dig till chatt med husdjursägaren.",
        "open_chat": "Öppna chatt",
        "chat_partner_joined_owner": "Samtalspartnern anslöt sig framgångsrikt till chatten. Vänligen gå också med i chatten för att diskutera detaljer.",
        "proximity_notification": "Du är nära! Aktivera ljudlösen, titta runt och ni kommer att mötas!",
        "sound_password": "Ljudlösen",
        "playing_sound_password": "Spelar upp ljudlösen (30 sekunder)...",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Uppdrag slutfört!",
        "check_owner_location": "Kontrollera ägarens plats",
        "check_finder_location": "Kontrollera hittarens plats",
        "owner_location_unavailable": "Ledsen, ägarens nuvarande plats är tillfälligt otillgänglig.",
        "finder_location_unavailable": "Ledsen, hittarens nuvarande plats är tillfälligt otillgänglig."
    },
    "da": {
        "pet_info_message": "Dette er dyrets side: {pet_name}. Alder: {age} år.\n\nHvis du læser dette, er jeg faret vild. Jeg vil virkelig hjem til min ejer. Han elsker mig meget og savner mig.\nKontakt venligst ham via knappen nedenfor og hjælp mig hjem.",
        "contact_owner": "Kontakt ejer",
        "owner_alerted": "Ejeren er blevet underrettet og vil snart svare.",
        "contact_action": "Kontakt",
        "owner_found_pet": "Hej! Jeg fandt dit kæledyr. Kontakt mig venligst, så vil jeg med glæde returnere det til dig.",
        "location_instruction": "Anmod om den anden persons placering for at arrangere et møde.",
        "request_pet_location": "Få dyrets placering",
        "location_requested": "Hej! Del venligst din placering, så vi kan mødes.",
        "location_requested_from_owner": "Placering anmodet. Afventer svar.",
        "share_location": "Del placering",
        "live_location_howto": "Del venligst din liveplacering med boten.\n\n📎 → «Placering» → «Del liveplacering» → vælg varighed → send.",
        "request_location": "Del venligst din placering, så jeg ved hvor du er.",
        "location_shared_response": "Placering delt. Afvent svar. Bliv i nærheden til mødet. Du modtager en notifikation når du er nær.",
        "finder_live_received": "Botten modtog placering fra din kontakt. Del venligst også din liveplacering for at modtage lydnotifikationer når du nærmer dig mødestedet.",
        "alert_error_location": "Liveplacering ser ud til at være stoppet. Del venligst din liveplacering igen.",
        "navigation_hint_owner": "Skift til navigations tilstand for at estimere rejsetid, og informer derefter finderen om din ankomsttid.",
        "navigation_hint_user": "Meddel når du ankommer eller inviter til chat hvis andre arrangementer er nødvendige",
        "arrive_10": "Ankommer om 10 minutter",
        "arrive_20": "Ankommer om 20 minutter",
        "arrive_30": "Ankommer om 30 minutter",
        "arrive_60": "Ankommer om en time",
        "start_chat": "Start chat",
        "arrival_owner_10": "Jeg ankommer indenfor 10 minutter, vent venligst på mig på din placering.",
        "arrival_owner_20": "Jeg ankommer indenfor 20 minutter, vent venligst på mig på din placering.",
        "arrival_owner_30": "Jeg ankommer indenfor 30 minutter, vent venligst på mig på din placering.",
        "arrival_owner_60": "Jeg ankommer indenfor en time, vent venligst på mig på din placering.",
        "arrival_timer_warning": "Du bør ankomme til det angivne sted indenfor {select_time}. Hvis du er forsinket eller planerne ændres, opdater din ankomsttid via denne menu.",
        "back": "Tilbage",
        "language_warning": "Advarsel! Din samtalepartner taler muligvis et andet sprog",
        "accept_chat": "Accepter",
        "invite_text": "Følg {invite_link} for at fortsætte kommunikationen i gruppen {group_name}.",
        "owner_chat_offer": "Dyrets ejer inviterer dig til en chat for at diskutere alternative mødemuligheder.\nKnappen nedenfor vil føre dig til chat med dyrets ejer.",
        "open_chat": "Åbn chat",
        "chat_partner_joined_owner": "Samtalepartner joinede chatten succesfuldt. Join venligst også chatten for at diskutere detaljer.",
        "proximity_notification": "Du er i nærheden! Aktiver adgangskode lyd, kig dig omkring og I vil mødes!",
        "sound_password": "Adgangskode lyd",
        "playing_sound_password": "Afspiller adgangskode lyd (30 sekunder)...",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Mission fuldført!",
        "check_owner_location": "Tjek ejerens placering",
        "check_finder_location": "Tjek finderens placering",
        "owner_location_unavailable": "Beklager, ejerens nuværende placering er midlertidigt utilgængelig.",
        "finder_location_unavailable": "Beklager, finderens nuværende placering er midlertidigt utilgængelig.",
    },
    "no": {
        "pet_info_message": "Dette er dyrets side: {pet_name}. Alder: {age} år.\n\nHvis du leser dette, har jeg gått meg vill. Jeg vil virkelig hjem til eieren min. Han er veldig glad i meg og savner meg.\nVennligst ta kontakt med ham via knappen nedenfor og hjelp meg hjem.",
        "contact_owner": "Kontakt eier",
        "owner_alerted": "Eieren er varslet og vil svare snart.",
        "contact_action": "Kontakt",
        "owner_found_pet": "Hei! Jeg fant kjæledyret ditt. Vennligst ta kontakt med meg, så skal jeg gjerne returnere det til deg.",
        "location_instruction": "Be om den andre persons plassering for å avtale et møte.",
        "request_pet_location": "Få dyrets plassering",
        "location_requested": "Hei! Vennligst del din plassering så vi kan møtes.",
        "location_requested_from_owner": "Plassering forespurt. Venter på svar.",
        "share_location": "Del plassering",
        "live_location_howto": "Vennligst del din liveplassering med boten.\n\n📎 → «Plassering» → «Del liveplassering» → velg varighet → send.",
        "request_location": "Vennligst gi meg beskjed om hvor du er ved å dele din plassering.",
        "location_shared_response": "Plassering delt. Vent på svar. Bli i nærheten til møtet. Du vil motta en varsling når du er nær.",
        "finder_live_received": "Botten mottok plassering fra din kontakt. Vennligst del også din liveplassering for å motta lydvarsler når du nærmer deg møtestedet.",
        "alert_error_location": "Liveplassering ser ut til å ha stoppet. Vennligst del din liveplassering på nytt.",
        "navigation_hint_owner": "Bytt til navigasjonsmodus for å estimere reisetid, deretter informer finneren om ankomsttiden din.",
        "navigation_hint_user": "Varsle når du ankommer eller inviter til chat hvis andre avtaler er nødvendig",
        "arrive_10": "Ankommer om 10 minutter",
        "arrive_20": "Ankommer om 20 minutter",
        "arrive_30": "Ankommer om 30 minutter",
        "arrive_60": "Ankommer om en time",
        "start_chat": "Start chat",
        "arrival_owner_10": "Jeg ankommer innen 10 minutter, vennligst vent på meg på din plassering.",
        "arrival_owner_20": "Jeg ankommer innen 20 minutter, vennligst vent på meg på din plassering.",
        "arrival_owner_30": "Jeg ankommer innen 30 minutter, vennligst vent på meg på din plassering.",
        "arrival_owner_60": "Jeg ankommer innen en time, vennligst vent på meg på din plassering.",
        "arrival_timer_warning": "Du bør ankomme til det angitte stedet innen {select_time}. Hvis du er forsinket eller planene endres, oppdater ankomsttiden din via denne menyen.",
        "back": "Tilbake",
        "language_warning": "Advarsel! Samtalepartneren din snakker kanskje et annet språk",
        "accept_chat": "Aksepter",
        "invite_text": "Følg {invite_link} for å fortsette kommunikasjonen i gruppen {group_name}.",
        "owner_chat_offer": "Dyrets eier inviterer deg til en chat for å diskutere alternative møtemuligheter.\nKnappen nedenfor vil føre deg til chat med dyrets eier.",
        "open_chat": "Åpne chat",
        "chat_partner_joined_owner": "Samtalepartner ble med i chatten. Vennligst bli også med i chatten for å diskutere detaljer.",
        "proximity_notification": "Du er i nærheten! Aktiver lydpassord, se deg rundt og dere vil møtes!",
        "sound_password": "Lydpassord",
        "playing_sound_password": "Spiller av lydpassord (30 sekunder)...",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Oppdrag fullført!",
        "check_owner_location": "Sjekk eierens plassering",
        "check_finder_location": "Sjekk finnerens plassering",
        "owner_location_unavailable": "Beklager, eierens nåværende plassering er midlertidig utilgjengelig.",
        "finder_location_unavailable": "Beklager, finnerens nåværende plassering er midlertidig utilgjengelig.",
    },
    "el": {
        "pet_info_message": "Αυτή είναι η σελίδα του κατοικίδιου: {pet_name}. Ηλικία: {age} έτη.\n\nΑν διαβάζετε αυτό, έχω χαθεί. Θέλω πραγματικά να γυρίσω σπίτι στον ιδιοκτήτη μου. Με αγαπάει πολύ και του λείπω.\nΠαρακαλώ επικοινωνήστε μαζί του χρησιμοποιώντας το κουμπί παρακάτω και βοηθήστε με να γυρίσω σπίτι.",
        "contact_owner": "Επικοινωνία με ιδιοκτήτη",
        "owner_alerted": "Ο ιδιοκτήτης έχει ειδοποιηθεί και θα απαντήσει σύντομα.",
        "contact_action": "Επικοινωνία",
        "owner_found_pet": "Γεια σας! Βρήκα το κατοικίδιό σας. Παρακαλώ επικοινωνήστε μαζί μου και με χαρά θα το επιστρέψω.",
        "location_instruction": "Ζητήστε την τοποθεσία του άλλου ατόμου για να κανονίσετε μια συνάντηση.",
        "request_pet_location": "Λήψη τοποθεσίας κατοικίδιου",
        "location_requested": "Γεια σας! Παρακαλώ μοιραστείτε την τοποθεσία σας για να συναντηθούμε.",
        "location_requested_from_owner": "Ζητήθηκε τοποθεσία. Αναμονή απάντησης.",
        "share_location": "Κοινοποίηση τοποθεσίας",
        "live_location_howto": "Παρακαλώ μοιραστείτε την ζωντανή τοποθεσία σας με το bot.\n\n📎 → «Τοποθεσία» → «Κοινοποίηση ζωντανής τοποθεσίας» → επιλέξτε διάρκεια → αποστολή.",
        "request_location": "Παρακαλώ ενημερώστε με πού βρίσκεστε μοιράζοντας την τοποθεσία σας.",
        "location_shared_response": "Τοποθεσία κοινοποιήθηκε. Παρακαλώ περιμένετε απάντηση. Μείνετε κοντά μέχρι τη συνάντηση. Θα λάβετε ειδοποίηση όταν είστε κοντά.",
        "finder_live_received": "Το bot έλαβε τοποθεσία από την επαφή σας. Παρακαλώ μοιραστείτε και την ζωντανή τοποθεσία σας για να λαμβάνετε ηχητικές ειδοποιήσεις όταν πλησιάζετε το σημείο συνάντησης.",
        "alert_error_location": "Η ζωντανή τοποθεσία φαίνεται να έχει σταματήσει. Παρακαλώ μοιραστείτε ξανά την ζωντανή τοποθεσία σας.",
        "navigation_hint_owner": "Αλλάξτε σε λειτουργία πλοήγησης για να εκτιμήσετε το χρόνο ταξιδιού, στη συνέχεια ενημερώστε τον εύρετη για την ώρα άφιξής σας.",
        "navigation_hint_user": "Ειδοποιήστε όταν φτάνετε ή προσκαλέστε σε συνομιλία εάν χρειάζονται άλλες ρυθμίσεις",
        "arrive_10": "Φθάνω σε 10 λεπτά",
        "arrive_20": "Φθάνω σε 20 λεπτά",
        "arrive_30": "Φθάνω σε 30 λεπτά",
        "arrive_60": "Φθάνω σε μια ώρα",
        "start_chat": "Έναρξη συνομιλίας",
        "arrival_owner_10": "Θα φθάσω εντός 10 λεπτών, παρακαλώ περιμένετε με στην τοποθεσία σας.",
        "arrival_owner_20": "Θα φθάσω εντός 20 λεπτών, παρακαλώ περιμένετε με στην τοποθεσία σας.",
        "arrival_owner_30": "Θα φθάσω εντός 30 λεπτών, παρακαλώ περιμένετε με στην τοποθεσία σας.",
        "arrival_owner_60": "Θα φθάσω εντός μιας ώρας, παρακαλώ περιμένετε με στην τοποθεσία σας.",
        "arrival_timer_warning": "Θα πρέπει να φθάσετε στο καθορισμένο σημείο εντός {select_time}. Αν καθυστερείτε ή αλλάξουν τα σχέδια, ενημερώστε την ώρα άφιξής σας μέσω αυτού του μενού.",
        "back": "Πίσω",
        "language_warning": "Προσοχή! Ο συνομιλητής σας μπορεί να μιλάει διαφορετική γλώσσα",
        "accept_chat": "Αποδοχή",
        "invite_text": "Ακολουθήστε {invite_link} για να συνεχίσετε την επικοινωνία στην ομάδα {group_name}.",
        "owner_chat_offer": "Ο ιδιοκτήτης του κατοικίδιου σας προσκαλεί σε συνομιλία για να συζητήσετε εναλλακτικές επιλογές συνάντησης.\nΤο κουμπί παρακάτω θα σας οδηγήσει σε συνομιλία με τον ιδιοκτήτη.",
        "open_chat": "Άνοιγμα συνομιλίας",
        "chat_partner_joined_owner": "Ο συνομιλητής συμμετείχε επιτυχώς. Παρακαλώ μπείτε και εσείς στη συνομιλία για συζήτηση λεπτομερειών.",
        "proximity_notification": "Είστε κοντά! Ενεργοποιήστε τον ηχητικό κωδικό, κοιτάξτε γύρω και θα συναντηθείτε!",
        "sound_password": "Ηχητικός κωδικός",
        "playing_sound_password": "Αναπαραγωγή ηχητικού κωδικού (30 δευτερόλεπτα)...",
        "after_sound_prompt": "*==============================*",
        "mission_done": "Αποστολή ολοκληρώθηκε!",
        "check_owner_location": "Έλεγχος τοποθεσίας ιδιοκτήτη",
        "check_finder_location": "Έλεγχος τοποθεσίας εύρετη",
        "owner_location_unavailable": "Συγγνώμη, η τρέχουσα τοποθεσία του ιδιοκτήτη είναι προσωρινά μη διαθέσιμη.",
        "finder_location_unavailable": "Συγγνώμη, η τρέχουσα τοποθεσία του εύρετη είναι προσωρινά μη διαθέσιμη.",
    },
    "ja": {
        "pet_info_message": "これはペットのページです: {pet_name}。年齢: {age} 歳。\n\nこれを読んでいるなら、私は迷子です。飼い主の元に帰りたいです。飼い主は私をとても愛していて、寂しがっています。\n下のボタンから飼い主に連絡して、家に帰れるように助けてください。",
        "contact_owner": "飼い主に連絡",
        "owner_alerted": "飼い主に通知され、すぐに返信があります。",
        "contact_action": "連絡",
        "owner_found_pet": "こんにちは！あなたのペットを見つけました。連絡してください、喜んでお返しします。",
        "location_instruction": "待ち合わせのために相手の場所をリクエストしてください。",
        "request_pet_location": "ペットの場所を取得",
        "location_requested": "こんにちは！会えるように場所を共有してください。",
        "location_requested_from_owner": "場所をリクエストしました。返信待ちです。",
        "share_location": "場所を共有",
        "live_location_howto": "ボットとライブ位置情報を共有してください。\n\n📎 → «位置情報» → «ライブ位置情報を共有» → 時間を選択 → 送信。",
        "request_location": "場所を共有して、あなたの場所を教えてください。",
        "location_shared_response": "場所が共有されました。返信をお待ちください。会うまでその近くにいてください。近づくと通知が届きます。",
        "finder_live_received": "ボットが連絡先から位置情報を受信しました。会合地点に近づいたときに音声通知を受け取るには、ライブ位置情報も共有してください。",
        "alert_error_location": "ライブ位置情報が停止したようです。もう一度ライブ位置情報を共有してください。",
        "navigation_hint_owner": "移動時間を見積もるためにナビゲーションモードに切り替え、到着時間を発見者に通知してください。",
        "navigation_hint_user": "到着時に通知するか、他の手配が必要な場合はチャットに招待してください",
        "arrive_10": "10分で到着",
        "arrive_20": "20分で到着",
        "arrive_30": "30分で到着",
        "arrive_60": "1時間後に到着",
        "start_chat": "チャット開始",
        "arrival_owner_10": "10分以内に到着しますので、あなたの場所で待っていてください。",
        "arrival_owner_20": "20分以内に到着しますので、あなたの場所で待っていてください。",
        "arrival_owner_30": "30分以内に到着しますので、あなたの場所で待っていてください。",
        "arrival_owner_60": "1時間以内に到着しますので、あなたの場所で待っていてください。",
        "arrival_timer_warning": "{select_time} 以内に指定されたポイントに到着する必要があります。遅延または計画変更がある場合は、このメニューから到着時間を更新してください。",
        "back": "戻る",
        "language_warning": "警告！会話相手は異なる言語を話す可能性があります",
        "accept_chat": "承諾",
        "invite_text": "{invite_link} をフォローして、グループ {group_name} で通信を続けてください。",
        "owner_chat_offer": "ペットの所有者が、別の会合オプションについて話し合うためにチャットに招待しています。\n下のボタンをクリックすると、ペットの所有者とのチャットに移動します。",
        "open_chat": "チャットを開く",
        "chat_partner_joined_owner": "相手がチャットに参加しました。詳細について話し合うために、あなたもチャットに参加してください。",
        "proximity_notification": "近くにいます！音声パスワードを有効にして、周りを見回すと会えます！",
        "sound_password": "音声パスワード",
        "playing_sound_password": "音声パスワードを再生中（30秒）…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "ミッション完了！",
        "check_owner_location": "所有者の場所を確認",
        "check_finder_location": "発見者の場所を確認",
        "owner_location_unavailable": "申し訳ありません、所有者の現在の場所は一時的に利用できません。",
        "finder_location_unavailable": "申し訳ありません、発見者の現在の場所は一時的に利用できません。",
    },
    "zh": {
        "pet_info_message": "这是宠物页面: {pet_name}。年龄: {age} 岁。\n\n如果你看到这个，说明我迷路了。我很想回到我的主人身边。他非常爱我，也很想念我。\n请通过下面的按钮联系他，帮我回家。",
        "contact_owner": "联系主人",
        "owner_alerted": "已通知主人，很快就会回复。",
        "contact_action": "联系",
        "owner_found_pet": "你好！我找到了你的宠物。请联系我，我很乐意归还。",
        "location_instruction": "请求对方的位置以安排会面。",
        "request_pet_location": "获取宠物位置",
        "location_requested": "你好！请分享你的位置，以便我们见面。",
        "location_requested_from_owner": "已请求位置。等待回复中。",
        "share_location": "分享位置",
        "live_location_howto": "请与机器人分享你的实时位置。\n\n📎 → «位置» → «分享实时位置» → 选择持续时间 → 发送。",
        "request_location": "请分享你的位置，让我知道你在哪里。",
        "location_shared_response": "位置已分享。请等待回复。在见面之前请保持在附近。当你靠近时会收到通知。",
        "finder_live_received": "机器人收到了你联系人的位置。请也分享你的实时位置，以便在接近会面点时收到声音通知。",
        "alert_error_location": "实时位置似乎已停止。请重新分享你的实时位置。",
        "navigation_hint_owner": "切换到导航模式以估计旅行时间，然后通知发现者你的到达时间。",
        "navigation_hint_user": "到达时通知或邀请聊天如需其他安排",
        "arrive_10": "10分钟内到达",
        "arrive_20": "20分钟内到达",
        "arrive_30": "30分钟内到达",
        "start_chat": "开始聊天",
        "arrival_owner_10": "我在10分钟内到达，请在你的位置等我。",
        "arrival_owner_20": "我在20分钟内到达，请在你的位置等我。",
        "arrival_owner_30": "我在30分钟内到达，请在你的位置等我。",
        "arrival_owner_60": "我在一小时内到达，请在你的位置等我。",
        "arrive_60": "一小时内到达",
        "arrival_timer_warning": "你应该在 {select_time} 内到达指定点。如果延迟或计划变更，请通过此菜单更新你的到达时间。",
        "back": "返回",
        "language_warning": "警告！你的对话伙伴可能使用不同的语言",
        "accept_chat": "接受",
        "invite_text": "跟随 {invite_link} 以在 {group_name} 群组中继续通信。",
        "owner_chat_offer": "宠物主人邀请你聊天讨论其他会面选项。\n下面的按钮将带你与宠物主人聊天。",
        "open_chat": "打开聊天",
        "chat_partner_joined_owner": "对方成功加入聊天。请也加入聊天以讨论细节。",
        "proximity_notification": "你在附近！启用声音密码，环顾四周，你们就会见面！",
        "sound_password": "声音密码",
        "playing_sound_password": "播放声音密码（30秒）…",
        "after_sound_prompt": "*==============================*",
        "mission_done": "任务完成！",
        "check_owner_location": "检查主人的位置",
        "check_finder_location": "检查发现者的位置",
        "owner_location_unavailable": "抱歉，主人当前的位置暂时不可用。",
        "finder_location_unavailable": "抱歉，发现者当前的位置暂时不可用。",
    },
    "ko": {
        "pet_info_message": "이것은 반려동물 페이지입니다: {pet_name}. 나이: {age} 살.\n\n이것을 읽고 있다면, 저는 길을 잃었습니다. 정말로 주인에게 돌아가고 싶습니다. 주인은 저를 매우 사랑하고 그리워하고 있습니다.\n아래 버튼을 통해 주인에게 연락하여 집에 돌아갈 수 있도록 도와주세요.",
        "contact_owner": "주인에게 연락",
        "owner_alerted": "주인에게 알림이 전송되었으며 곧 응답할 것입니다.",
        "contact_action": "연락",
        "owner_found_pet": "안녕하세요! 당신의 반려동물을 찾았습니다. 연락해 주시면 기꺼이 돌려드리겠습니다.",
        "location_instruction": "만남을 주선하기 위해 상대방의 위치를 요청하세요.",
        "request_pet_location": "반려동물 위치 가져오기",
        "location_requested": "안녕하세요! 만날 수 있도록 위치를 공유해 주세요.",
        "location_requested_from_owner": "위치가 요청되었습니다. 응답을 기다리고 있습니다.",
        "share_location": "위치 공유",
        "live_location_howto": "봇과 실시간 위치를 공유해 주세요.\n\n📎 → «위치» → «실시간 위치 공유» → 지속 시간 선택 → 전송.",
        "request_location": "위치를 공유하여 어디에 있는지 알려주세요.",
        "location_shared_response": "위치가 공유되었습니다. 응답을 기다려 주세요. 만날 때까지 근처에 머물러 주세요. 가까워지면 알림을 받게 됩니다.",
        "finder_live_received": "봇이 연락처로부터 위치를 받았습니다. 만남 지점에 접근할 때 음성 알림을 받으려면 실시간 위치도 공유해 주세요.",
        "alert_error_location": "실시간 위치가 중단된 것 같습니다. 실시간 위치를 다시 공유해 주세요.",
        "navigation_hint_owner": "이동 시간을 추정하기 위해 내비게이션 모드로 전환한 다음, 발견자에게 도착 시간을 알려주세요.",
        "navigation_hint_user": "도착 시 알리거나 다른 약속이 필요한 경우 채팅에 초대하세요",
        "arrive_10": "10분 후 도착",
        "arrive_20": "20분 후 도착",
        "arrive_30": "30분 후 도착",
        "arrive_60": "한 시간 후 도착",
        "start_chat": "채팅 시작",
        "arrival_owner_10": "10분 이내에 도착하겠습니다. 당신의 위치에서 기다려 주세요.",
        "arrival_owner_20": "20분 이내에 도착하겠습니다. 당신의 위치에서 기다려 주세요.",
        "arrival_owner_30": "30분 이내에 도착하겠습니다. 당신의 위치에서 기다려 주세요.",
        "arrival_owner_60": "한 시간 이내에 도착하겠습니다. 당신의 위치에서 기다려 주세요.",
        "arrival_timer_warning": "{select_time} 이내에 지정된 지점에 도착해야 합니다. 지연되거나 계획이 변경되면 이 메뉴를 통해 도착 시간을 업데이트하세요.",
        "back": "뒤로",
        "language_warning": "경고! 대화 상대가 다른 언어를 사용할 수 있습니다",
        "accept_chat": "수락",
        "invite_text": "{invite_link}을 따라 {group_name} 그룹에서 계속 소통하세요.",
        "owner_chat_offer": "반려동물 주인이 대안적인 만남 옵션을 논의하기 위해 채팅에 초대합니다.\n아래 버튼을 클릭하면 반려동물 주인과의 채팅으로 이동합니다.",
        "open_chat": "채팅 열기",
        "chat_partner_joined_owner": "상대방이 채팅에 성공적으로 참여했습니다. 세부 사항을 논의하기 위해 채팅에 참여해 주세요.",
        "proximity_notification": "근처에 있습니다! 음성 비밀번호를 활성화하고 주변을 둘러보면 만날 수 있습니다!",
        "sound_password": "음성 비밀번호",
        "playing_sound_password": "음성 비밀번호 재생 중 (30초)...",
        "after_sound_prompt": "*==============================*",
        "mission_done": "임무 완료!",
        "check_owner_location": "주인의 위치 확인",
        "check_finder_location": "발견자의 위치 확인",
        "owner_location_unavailable": "죄송합니다. 주인의 현재 위치를 일시적으로 사용할 수 없습니다.",
        "finder_location_unavailable": "죄송합니다. 발견자의 현재 위치를 일시적으로 사용할 수 없습니다.",
    },
    "ar": {
        "pet_info_message": "هذه صفحة الحيوان الأليف: {pet_name}. العمر: {age} سنة.\n\nإذا كنت تقرأ هذا، فأنا ضائع. أريد حقًا العودة إلى المنزل إلى مالكي. يحبني كثيرًا ويشتاق لي.\nيرجى الاتصال به باستخدام الزر أدناه ومساعدتي في العودة إلى المنزل.",
        "contact_owner": "الاتصال بالمالك",
        "owner_alerted": "تم إخطار المالك وسيرد قريبًا.",
        "contact_action": "اتصال",
        "owner_found_pet": "مرحبًا! لقد وجدت حيوانك الأليف. يرجى الاتصال بي وسأعيده إليك بكل سرور.",
        "location_instruction": "اطلب موقع الشخص الآخر لترتيب لقاء.",
        "request_pet_location": "الحصول على موقع الحيوان الأليف",
        "location_requested": "مرحبًا! يرجى مشاركة موقعك حتى نتمكن من اللقاء.",
        "location_requested_from_owner": "تم طلب الموقع. في انتظار الرد.",
        "share_location": "مشاركة الموقع",
        "live_location_howto": "يرجى مشاركة موقعك المباشر مع البوت.\n\n📎 → «الموقع» → «مشاركة الموقع المباشر» → اختر المدة → إرسال.",
        "request_location": "يرجى إعلامي بمكانك عن طريق مشاركة موقعك.",
        "location_shared_response": "تم مشاركة الموقع. يرجى الانتظار للرد. ابق قريبًا حتى اللقاء. ستصلك إشعار عندما تكون قريبًا.",
        "finder_live_received": "تلقى البوت موقعًا من جهة اتصالك. يرجى أيضًا مشاركة موقعك المباشر لتلقي إشعارات صوتية عند الاقتراب من نقطة اللقاء.",
        "alert_error_location": "يبدو أن البث المباشر للموقع قد توقف. يرجى مشاركة موقعك المباشر مرة أخرى.",
        "navigation_hint_owner": "انتقل إلى وضع الملاحة لتقدير وقت السفر، ثم أبلغ الشخص الذي وجد الحيوان بوقت وصولك.",
        "navigation_hint_user": "أبلغ عند الوصول أو ادعُ إلى الدردشة إذا كانت هناك ترتيبات أخرى مطلوبة",
        "arrive_10": "سأصل خلال 10 دقائق",
        "arrive_20": "سأصل خلال 20 دقيقة",
        "arrive_30": "سأصل خلال 30 دقيقة",
        "arrive_60": "سأصل خلال ساعة",
        "start_chat": "بدء الدردشة",
        "arrival_owner_10": "سأصل خلال 10 دقائق، يرجى انتظاري في موقعك.",
        "arrival_owner_20": "سأصل خلال 20 دقيقة، يرجى انتظاري في موقعك.",
        "arrival_owner_30": "سأصل خلال 30 دقيقة، يرجى انتظاري في موقعك.",
        "arrival_owner_60": "سأصل خلال ساعة، يرجى انتظاري في موقعك.",
        "arrival_timer_warning": "يجب أن تصل إلى النقطة المحددة خلال {select_time}. إذا تأخرت أو تغيرت الخطط، فقم بتحديث وقت وصولك من خلال هذه القائمة.",
        "back": "عودة",
        "language_warning": "تحذير! قد يتحدث شريك المحادثة لغة مختلفة",
        "accept_chat": "قبول",
        "invite_text": "اتبع {invite_link} لمواصلة الاتصال في مجموعة {group_name}.",
        "owner_chat_offer": "يدعوك مالك الحيوان الأليف إلى الدردشة لمناقشة خيارات لقاء بديلة.\nسينقلك الزر أدناه إلى الدردشة مع مالك الحيوان الأليف.",
        "open_chat": "فتح الدردشة",
        "chat_partner_joined_owner": "انضم شريك المحادثة بنجاح. يرجى الانضمام إلى الدردشة أيضًا لمناقشة التفاصيل.",
        "proximity_notification": "أنت قريب! قم بتمكين كلمة المرور الصوتية، انظر حولك وسوف تلتقي!",
        "sound_password": "كلمة المرور الصوتية",
        "playing_sound_password": "جاري تشغيل كلمة المرور الصوتية (30 ثانية)...",
        "after_sound_prompt": "*==============================*",
        "mission_done": "تمت المهمة!",
        "check_owner_location": "تحقق من موقع المالك",
        "check_finder_location": "تحقق من موقع الشخص الذي وجد الحيوان",
        "owner_location_unavailable": "عذرًا، موقع المالك الحالي غير متاح مؤقتًا.",
        "finder_location_unavailable": "عذرًا، موقع الشخص الذي وجد الحيوان غير متاح مؤقتًا.",
    },
    "he": {
        "pet_info_message": "זהו עמוד החיית המחמד: {pet_name}. גיל: {age} שנים.\n\nאם אתה קורא את זה, אני הלכתי לאיבוד. אני באמת רוצה לחזור הביתה לבעלים שלי. הוא אוהב אותי מאוד ומתגעגע אלי.\nאנא צור איתו קשר באמצעות הכפתור למטה ועזור לי לחזור הביתה.",
        "contact_owner": "יצירת קשר עם הבעלים",
        "owner_alerted": "הבעלים קיבל הודעה ויענה בקרוב.",
        "contact_action": "יצירת קשר",
        "owner_found_pet": "שלום! מצאתי את חיית המחמד שלך. אנא צור איתי קשר ואחזיר אותה בשמחה.",
        "location_instruction": "בקש את המיקום של האדם השני כדי לתאם פגישה.",
        "request_pet_location": "קבל מיקום חיית מחמד",
        "location_requested": "שלום! אנא שתף את המיקום שלך כדי שנוכל להיפגש.",
        "location_requested_from_owner": "המיקום התבקש. ממתין לתגובה.",
        "share_location": "שתף מיקום",
        "live_location_howto": "אנא שתף את המיקום החי שלך עם הבוט.\n\n📎 → «מיקום» → «שתף מיקום חי» → בחר משך זמן → שלח.",
        "request_location": "אנא הודע לי איפה אתה על ידי שיתוף המיקום שלך.",
        "location_shared_response": "המיקום שותף. אנא המתן לתגובה. הישאר בקרבת מקום עד הפגישה. תקבל הודעה כשתהיה קרוב.",
        "finder_live_received": "הבוט קיבל מיקום מאיש הקשר שלך. אנא שתף גם את המיקום החי שלך כדי לקבל התראות קוליות כשאתה מתקרב לנקודת הפגישה.",
        "alert_error_location": "נראה שהמיקום החי הפסיק. אנא שתף את המיקום החי שלך שוב.",
        "navigation_hint_owner": "עבור למצב ניווט כדי להעריך זמן נסיעה, ואז הודע למוצא על זמן ההגעה שלך.",
        "navigation_hint_user": "הודע כשאתה מגיע או הזמן לצ'אט אם נדרשים הסדרים אחרים",
        "arrive_10": "מגיע בעוד 10 דקות",
        "arrive_20": "מגיע בעוד 20 דקות",
        "arrive_30": "מגיע בעוד 30 דקות",
        "arrive_60": "מגיע בעוד שעה",
        "start_chat": "התחל צ'אט",
        "arrival_owner_10": "אני אגיע תוך 10 דקות, אנא המתן לי במיקום שלך.",
        "arrival_owner_20": "אני אגיע תוך 20 דקות, אנא המתן לי במיקום שלך.",
        "arrival_owner_30": "אני אגיע תוך 30 דקות, אנא המתן לי במיקום שלך.",
        "arrival_owner_60": "אני אגיע תוך שעה, אנא המתן לי במיקום שלך.",
        "arrival_timer_warning": "אתה צריך להגיע לנקודה המצוינת תוך {select_time}. אם אתה מתעכב או התוכניות משתנות, עדכן את זמן ההגעה שלך דרך התפריט הזה.",
        "back": "חזור",
        "language_warning": "אזהרה! שותף השיחה שלך עשוי לדבר שפה אחרת",
        "accept_chat": "קבל",
        "invite_text": "עקוב אחר {invite_link} כדי להמשיך בתקשורת בקבוצה {group_name}.",
        "owner_chat_offer": "בעל חיית המחמד מזמין אותך לצ'אט כדי לדון באפשרויות פגישה חלופיות.\nהכפתור למטה ייקח אותך לצ'אט עם בעל חיית המחמד.",
        "open_chat": "פתח צ'אט",
        "chat_partner_joined_owner": "שותף השיחה הצטרף בהצלחה לצ'אט. אנא הצטרף גם אתה לצ'אט כדי לדון בפרטים.",
        "proximity_notification": "אתה בקרבת מקום! הפעל סיסמת קול, הסתכל סביב ותפגשו!",
        "sound_password": "סיסמת קול",
        "playing_sound_password": "מנגן סיסמת קול (30 שניות)...",
        "after_sound_prompt": "*==============================*",
        "mission_done": "המשימה הושלמה!",
        "check_owner_location": "בדוק מיקום הבעלים",
        "check_finder_location": "בדוק מיקום המוצא",
        "owner_location_unavailable": "מצטער, המיקום הנוכחי של הבעלים אינו זמין זמנית.",
        "finder_location_unavailable": "מצטער, המיקום הנוכחי של המוצא אינו זמין זמנית.",
    }
}

DEFAULT_LANG = "en"


def normalize_lang(lang: str | None) -> str:
    if not lang:
        return DEFAULT_LANG
    base = lang.split("-")[0].lower()
    return base if base in locales else DEFAULT_LANG


class I18n:
    def __init__(self, data: Dict[str, Dict[str, str]], default: str = DEFAULT_LANG):
        self.data = data
        self.default = default

    def t(self, lang: str, key: str, **kwargs: Any) -> str:
        code = normalize_lang(lang)
        bucket = self.data.get(code, {})
        s = bucket.get(key) or self.data[self.default].get(key) or key
        try:
            return s.format(**kwargs)
        except Exception:
            return s


I18N = I18n(locales, DEFAULT_LANG)