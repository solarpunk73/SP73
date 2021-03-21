#!/usr/bin/env python
# coding: utf-8

# # Notions utiles de l'Energie

# ## Introduction

# L'énergie est une constante. A notre échelle, tout du moins. Il n'y a donc que des vecteurs d'énergie et des échanges entre ces vecteurs. En fait, les physiciens ont remarqué que deux choses restaient constantes au cours des différentes transformations: la masse et l'énergie. Einstein démontra même la possibilité de passer de l'un à l'autre. 
# 
# On peut sentir instinctivement l'énergie en nous, les besoins nécesaires à la vie comme se manger correspondant à une recharge et permettant le mouvement du corps. Le feu fut le premier rapport de l'homme à l'utilisation de l'énergie.
# 
# Au niveau sociétal, notre niveau de consommation est proportionnel à notre consommation d'énergie. L'accès à l'énergie en devient donc un sujet politique et économique, allant jusqu'à sous-tendre l'invasion de pays entiers. De plus, les énergies fossiles, très denses, ont permis une rapide élévation du niveau de vie, par la transformation de l'énergie thermique en mouvement et en électricité, un vecteur d'énergie particulièrement maniable. Le soucis étant, bien sûr, le réchauffement climatique qui en découle et des inégalités sociales encore plus marquées; le capital corrompt. 
# 
# *La compréhension, la maitrise et la production de l'énergie par le peuple est donc un besoin émancipateur de nos sociétés modernes.*

# ![https://www.scientificamerican.com/article/earth-is-on-fire/](../images/Terre.PNG)

# Si l'on considère l'humain comme une machine thermique avec un rendement de 1, et qu'un humain ingère 2000 kcal/jour, notre consommation actuelle d'énergie s'éleverait à chaque français ayant 60 esclaves!

# ## Notion de puissance et d'énergie

# De manière générale, la puissance est de l'énergie par unité de temps; mathématiquement, $P=\frac{dE}{dt}$ avec **P** la puissance et **E** l'énergie. Les unités de la puissance sont les Watts(**W**); ceux de l'énergie sont beaucoup plus variés: Watt-Heure (**Wh**), Joules (**J**), calories (**cal**). Dans la vie courante, on utilise en général les *Wh* dans l'électricité (facture EDF,..), les Joules dans l'énergie cinétique(Air-Soft, voitures..) , et les calories dans l'énergie thermique (informations sur les paquets de nourriture, ..). 

# Il est possible de se souvenir du système de conversion d'une unité à l'autre en connaissant leur définition physique. En sciences, en France, on enseigne le [Système International](https://fr.wikipedia.org/wiki/Syst%C3%A8me_international_d%27unit%C3%A9s) (S.I.); 
# 1. Le Joule est donné comme l'unité de l'énergie, et tout "fonctionne bien": la formule de l'énergie cinétique, $E_c = \frac{1}{2}*m*v^2$, correspond au produit de la masse m (S.I.: *kg*), de la vitesse v (S.I.: *m/s*), mise au carré. En transposant cela aux unités, cela nous donne $ J = kg \times m^2/s^2 = kg \times m^2 \times s^{-2}$. De l'équation $P=\frac{dE}{dt}$, on tire $W = J/s = kg \times m^2 \times s^{-3}$.
# 2. Le Watt-Heure est le produit d'une puissance par le temps: $E=P\times \Delta t$ avec $\Delta t$ le temps. Comme cela est indiqué dans le nom, le temps est pris en heure. $1 Wh$ correspond à une puissance d'un Watt utilisé pendant 1h. Comme $1h = 3600s$, et que $W=J/s$, alors $J=W\times s$. Or $Wh = 3600 Ws = 3600 J$. 
# 3. La calorie fut historiquement une des premières mesures de l'énergie thermique. Cela correspond à l'énergie nécessaire pour élever d'un degré un litre d'eau: on peut souvent écrire $\Delta E = m C_p \Delta T$, avec **E** l'énergie, **m** la masse du système, $C_p$ la capacité thermique massique (J/kg.°C) et $\Delta T$ la variation de la température. Selon le matériau considéré, le $C_p$ varie; il correspond à l'inertie du matériau, ou encore à sa capacité de *stocker* l'énergie sous forme de température. Par exemple, les roches et autres céramiques sont en général dans un intervalle de $1200 \ J/kg.°C$ à $2400 \ J/kg.°C$; l'eau sous forme de  vapeur se situe vers $2000J/kg.°C$, alors que l'eau liquide vers $4187 \ J/kg.°C$. Par conséquent, une calorie correspond à $4187 J$

# ## L'énergie cinétique - $E_c$

# Le mouvement d'une masse est un vecteur d'énergie. Le mouvement de l'eau et du vent sont utilisés par l'homme (moulin, turbines, ..). L'électricité et la combustion ont contribué à l'essor technologique en permettant le mouvement d'une masse sans énergie humaine. 
# 
# L'équation définissant l'énergie cinétique d'une masse est: $E_c= \frac{1}{2} m v^2$, avec m la masse en kg, v la vitesse en m/s et $E_c$ l'énergie en Joules. 

# ### La vitesse

# La 3ème loi de Newton donne $m \vec{a} = \sum \vec{F}_{ext}$, avec $\vec{a}$ le vecteur accélération et $\vec{F}_{ext}$ l'ensemble des forces extérieures s'appliquant sur le système considéré. L'accélération est la dérivée de la vitesse, $\vec{a} = \frac{d\vec{v}}{dt}$.
# 
# En faisant le produit scalaire de la 3ème loi de Newton par $\vec{v}$, on obtient: $m\vec{v}.\frac{d\vec{v}}{dt} =\sum \vec{F}_{ext}.\vec{v}$. Or la dérivée de l'énergie cinétique s'écrit: $\frac{dE_c}{dt}  = \frac{1}{2}m \frac{d\vec{v}.\vec{v}}{dt} = m \vec{v}. \frac{d\vec{v}}{dt}$. D'où: $\frac{dE_c}{dt} = \sum \vec{F}_{ext}.\vec{v}$.
# 
# Or la dérivée de l'énergie est la puissance; on peut donc identifier la puissance instantanée exercée par les forces extérieures à $\vec{F}.\vec{v}$. Enfin, on voit la relation entre puissance en entrée et accélération. Pour une voiture, les forces majoritaires en exercice sont: les frottements (avec l'air et le sol), la gravité, et l'impulsion de la voiture. 

# **La voiture**
# 
# Une voiture thermique transforme l'énergie thermique issu de la combustion de l'essence/de l'éthanol pour la transformer en énergie cinétique. Elles présentent en général un rendement de 20%. Néanmoins, la masse déplacée pour un humain de 100kg face à une voiture de 1000kg, présente immédiatement les limites des voitures individuelles; surtout lorsque l'on considère le nombre moyen de passagers par voiture en France, de [1,7](https://www.futura-sciences.com/planete/questions-reponses/automobile-taux-occupation-voiture-1019/). 

# ![Transformation voiture](../images/transfoVoiture.PNG)

# **Le référentiel**
# 
# La vitesse dépend du référentiel: si l'on se déplace à la même vitesse qu'un autre usager de la route (ou de la piste cyclable), nos vitesses relatives sont nulles, et donc dans ce référentiel, l'énergie cinétique est nulle. Les objets ne bougeant pas dans le référentiel absolu, ce sont eux qui se retrouvent munis d'une énergie cinétique liée à une vitesse négative.

# ### L'inertie

# Le stockage de l'énergie cinétique se fait via la vitesse: un objet à une vitesse $\vec{v}$ possède une énergie cinétique (par rapport à son référentiel). C'est donc une forme de stockage; on parle d'inertie. Plus l'ojet sera gros, plus il aura stocké de l'énergie cinétique. La capacité de stockage de l'énergie cinétique est donc la masse. 
# 
# Le [volant d'inertie](https://fr.wikipedia.org/wiki/Volant_d%27inertie) est considéré comme une des possibilités de stockage de nos différents moyens de production de l'énergie: on fait tourner très vite une grosse masse, on stocke l'énergie en l'accélérant et on la décharge en le décélérant. 

# ![Volant](../images/volantInertie.png)

# ## L'Energie potentielle - $E_p$

# Tout comme l'énergie dans les différentes équations, l'énergie potentielle est une invention des physiciens permettant de quantifier la conservation de l'énergie. 
# 
# 
# : plus nous montons en hauteur, plus nous stockons de l'énergie cinétique en énergie potentielle; à la descente, nous la récupérons. En fait, cette notion d'énergie potentielle permet de mesurer l'énergie que nous pouvons récupérer de l'exercice des forces de gravité sur un objet. 
# 
# Si l'on reprend la 3ème loi de Newton, l'énergie potentielle apparaît comme une factorisation du produit $\vec{F}_{ext}.\vec{v}$: si l'on peut écrire cette quantité comme la dérivée d'une fonction par rapport au temps, cela permet, au niveau mathématique, d'intégrer facilement l'équation: $\frac{dE_C}{dt} = \sum \F_{ext}.\vec{v}$.
# Cela est possible pour une force **conservative**, dont c'est la définition. On écrit alors $\vec{F}_{ext}.\vec{v} $ comme $-\frac{dE_{P,ext}}{dt}$, ce qui donne: $\frac{dE_C}{dt} = - \sum \frac{dE_{P,ext}}{dt}$, d'où en posant l'énergie mécanique $E_M = E_C + \sum E_{P,ext}$
# 
# Stockage en mettant en hauteur. Notion inventé par les physiciens (tout comme les autres)

# ## L'énergie thermique - $U$

# Qu'est-ce que la température? On la ressent, la voit à la météo, mais la définition scientifique est toujours considérée comme complexe; on définit aujourd'hui la température comme $\frac{1}{T}= \frac{\partial S}{\partial E}$, avec S l'entropie et E l'énergie du système. Cette définition reste complexe, et demande la définition (et la compréhension) d'un certain nombre de concepts thermodynamiques. 
# 
# Ce que l'on peut dire avec les mains: la température correspond à l'agitation moléculaire (et donc à l'énergie cinétique moléculaire). Chauffer correspond donc à augmenter l'activité des molécules, refroidir à les ralentir. Cela se voit avec l'eau: gelée, ses molécules ne bougent presque plus les unes par rapport aux autres; liquide, le mouvement augmente; et gazeux, ces molécules s'agitent dans tous les sens. 
# 

# **Le référentiel**
# 
# L'énergie est une constante, et ne fait que se transférer; c'est d'ailleurs la seule façon de remarquer sa présence. Par conséquent, on ne peut la décrire que par rapport à un référentiel. On utilise fréquemment le 0 absolu, c'est-à-dire le 0 Kelvin, comme référence; mais chaque problème possède un référentiel plus adapté.
# 
# Si tous les objets sont à la même température (20°C, par exemple), il n'y aura pas de transferts d'énergie. Pour qu'il y ait transfert, il faut donc nécessairement une variation de la température. 

# ### L'inertie thermique

# La température d'un objet consiste donc en l'énergie thermique stockée en lui. La capacité de stockage de l'énergie thermique est mesurée expérimentalement; cette capacité de stockage varie en fonction de la température et de l'état (solide, liquide, gazeux) de la matière. Pour de petites variations de température, on utilise souvent la capacité thermique à pression constante, ou encore le "cépé": $C_p$. L'unité de ce paramètre sont les $J/kg.°C$. Cela correspond donc à l'énergie (**J**) par unité de masse (**kg**) et variation de température (**°C**).
# 
# Quelques exemples: faire monter un litre d'eau liquide de 1°C correspond à l'énergie d'une calorie, ou encore 4187 J; la roche a une capacité thermique variant de 1200 J/kg.°C à 2400 J/kg.°C .  
# 
# Une façon de stocker l'énergie thermique est donc de faire monter en température un liquide ou un solide; c'est ce qu'on appelle le stockage par chaleur sensible (la température variant). Par exemple, le ballon d'Eau Chaude Sanitaire dans les maisons, stocke de l'eau chaude à 60°C.

# ![Ballon d'ECS](../images/ballonECS.PNG)

# ## L'énergie chimique

# Drôle de vecteur d'énergie que la chimie: on peut stocker l'énergie sous forme d'un composant, tel l'hydrogène ($H_2$), l'essence, le bois, ... Une réaction chimique va demander de l'énergie, et la réaction inverse permettra de libérer cette énergie; très souvent, l'énergie stockée se libère sous forme de chaleur: combustion du bois ou de l'essence par exemple. On parle de réaction exothermique, qui libère de la chaleur. A l'inverse, une réaction demandant de la chaleur est appelé endothermique. C'est souvent comme cela que l'on stocke l'énergie sous forme chimique. 
# 
# 

# ## L'énergie électrique

# Des formules relient la puissance (P) et l'énergie électrique (E) à l'intensité (I) et la tension (U) qui traverse les systèmes électriques: $P=U \times I$, et donc si la puissance est constante $E=P \times t$ avec P la puissance et t le temps.
# 
# Il est donc possible d'estimer la puissance et l'énergie nécessaire à faire tourner différents appareils électriques. Par exemple, faire tourner 1 L.E.D de 5W pendant 1h prendra 5*Wh*; une brosse à dents à pile fonctionnant avec deux piles AAA (2 piles de 1.5V en série -> 3V) et nécessitant un courant en fonctionnement de 0.5*A* utilisera, pour fonctionner durant 1h, $E = P \times t = U \times I \times t = 3V * 0.5A *1h = 1.5Wh$. Un Excel, fait par G. Kamerling pour dimensionner l'électrification de son camion et présent dans le dossier GitHub accessible via le bouton en haut à droite donne un bon exemple de calculs de dimensionnement.

# #### Courant continu vs Courant alternatif

# Il est beaucoup plus simple de raisonner avec du [courant continue](https://fr.wikipedia.org/wiki/Courant_continu) que du [courant alternatif](https://fr.wikipedia.org/wiki/Courant_alternatif): dans le premier cas, la tension est constante aux bornes de l'appareil électrique, et l'intensité varie; dans le deuxième cas, il commence à y avoir des sinus partout. De plus, les panneaux photovoltaïques produisent du courant continu (CC); les batteries électriques prennent et délivrent du courant continu. Néanmoins, le réseau électrique et la majorité de nos outils utilisent du courant alternatif (230V, **50 Hz**). Mais néanmoins, une bonne partie des appareils électriques utilisent en réalité du courant continu et possèdent un dispositif électronique faisant la conversion. C'est le cas des lampes, des ordinateurs (chargeurs),..; ce n'est pas le cas des moteurs (machine à laver le linge,..). Les résistances fonctionnent avec les deux types (*?* à vérifier).
# 
# Notons que les turbines (à vapeur, à eau, ..) produisent du courant alternatif (ça tourne), de même que les éoliennes et autres hydroliennes; la majorité de nos modes de production consiste donc en du courant alternatif.
# 
# La conversion de l'un à l'autre est possible via de l'électronique: on parle d'un onduleur/alternateur de CC vers AC et de 

# ## La part des énergies dans le monde industriel

# ### Le cas de la France

# 
