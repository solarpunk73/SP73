#!/usr/bin/env python
# coding: utf-8

# # Solaire passif

# Le solaire passif est une solution à la problématique de chauffage. En effet, les apports du soleil sont immenses: une fenêtre plein sud, comme chacun le sait, permettra de se chauffer l'hiver. Il est néanmoins nécessaire de faire un paresoleil afin de ne pas chauffer en été. Cette dyssimétrie entre le besoin et la disponibilité de l'énergie implique une grande réflexion du bâtiment. De nombreux travaux sont menés à l'INES et au sein d'INES Formation, ces derniers étant bien plus à même de répondre à des questions précises sur le sujet.
# 
# Le SolarPunk est un mouvement d'imagination; nous souhaitons donc donner du rêve ici, car les possibilités sont grandes et fondamentalement intéressantes: la société a besoin d'un mythe, le SolarPunk est une des réponses!

# Nous allons ici partager et commenter un certain nombre de scan du livre **Le Guide de l'Energie Solaire**, de E. Mazria, publié en 1975. Des concepts très intéressants y sont décrits, ainsi que des solutions de calcul pour tout un chacun. Preuve, s'il en est, que tout est déjà réfléchi et calculé - il ne reste plus qu'une motivation politique (et donc sociétale) pour les mettre en place. Nous présentons ici quelques-uns de ces concepts.

# ## Organisation de l'espace de vie

# ```{margin} Organisation de la maison
# Une organisation logique permet un gain d'énergie solaire utile: situer les pièces de vie au sud, où le chauffage solaire est assuré en hiver, permet de diminuer la nécessité d'un chauffage d'appoint.
# ```

# ```{image} ../images/Guide/OrgMaison.jpg
# :alt: organisation de la maison
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Répartition des fenêtres
# Nous pouvons voir ici une idée de répartition des fenêtres, assurant un meilleur chauffage.
# ```

# ```{image} ../images/Guide/OrgFenetre.jpg
# :alt: organisation des fenetres
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ## Dissymétrie Hiver/Eté

# ```{margin} Elevation
# Le soleil change de hauteur dans le ciel, de par le mouvement de la Terre. Au solstice de printemps et d'automne, à midi heure solaire, il se trouve à un angle d'élevation égal à 90° - latitude. En France, c'est donc environ 45°. Il bougera ensuite, par rapport à cette position, de +23.5° (solstice d'été) à -23.5° (solstice d'hiver).
# ```

# ```{image} ../images/Guide/elevation.jpg
# :alt: Elevation
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Position dans le ciel
# Connaitre la position du soleil s'avère très pratique dans de nombreux cas (perdu dans la forêt, solaire passif, actif, ..). Voici un graphique de sa position et une façon utile de le présenter, entre azimuth et élévation.
# ```

# ```{image} ../images/Guide/PositionSoleil.jpg
# :alt: Position du Soleil
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Eté et hiver
# Il ne faut pas chauffer en été, c'est même plutôt l'inverse. Cette illustration montre comment le changement de position du soleil doit être utilisé et connu pour bien disposer ses claires-voies.
# ```

# ```{image} ../images/Guide/DyssimEteHiver.jpg
# :alt: Angles
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ## Réflecteurs et usages du toit

# ```{margin} Réflecteurs sur toit
# L'usage de ces réflecteurs est triple: en hiver, de jour, il permet de gagner de l'énergie solaire en entrée direct. En hiver, de nuit, il sert d'isolant; en été, de jour, il sert de protection solaire.
# ```

# ```{image} ../images/Guide/ReflToit.jpg
# :alt: Reflecteurs Toit
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Claires-voies et lanterneaus
# Apport direct par le toit; la claire-voie permet de gérer la différence été/hiver. Le lanterneau lui nécessite la disposition d'un protecteur solaire.
# ```

# ```{image} ../images/Guide/ClaireVoieLanterneau.jpg
# :alt: Claire voie et lanterneau
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Toits Bassins
# Mettre un bassin sur son toit est à bien réfléchir en amont! Mais les avantages sont non négligeables, de par l'inertie thermique très élevée de l'eau.
# ```

# ```{image} ../images/Guide/ToitBassinconcept.jpg
# :alt: Toit bassin concept
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Autres dispositions
# Il est possible de mettre le bassin en intérieur, et de le chauffer par une claire-voie. Une petite piscine serait-elle envisageable?
# ```

# ```{image} ../images/Guide/bassinToit.jpg
# :alt: Toit bassin 
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ## Mur d'eau & Inertie thermique

# ```{margin} Murs capteurs
# Les murs capteurs vont stocker l'énergie solaire, grâce à leur inertie thermique. Des calculs précis sont nécessaires, car il existe une taille optimale du mur, entre conduction et inertie.
# Les murs d'eau ont une très grande inertie: l'eau est le matériau avec la plus grande inertie par kilogrammes, $C_p = 4187 J/kg.°C$
# ```

# ```{image} ../images/Guide/MurCapteur.jpg
# :alt: Murs capteurs
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Chauffage
# Ici, le soleil chauffe un mur d'eau intérieur par le biais d'une claire-voie.
# ```

# ```{image} ../images/Guide/MurEauChauffe.jpg
# :alt: Mur d'eau en intérieur
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Stockage
# Il y a de nombreuses solutions de stockage par inertie thermique. en voici quelques-unes. en dehors du mur capteur/accumulateur, nous pouvons également voir un stockage actif: des galets, chauffés par le soleil, dont la chaleur est récupérée par l'utilisation d'un ventilateur.
# ```

# ```{image} ../images/Guide/StockageDirect.jpg
# :alt: Stocker
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ## Serres attenantes, enterrées

# Les serres permettent énormément de choses. Entre autre, une serre attenante permettra un chauffage partiel de la maison: moins efficace qu'une fenêtre pour chauffer la maison, mais avec un gain d'espace pour la pousse de végétaux. D'autant plus que la chauffe de la maison permettra de tenir la serre un peu plus chaude qu'isolée.

# ```{margin} Serre et inertie
# On peut voir ici une serre attenante, avec l'utilisation d'un système de stockage par galets et courant d'air.
# ```

# ```{image} ../images/Guide/StockageSerre.jpg
# :alt: Stockage Serre
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Serre enfouie
# On peut voir ici une serre enfouie côté nord, ce qui permet une isolation simple et rapide.
# ```

# ```{image} ../images/Guide/SerreEnfouie.jpg
# :alt: Serre Enfouie
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# ```{margin} Serre avec inertie
# Une serre avec de l'inertie n'aura pas besoin de stockage d'appoint. Voici une disposition possible.
# ```

# ```{image} ../images/Guide/SerreStockage.jpg
# :alt: Serre Stockante
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```

# In[ ]:




