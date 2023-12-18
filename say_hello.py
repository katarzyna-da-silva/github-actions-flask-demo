# Cette ligne définit une fonction appelée say_hello qui prend un argument appelé name. 
#  À l'intérieur de la chaîne, il y a un endroit pour insérer la valeur de la variable name. 
#Lorsque la fonction est appelée, la variable de nom sera remplacée 
#par la valeur réelle transmise à la fonction.
def say_hello(name):
    return f"Hello,GoodMorning, {name}!"

test_hello_world.py

# test 

from say_hello import say_hello

def test_say_hello():
    result = say_hello("")
    assert result == "Hello,GoodMorning, !"

def test_say_hello_with_empty_name():
    result = say_hello("")
    assert result == "Hello,GoodMorning, !"

def test_say_hello_with_unicode_name():
    result = say_hello("Matt")
    assert result == "Hello,GoodMorning, Matt!"

#Le terme « test unitaire » fait référence à un type de test en programmation informatique qui teste une partie unitaire du 
#code d'un programme, le plus souvent une seule fonction. Voici une explication de chaque test :

#test_say_hello() : Ce test vérifie si la fonction say_hello fonctionne correctement lors du passage d'une 
#chaîne vide en argument (nom). Le résultat devrait être "Bonjour, bonjour !".

#test_say_hello_with_empty_name() : Ce test vérifie également la réponse de la fonction à une chaîne vide comme argument. 
#Le résultat devrait être "Bonjour, bonjour !".

#test_say_hello_with_unicode_name() : Ce test vérifie si la fonction gère correctement l'argument unicode, en l'occurrence 
#le nom "Matt". Le résultat devrait être "Bonjour, bonjour, Matt !".

#Les tests unitaires constituent une partie importante des pratiques de développement car ils permettent de vérifier que les 
#éléments individuels du code fonctionnent comme prévu. Les tests unitaires sont 
#automatiquement exécutés pour détecter rapidement les erreurs de code et faciliter les modifications sans risque d'introduire de nouvelles erreurs.
