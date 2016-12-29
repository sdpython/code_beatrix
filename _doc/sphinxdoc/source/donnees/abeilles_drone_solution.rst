
.. index:: abeille, drone

.. _l-abeilles_drones_sol:

Les petits drones ailés (solution)
==================================

**Pourquoi choisir de fabriquer un drone qui livre des colis ou un drone polinisateur plutôt qu'un autre ?**

L'industrie investit dans le domaine de la livraison car la recherche mettra au point
cette technologie dans une avenir assez proche mais surtout parce que le service
sera probablement moins cher et plus pratique à utiliser. Les entreprises qui investissent
font le pari que cela sera un avantage par rapport aux autres entreprises.
C'est sans doute un mauvais signe si une société décide de mettre au point une abeille polinisatrice.
Cela voudrait dire que les vraies abeilles ne remplissent plus ce rôle et que nous n'avons
pas su empêcher leur disparition. Il n'est pas impossible que d'autres idées voient le jour
si la pollution décime une population d'animal très utile pour la nature et donc pour l'Homme.

**Pourquoi pas un drone chauve-souris ? Est-ce plus complexe techniquement ?**

Les chauves-souris utilisent le son pour se diriger. La question sous-entend que le drone
utiliserait ce moyen pour se diriger. Ce n'est pas plus complexe techniquement, le sonar existe depuis longtemps.
C'est sur la reconnaissance que le problème devient compliqué. Après plusieurs années de recherche
- on a commencé à s'y intéresser vraiment dans les années 1990 -,
la reconnaissance de la parole n'est pas encore tout-à-fait au point.
Elle progresse rapidement aujourd'hui grâce à la puissance des ordinateurs
et des algorithmes comme le `deep learning <https://fr.wikipedia.org/wiki/Deep_learning>`_.
Les chercheurs se sont intéressés à la vision, un peu le goût et les odeurs, c'est-à-dire
les sens que les humains maîtrisent bien car il est plus facile de dire ce que la machine
doit faire. Nous savons décrire ce qu'il y a dans une image visuelle mais pas
vraiment dans une image sonore. C'est un peu comme essayer de prendre une décision
sans rien comprendre du problème. Cela ne veut pas dire que c'est impossible,
simplement que cela demande un peu plus d'imagination.

**Comment un drone apprend-il à se mouvoir ?**

Le drone n'est si différente d'un être vivant de ce point de vue là. Il dispose de capteurs,
des caméras, deux de préférence, et peut décider de changer sa vitesse ou sa direction. Il
reçoit des informations, dispose d'un nombre d'actions limitées avec l'objectif de ce rendre
au point B en évitant les obstacles. Le drone passe la majeur partie de son temps à analyser des images
et c'est de loin la tâche la plus complexe. Néanmoins, le drone n'apprend pas tout seul, c'est un chercheur
qui écrit un programme informatique qui va apprendre. Une fois appris, on peut créer autant de drone
qu'on veut, les répliquer à l'infini.
Une fois que le programme informatique aura appris, il saura avoir une représentation
de ce qu'il entoure en trois dimensions. Concrètement, l'apprentissage d'un drone consiste
à décrypter une séquence d'images captées par les caméras pour déterminer la forme des objets qui bougent,
leur vitesse et leur directions. Un petit aperçu de l'apprentissage :
`Predator: Camera That Learns <https://www.youtube.com/watch?v=1GhNXHCQGsM>`_,
`Predator: A Visual Tracker that Learns from its Errors <https://www.youtube.com/watch?v=lmG_FjG4Dy8>`_.

**Que fait l'article *Retour sur le Google Hash Code 2016* dans la liste ?**

Les batteries des drones sont très limitées. Elles ne peuvent pas être trop lourdes sans
quoi il dépense plus d'énergie pour porter. En 2016, il est apparemment possible de transporter
2-3 kilos sur 20-30 kilomètres. Il paraît très pertinent d'essayer de faire des voyages avec plusieurs
colis, de se débarrasser des plus lourds en premier quitte à faire un détour. On dit qu'on
optimise le chemin suivi par les drones ou plus exactement leur tournée. Ce n'est pas
par hasard si Google propose un challenge sur un sujet plus complexe que le
problème classique du :ref:`l-algo_tsp`. Les gagnants contribueront sans doute à la mise au point de
l'algorithme final probablement embauchés par Google. Un drone n'est pas tout-à-fait autonome.
Il est capable de prendre des décisions pour tout ce qui est urgent (les collisions, délivrer,
aller dans une direction) mais il ne sait pas optimiser une trajectoire sur une grande distance.
Les drones sont donc en permanence connectés et échangent une multitude d'information
avec un centre de pilotage.

**Les abeilles polinisent les fleurs. Avec un drone, on va savoir exactement combien. A quoi ça sert ?**

Dans la mesure où on conçoit des robots qui polinise à notre place, on peut avoir une idée assez précise
du nombre de plante dans une région donnée. Suivre l'évolution de cette information sur une période de temps
donne une idée de la santé de l'environnement. Le nombre de plante diminue-t-il, augmente-t-il ?
On peut également doter l'abeille d'autres capteurs pour mesurer la composition de l'air, la présence
de pesticides, l'humidité, la présence d'un sac plastique, le départ d'un feu, la radioactivité.
Cela permet d'établir une cartographie très précise d'un territoire et de suivre son évolution.
On dispose alors de mesures complètes et en temps réels. Le prochain camion de pompiers sera peut-être
un drone qui se déplace avec juste quelques litres d'eau pour éteindre un départ d'incendie.

**Un drone se déplace à l'aide de caméras qui filment. Que fait-on avec les images ?**

C'est une grande question. Les chercheurs ont besoin d'images pour construire ces drones.
Il est tout naturel de stocker des quantités d'images et continuer à les stocker
pour améliorer les capacités de reconnaissance. Les caméras vont tout filmer sans distinctions
et enregistrer des visages. Ces machines pour de nombreux objets électroniques sont les
témoins de votre vie. Ils sont infaillibles et tout le temps là. Il n'y a quasiment plus
d'instants où personne ne sait ce que vous faites alors que le secret est une composante
importante de notre société. Secret professionnel, secret médical, ces secrets ne s'accommodent
pas encore très bien avec le monde numérique qui garde une trace quasi indélébile et infaillible
de nos interactions avec lui.

**Un coup de vent a poussé un drone sur une voiture qui a eu un accident, qui est responsable ?**

C'est une question épineuse. La personne qui a conçu le drone l'optimise pour éviter à tout prix
cette situation. Elle n'est pas présente au moment de l'accident. Il existe des situations où l'auteur
est éloigné, un court-circuit électrique, une machine défectueuse. Dans la plupart des cas, on peut relier
la faute à l'auteur. C'est soit une faute de négligence, soit un acte intentionnel.
Dans les deux cas, cela repose sur le fait que l'utilisateur ou le concepteur sait anticiper ce que
la machine va faire dans telle ou telle situation et l'impact que cela aura sur lui-même ou d'autres personnes.
Un drone automatisé qui choisit son chemin n'est pas fiable à 100\%. Il prendra la bonne décision
dans la très grande majorité des cas. La probabilité qu'il se trompe est très très faible mais
elle existe si bien que la probabilité qu'il se trompe sur une grande durée est grande. Comme il n'y a pas de
pilote, il n'y a personne pour empêcher l'accident. Toutes les machines ont des pannes mais elles ne
sont a priori pas dangereuse comme celle-ci. Mais si on décide alors que le concepteur du drone n'est pas
responsable, qu'est-ce qui l'empêche alors ne pas faire autant attention qu'il le devrait à ce problème ?
Pour résumer, les drones livreurs de colis seraient les premières machines qui causeraient de façon
quasi certaine un nombre très limité d'accidents potentiellement graves **lors d'une utilisation normale**.
Ce dernier terme est important. Pourquoi se pose-t-on la question alors ? Parce que
le taux d'accidents par colis délivrés seraient sans doute comparable voire inférieur à celui d'un facteur.

**Que deviendra le facteur ?**

La première réponse est celle de la disparition du facteur. Et voilà une petite équipe de chercheurs
qui remplace un grand nombre de facteurs. On remplace un travail pas toujours très bien rémunéré,
pas toujours très bien valorisé, pas toujours passionnant non plus par un travail hautement qualifié,
souvent très intéressant, très créatif et beaucoup moins répétitif. Le métier de facteur est probablement
amené à disparaitre mais il faut se pencher un peu plus sur la personne qui occupe ce métier aujourd'hui.
Il n'y a pas de réponse simple et si elle existe, elle est sans doute collective.
Il y a aussi une certaine provocation dans le titre des articles
abordant le sujet
comme `« Le numérique s'impose partout, mais la croissance ne décollera pas » <http://www.latribune.fr/opinions/tribunes/le-numerique-s-impose-partout-mais-la-croissance-ne-decollera-pas-510227.html>`_
et il faut les lire. Aujourd'hui on ne sait pas. On sait que les métiers vont devenirs de moins en moins
répétitifs, de plus en plus créatifs, qu'il y en aura d'autres très mal payer et très répétitifs.
On sait aussi que l'école d'aujourd'hui n'arrive pas à former assez de monde pour ces
métiers créatifs. Cela ne veut pas dire qu'elle ne saura pas le faire. On évoque un changement
trop rapide pour la société. La société n'est pas toujours prête pour une innovation.

**Si vous deviez concevoir un drone qui se pilote lui-même, qui recruteriez-vous ?**

Beaucoup d'ingénieurs calés en électronique pour le drone lui-même, les communications,
en physique le vol, les capteurs et en informatique. L'ingénieur qui va apprendre à voir
à partir des objets doit connaître le machine learning. Celui qui optimise les parcours doit connaître
de nombreux algorithmes. Un dernier ingénieur devra intervenir pour implémenter le logiciel
qui va régir le drone car celui n'est pas un ordinateur comme les autres.
Enfin, on peut ajouter un informaticien pour un site web.
