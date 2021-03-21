#!/usr/bin/env python
# coding: utf-8

# # Les différentes pertes optiques

# ## L'effet cosinus

# L'effet cosinus n'est pas à proprement parlé une perte. 

# ![http://www.powerfromthesun.net/Book/chapter10/chapter10.html](../images/CosineEffect.PNG)

# Cela traduit juste le fait qu'une surface ne reçoit que l'énergie qu'elle voit, et qu'il faut donc projeter l'aire du collecteur dans la direction du rayon. Cela peut se voir lorsque l'on penche sa main petit à petit en redirection du soleil: la lumière palit jusqu'à disparaître: on a dépassé les 90°, le côté de la main éclairé est passé dans l'ombre.

#  Soit alors $\vec{s}$ le vecteur solaire, càd le vecteur pointant vers le soleil. 
# 
# Soit $\vec{n}_P$ la normale au panneau/héliostat/là où arrive l'énergie solaire et $A_{col}$ la surface du collecteur. 
# 
# L'aire effective "vue par le soleil" est alors: $A_{eff}=A_{col} \times (\vec{s}.\vec{n}_P) = A_{col} \times \cos(\theta)$, avec $\theta$ l'angle entre le soleil et la normale au panneau.

# ## Mal viser

# Lorsque l'on utilise des miroirs, il est possible de mal viser. Cela est appelé le *spillage* en anglais. A une certaine distance, la taille de l'image renvoyée par le miroir grandie tant qu'il peut être impossible de toucher le récepteur.

# In[ ]:




