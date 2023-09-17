import random

ACCOUNTS = [1,2,3,4,5,6,7,8,9]

hashtags = '#amazonfinds #amazonmusthaves #amazon #coolproducts #kitchen #gadgets #giftideas #homehacks #lifehacks #kitchenhacks #home #amazonfinds #amazonmusthaves #amazon #coolproducts #gadgets #giftideas #homehacks #lifehacks #home #kitchen #amazonfinds #amazonmusthaves #amazon #coolproducts #gadgets #giftideas #homehacks #lifehacks #techtok #home #tech'

HASHTAGS = lambda : ''.join([random.choice([i for i in hashtags.split(' ') if i]) for _ in range(3)])