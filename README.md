# Awale
Projet d'IA sur le jeu Awale

# Rules 
Il y a 16 trous, 8 par joueur Les trous sont numérotés de 1 à 16. On tourne dans le sens des aiguilles d'une montre : Le trou 1 suit le trou 16 dans le sens des aiguilles d'une montre. Le premier joueur a les trous impairs, le deuxième joueur a les trous pairs.

Il y a deux couleurs : rouge et bleu Au début il y a 2 graines de chaque couleur par trou.

-- Objet Le jeu commence avec 2+2 graines dans chaque trou. Le but du jeu est de capturer plus de graines que son adversaire. Comme il y a un nombre pair de graines, il est possible que le jeu se termine par un match nul, où chaque joueur a capturé 32 graines.

-- Semis Les joueurs déplacent les graines à tour de rôle. À son tour, un joueur choisit l'un des huit trous qu'il contrôle. Le joueur retire les graines de ce trou (voir ci-dessous pour la gestion des couleurs), et les distribue, en en déposant une dans les trous dans le sens des aiguilles d'une montre (c'est-à-dire dans un ordre non décroissant) à partir de ce trou, dans un processus appelé semis. Les déplacements se font en fonction des couleurs. D'abord une couleur est désignée et toutes les graines de cette couleur sont jouées, Si les graines sont rouges, alors elles sont distribuées dans chaque trou. Si les graines sont bleues, alors elles sont distribuées uniquement dans les trous de l'adversaire.

Les graines ne sont pas distribuées dans le trou tiré. Le trou de départ est toujours laissé vide ; s'il contenait 16 graines (ou plus), il est sauté, et la seizième graine est placée dans le trou suivant. Ainsi, un coup est exprimé par NC où N est le numéro du trou, C est la couleur qui est jouée Par exemple, 3R signifie que nous jouons les graines rouges du trou 3 (et seulement les rouges)

-- Capture La capture ne se produit que lorsqu'un joueur porte le nombre de trous à exactement deux ou trois graines (de n'importe quelle couleur). Il capture toujours les graines du trou correspondant, et éventuellement plus : Si l'avant-dernière graine a également amené un trou à deux ou trois graines, celles-ci sont également capturées, et ainsi de suite jusqu'à ce qu'un trou ne contenant pas deux ou trois graines soit atteint. Les graines capturées sont mises de côté. Affamer l'adversaire EST PERMIS Attention, il est autorisé à prendre les graines de son propre trou et les graines sont capturées indépendamment de leurs couleurs. Prendre toutes les graines de l'adversaire est autorisé. En cas d'affamage, toutes les graines sont capturées par le dernier joueur. Le jeu s'arrête lorsqu'il y a strictement moins de 8 graines sur le plateau. Dans ce cas, les graines restantes ne sont pas prises en compte.

-- Gagner La partie est terminée lorsqu'un joueur a capturé 33 graines ou plus, ou que chaque joueur a pris 32 graines (égalité), ou qu'il ne reste que strictement moins de 8 graines. Le gagnant est le joueur qui a plus de graines que son adversaire.

# Lancement du projet
Tout d'abord ouvrez le zip et dézipper le projet
Ensuite lancer cette commande dans le terminal à la racine du projet : 
```
python3 .\src\main.py
```
# Les fonctionnalités

Plusieurs fonctionnalités ont été effectués lors du projet : 
- L'implémentation des règles pour le "Sowing", "Capture".
- Jeu fonctionnel à 100%.
- Implémentation d'une IA (min-max).
- Affichage couleur des tours de jeu.

# Difficultés rencontrés

Nos principaux difficultés ont été sur deux points précis :
-La fonction harvest qui parle de la capture, elle a été difficile à implémenter car on devait gérer le fait qu on devait repartir à la fin du plateau lorsqu on était dans le premier trou. 
-Difficulté de passer de la théorie min-max à l'implémentation de l'algorithme min max 
