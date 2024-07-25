from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette import status
import uvicorn
from pydantic import BaseModel

import base64
from PIL import Image
from io import BytesIO
import numpy as np

import torch
import torchvision
import torchvision.transforms as transforms
from torchvision.transforms import InterpolationMode

import onnxruntime as ort
import subprocess

from ultralytics import YOLO
import cv2

import matplotlib.pyplot as plt

# IMGENET
class_dict = {0: 'tench, Tinca tinca',
 1: 'goldfish, Carassius auratus',
 2: 'great white shark, white shark, man-eater, man-eating shark, Carcharodon carcharias',
 3: 'tiger shark, Galeocerdo cuvieri',
 4: 'hammerhead, hammerhead shark',
 5: 'electric ray, crampfish, numbfish, torpedo',
 6: 'stingray',
 7: 'cock',
 8: 'hen',
 9: 'ostrich, Struthio camelus',
 10: 'brambling, Fringilla montifringilla',
 11: 'goldfinch, Carduelis carduelis',
 12: 'house finch, linnet, Carpodacus mexicanus',
 13: 'junco, snowbird',
 14: 'indigo bunting, indigo finch, indigo bird, Passerina cyanea',
 15: 'robin, American robin, Turdus migratorius',
 16: 'bulbul',
 17: 'jay',
 18: 'magpie',
 19: 'chickadee',
 20: 'water ouzel, dipper',
 21: 'kite',
 22: 'bald eagle, American eagle, Haliaeetus leucocephalus',
 23: 'vulture',
 24: 'great grey owl, great gray owl, Strix nebulosa',
 25: 'European fire salamander, Salamandra salamandra',
 26: 'common newt, Triturus vulgaris',
 27: 'eft',
 28: 'spotted salamander, Ambystoma maculatum',
 29: 'axolotl, mud puppy, Ambystoma mexicanum',
 30: 'bullfrog, Rana catesbeiana',
 31: 'tree frog, tree-frog',
 32: 'tailed frog, bell toad, ribbed toad, tailed toad, Ascaphus trui',
 33: 'loggerhead, loggerhead turtle, Caretta caretta',
 34: 'leatherback turtle, leatherback, leathery turtle, Dermochelys coriacea',
 35: 'mud turtle',
 36: 'terrapin',
 37: 'box turtle, box tortoise',
 38: 'banded gecko',
 39: 'common iguana, iguana, Iguana iguana',
 40: 'American chameleon, anole, Anolis carolinensis',
 41: 'whiptail, whiptail lizard',
 42: 'agama',
 43: 'frilled lizard, Chlamydosaurus kingi',
 44: 'alligator lizard',
 45: 'Gila monster, Heloderma suspectum',
 46: 'green lizard, Lacerta viridis',
 47: 'African chameleon, Chamaeleo chamaeleon',
 48: 'Komodo dragon, Komodo lizard, dragon lizard, giant lizard, Varanus komodoensis',
 49: 'African crocodile, Nile crocodile, Crocodylus niloticus',
 50: 'American alligator, Alligator mississipiensis',
 51: 'triceratops',
 52: 'thunder snake, worm snake, Carphophis amoenus',
 53: 'ringneck snake, ring-necked snake, ring snake',
 54: 'hognose snake, puff adder, sand viper',
 55: 'green snake, grass snake',
 56: 'king snake, kingsnake',
 57: 'garter snake, grass snake',
 58: 'water snake',
 59: 'vine snake',
 60: 'night snake, Hypsiglena torquata',
 61: 'boa constrictor, Constrictor constrictor',
 62: 'rock python, rock snake, Python sebae',
 63: 'Indian cobra, Naja naja',
 64: 'green mamba',
 65: 'sea snake',
 66: 'horned viper, cerastes, sand viper, horned asp, Cerastes cornutus',
 67: 'diamondback, diamondback rattlesnake, Crotalus adamanteus',
 68: 'sidewinder, horned rattlesnake, Crotalus cerastes',
 69: 'trilobite',
 70: 'harvestman, daddy longlegs, Phalangium opilio',
 71: 'scorpion',
 72: 'black and gold garden spider, Argiope aurantia',
 73: 'barn spider, Araneus cavaticus',
 74: 'garden spider, Aranea diademata',
 75: 'black widow, Latrodectus mactans',
 76: 'tarantula',
 77: 'wolf spider, hunting spider',
 78: 'tick',
 79: 'centipede',
 80: 'black grouse',
 81: 'ptarmigan',
 82: 'ruffed grouse, partridge, Bonasa umbellus',
 83: 'prairie chicken, prairie grouse, prairie fowl',
 84: 'peacock',
 85: 'quail',
 86: 'partridge',
 87: 'African grey, African gray, Psittacus erithacus',
 88: 'macaw',
 89: 'sulphur-crested cockatoo, Kakatoe galerita, Cacatua galerita',
 90: 'lorikeet',
 91: 'coucal',
 92: 'bee eater',
 93: 'hornbill',
 94: 'hummingbird',
 95: 'jacamar',
 96: 'toucan',
 97: 'drake',
 98: 'red-breasted merganser, Mergus serrator',
 99: 'goose',
 100: 'black swan, Cygnus atratus',
 101: 'tusker',
 102: 'echidna, spiny anteater, anteater',
 103: 'platypus, duckbill, duckbilled platypus, duck-billed platypus, Ornithorhynchus anatinus',
 104: 'wallaby, brush kangaroo',
 105: 'koala, koala bear, kangaroo bear, native bear, Phascolarctos cinereus',
 106: 'wombat',
 107: 'jellyfish',
 108: 'sea anemone, anemone',
 109: 'brain coral',
 110: 'flatworm, platyhelminth',
 111: 'nematode, nematode worm, roundworm',
 112: 'conch',
 113: 'snail',
 114: 'slug',
 115: 'sea slug, nudibranch',
 116: 'chiton, coat-of-mail shell, sea cradle, polyplacophore',
 117: 'chambered nautilus, pearly nautilus, nautilus',
 118: 'Dungeness crab, Cancer magister',
 119: 'rock crab, Cancer irroratus',
 120: 'fiddler crab',
 121: 'king crab, Alaska crab, Alaskan king crab, Alaska king crab, Paralithodes camtschatica',
 122: 'American lobster, Northern lobster, Maine lobster, Homarus americanus',
 123: 'spiny lobster, langouste, rock lobster, crawfish, crayfish, sea crawfish',
 124: 'crayfish, crawfish, crawdad, crawdaddy',
 125: 'hermit crab',
 126: 'isopod',
 127: 'white stork, Ciconia ciconia',
 128: 'black stork, Ciconia nigra',
 129: 'spoonbill',
 130: 'flamingo',
 131: 'little blue heron, Egretta caerulea',
 132: 'American egret, great white heron, Egretta albus',
 133: 'bittern',
 134: 'crane',
 135: 'limpkin, Aramus pictus',
 136: 'European gallinule, Porphyrio porphyrio',
 137: 'American coot, marsh hen, mud hen, water hen, Fulica americana',
 138: 'bustard',
 139: 'ruddy turnstone, Arenaria interpres',
 140: 'red-backed sandpiper, dunlin, Erolia alpina',
 141: 'redshank, Tringa totanus',
 142: 'dowitcher',
 143: 'oystercatcher, oyster catcher',
 144: 'pelican',
 145: 'king penguin, Aptenodytes patagonica',
 146: 'albatross, mollymawk',
 147: 'grey whale, gray whale, devilfish, Eschrichtius gibbosus, Eschrichtius robustus',
 148: 'killer whale, killer, orca, grampus, sea wolf, Orcinus orca',
 149: 'dugong, Dugong dugon',
 150: 'sea lion',
 151: 'Chihuahua',
 152: 'Japanese spaniel',
 153: 'Maltese dog, Maltese terrier, Maltese',
 154: 'Pekinese, Pekingese, Peke',
 155: 'Shih-Tzu',
 156: 'Blenheim spaniel',
 157: 'papillon',
 158: 'toy terrier',
 159: 'Rhodesian ridgeback',
 160: 'Afghan hound, Afghan',
 161: 'basset, basset hound',
 162: 'beagle',
 163: 'bloodhound, sleuthhound',
 164: 'bluetick',
 165: 'black-and-tan coonhound',
 166: 'Walker hound, Walker foxhound',
 167: 'English foxhound',
 168: 'redbone',
 169: 'borzoi, Russian wolfhound',
 170: 'Irish wolfhound',
 171: 'Italian greyhound',
 172: 'whippet',
 173: 'Ibizan hound, Ibizan Podenco',
 174: 'Norwegian elkhound, elkhound',
 175: 'otterhound, otter hound',
 176: 'Saluki, gazelle hound',
 177: 'Scottish deerhound, deerhound',
 178: 'Weimaraner',
 179: 'Staffordshire bullterrier, Staffordshire bull terrier',
 180: 'American Staffordshire terrier, Staffordshire terrier, American pit bull terrier, pit bull terrier',
 181: 'Bedlington terrier',
 182: 'Border terrier',
 183: 'Kerry blue terrier',
 184: 'Irish terrier',
 185: 'Norfolk terrier',
 186: 'Norwich terrier',
 187: 'Yorkshire terrier',
 188: 'wire-haired fox terrier',
 189: 'Lakeland terrier',
 190: 'Sealyham terrier, Sealyham',
 191: 'Airedale, Airedale terrier',
 192: 'cairn, cairn terrier',
 193: 'Australian terrier',
 194: 'Dandie Dinmont, Dandie Dinmont terrier',
 195: 'Boston bull, Boston terrier',
 196: 'miniature schnauzer',
 197: 'giant schnauzer',
 198: 'standard schnauzer',
 199: 'Scotch terrier, Scottish terrier, Scottie',
 200: 'Tibetan terrier, chrysanthemum dog',
 201: 'silky terrier, Sydney silky',
 202: 'soft-coated wheaten terrier',
 203: 'West Highland white terrier',
 204: 'Lhasa, Lhasa apso',
 205: 'flat-coated retriever',
 206: 'curly-coated retriever',
 207: 'golden retriever',
 208: 'Labrador retriever',
 209: 'Chesapeake Bay retriever',
 210: 'German short-haired pointer',
 211: 'vizsla, Hungarian pointer',
 212: 'English setter',
 213: 'Irish setter, red setter',
 214: 'Gordon setter',
 215: 'Brittany spaniel',
 216: 'clumber, clumber spaniel',
 217: 'English springer, English springer spaniel',
 218: 'Welsh springer spaniel',
 219: 'cocker spaniel, English cocker spaniel, cocker',
 220: 'Sussex spaniel',
 221: 'Irish water spaniel',
 222: 'kuvasz',
 223: 'schipperke',
 224: 'groenendael',
 225: 'malinois',
 226: 'briard',
 227: 'kelpie',
 228: 'komondor',
 229: 'Old English sheepdog, bobtail',
 230: 'Shetland sheepdog, Shetland sheep dog, Shetland',
 231: 'collie',
 232: 'Border collie',
 233: 'Bouvier des Flandres, Bouviers des Flandres',
 234: 'Rottweiler',
 235: 'German shepherd, German shepherd dog, German police dog, alsatian',
 236: 'Doberman, Doberman pinscher',
 237: 'miniature pinscher',
 238: 'Greater Swiss Mountain dog',
 239: 'Bernese mountain dog',
 240: 'Appenzeller',
 241: 'EntleBucher',
 242: 'boxer',
 243: 'bull mastiff',
 244: 'Tibetan mastiff',
 245: 'French bulldog',
 246: 'Great Dane',
 247: 'Saint Bernard, St Bernard',
 248: 'Eskimo dog, husky',
 249: 'malamute, malemute, Alaskan malamute',
 250: 'Siberian husky',
 251: 'dalmatian, coach dog, carriage dog',
 252: 'affenpinscher, monkey pinscher, monkey dog',
 253: 'basenji',
 254: 'pug, pug-dog',
 255: 'Leonberg',
 256: 'Newfoundland, Newfoundland dog',
 257: 'Great Pyrenees',
 258: 'Samoyed, Samoyede',
 259: 'Pomeranian',
 260: 'chow, chow chow',
 261: 'keeshond',
 262: 'Brabancon griffon',
 263: 'Pembroke, Pembroke Welsh corgi',
 264: 'Cardigan, Cardigan Welsh corgi',
 265: 'toy poodle',
 266: 'miniature poodle',
 267: 'standard poodle',
 268: 'Mexican hairless',
 269: 'timber wolf, grey wolf, gray wolf, Canis lupus',
 270: 'white wolf, Arctic wolf, Canis lupus tundrarum',
 271: 'red wolf, maned wolf, Canis rufus, Canis niger',
 272: 'coyote, prairie wolf, brush wolf, Canis latrans',
 273: 'dingo, warrigal, warragal, Canis dingo',
 274: 'dhole, Cuon alpinus',
 275: 'African hunting dog, hyena dog, Cape hunting dog, Lycaon pictus',
 276: 'hyena, hyaena',
 277: 'red fox, Vulpes vulpes',
 278: 'kit fox, Vulpes macrotis',
 279: 'Arctic fox, white fox, Alopex lagopus',
 280: 'grey fox, gray fox, Urocyon cinereoargenteus',
 281: 'tabby, tabby cat',
 282: 'tiger cat',
 283: 'Persian cat',
 284: 'Siamese cat, Siamese',
 285: 'Egyptian cat',
 286: 'cougar, puma, catamount, mountain lion, painter, panther, Felis concolor',
 287: 'lynx, catamount',
 288: 'leopard, Panthera pardus',
 289: 'snow leopard, ounce, Panthera uncia',
 290: 'jaguar, panther, Panthera onca, Felis onca',
 291: 'lion, king of beasts, Panthera leo',
 292: 'tiger, Panthera tigris',
 293: 'cheetah, chetah, Acinonyx jubatus',
 294: 'brown bear, bruin, Ursus arctos',
 295: 'American black bear, black bear, Ursus americanus, Euarctos americanus',
 296: 'ice bear, polar bear, Ursus Maritimus, Thalarctos maritimus',
 297: 'sloth bear, Melursus ursinus, Ursus ursinus',
 298: 'mongoose',
 299: 'meerkat, mierkat',
 300: 'tiger beetle',
 301: 'ladybug, ladybeetle, lady beetle, ladybird, ladybird beetle',
 302: 'ground beetle, carabid beetle',
 303: 'long-horned beetle, longicorn, longicorn beetle',
 304: 'leaf beetle, chrysomelid',
 305: 'dung beetle',
 306: 'rhinoceros beetle',
 307: 'weevil',
 308: 'fly',
 309: 'bee',
 310: 'ant, emmet, pismire',
 311: 'grasshopper, hopper',
 312: 'cricket',
 313: 'walking stick, walkingstick, stick insect',
 314: 'cockroach, roach',
 315: 'mantis, mantid',
 316: 'cicada, cicala',
 317: 'leafhopper',
 318: 'lacewing, lacewing fly',
 319: "dragonfly, darning needle, devil's darning needle, sewing needle, snake feeder, snake doctor, mosquito hawk, skeeter hawk",
 320: 'damselfly',
 321: 'admiral',
 322: 'ringlet, ringlet butterfly',
 323: 'monarch, monarch butterfly, milkweed butterfly, Danaus plexippus',
 324: 'cabbage butterfly',
 325: 'sulphur butterfly, sulfur butterfly',
 326: 'lycaenid, lycaenid butterfly',
 327: 'starfish, sea star',
 328: 'sea urchin',
 329: 'sea cucumber, holothurian',
 330: 'wood rabbit, cottontail, cottontail rabbit',
 331: 'hare',
 332: 'Angora, Angora rabbit',
 333: 'hamster',
 334: 'porcupine, hedgehog',
 335: 'fox squirrel, eastern fox squirrel, Sciurus niger',
 336: 'marmot',
 337: 'beaver',
 338: 'guinea pig, Cavia cobaya',
 339: 'sorrel',
 340: 'zebra',
 341: 'hog, pig, grunter, squealer, Sus scrofa',
 342: 'wild boar, boar, Sus scrofa',
 343: 'warthog',
 344: 'hippopotamus, hippo, river horse, Hippopotamus amphibius',
 345: 'ox',
 346: 'water buffalo, water ox, Asiatic buffalo, Bubalus bubalis',
 347: 'bison',
 348: 'ram, tup',
 349: 'bighorn, bighorn sheep, cimarron, Rocky Mountain bighorn, Rocky Mountain sheep, Ovis canadensis',
 350: 'ibex, Capra ibex',
 351: 'hartebeest',
 352: 'impala, Aepyceros melampus',
 353: 'gazelle',
 354: 'Arabian camel, dromedary, Camelus dromedarius',
 355: 'llama',
 356: 'weasel',
 357: 'mink',
 358: 'polecat, fitch, foulmart, foumart, Mustela putorius',
 359: 'black-footed ferret, ferret, Mustela nigripes',
 360: 'otter',
 361: 'skunk, polecat, wood pussy',
 362: 'badger',
 363: 'armadillo',
 364: 'three-toed sloth, ai, Bradypus tridactylus',
 365: 'orangutan, orang, orangutang, Pongo pygmaeus',
 366: 'gorilla, Gorilla gorilla',
 367: 'chimpanzee, chimp, Pan troglodytes',
 368: 'gibbon, Hylobates lar',
 369: 'siamang, Hylobates syndactylus, Symphalangus syndactylus',
 370: 'guenon, guenon monkey',
 371: 'patas, hussar monkey, Erythrocebus patas',
 372: 'baboon',
 373: 'macaque',
 374: 'langur',
 375: 'colobus, colobus monkey',
 376: 'proboscis monkey, Nasalis larvatus',
 377: 'marmoset',
 378: 'capuchin, ringtail, Cebus capucinus',
 379: 'howler monkey, howler',
 380: 'titi, titi monkey',
 381: 'spider monkey, Ateles geoffroyi',
 382: 'squirrel monkey, Saimiri sciureus',
 383: 'Madagascar cat, ring-tailed lemur, Lemur catta',
 384: 'indri, indris, Indri indri, Indri brevicaudatus',
 385: 'Indian elephant, Elephas maximus',
 386: 'African elephant, Loxodonta africana',
 387: 'lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens',
 388: 'giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca',
 389: 'barracouta, snoek',
 390: 'eel',
 391: 'coho, cohoe, coho salmon, blue jack, silver salmon, Oncorhynchus kisutch',
 392: 'rock beauty, Holocanthus tricolor',
 393: 'anemone fish',
 394: 'sturgeon',
 395: 'gar, garfish, garpike, billfish, Lepisosteus osseus',
 396: 'lionfish',
 397: 'puffer, pufferfish, blowfish, globefish',
 398: 'abacus',
 399: 'abaya',
 400: "academic gown, academic robe, judge's robe",
 401: 'accordion, piano accordion, squeeze box',
 402: 'acoustic guitar',
 403: 'aircraft carrier, carrier, flattop, attack aircraft carrier',
 404: 'airliner',
 405: 'airship, dirigible',
 406: 'altar',
 407: 'ambulance',
 408: 'amphibian, amphibious vehicle',
 409: 'analog clock',
 410: 'apiary, bee house',
 411: 'apron',
 412: 'ashcan, trash can, garbage can, wastebin, ash bin, ash-bin, ashbin, dustbin, trash barrel, trash bin',
 413: 'assault rifle, assault gun',
 414: 'backpack, back pack, knapsack, packsack, rucksack, haversack',
 415: 'bakery, bakeshop, bakehouse',
 416: 'balance beam, beam',
 417: 'balloon',
 418: 'ballpoint, ballpoint pen, ballpen, Biro',
 419: 'Band Aid',
 420: 'banjo',
 421: 'bannister, banister, balustrade, balusters, handrail',
 422: 'barbell',
 423: 'barber chair',
 424: 'barbershop',
 425: 'barn',
 426: 'barometer',
 427: 'barrel, cask',
 428: 'barrow, garden cart, lawn cart, wheelbarrow',
 429: 'baseball',
 430: 'basketball',
 431: 'bassinet',
 432: 'bassoon',
 433: 'bathing cap, swimming cap',
 434: 'bath towel',
 435: 'bathtub, bathing tub, bath, tub',
 436: 'beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon',
 437: 'beacon, lighthouse, beacon light, pharos',
 438: 'beaker',
 439: 'bearskin, busby, shako',
 440: 'beer bottle',
 441: 'beer glass',
 442: 'bell cote, bell cot',
 443: 'bib',
 444: 'bicycle-built-for-two, tandem bicycle, tandem',
 445: 'bikini, two-piece',
 446: 'binder, ring-binder',
 447: 'binoculars, field glasses, opera glasses',
 448: 'birdhouse',
 449: 'boathouse',
 450: 'bobsled, bobsleigh, bob',
 451: 'bolo tie, bolo, bola tie, bola',
 452: 'bonnet, poke bonnet',
 453: 'bookcase',
 454: 'bookshop, bookstore, bookstall',
 455: 'bottlecap',
 456: 'bow',
 457: 'bow tie, bow-tie, bowtie',
 458: 'brass, memorial tablet, plaque',
 459: 'brassiere, bra, bandeau',
 460: 'breakwater, groin, groyne, mole, bulwark, seawall, jetty',
 461: 'breastplate, aegis, egis',
 462: 'broom',
 463: 'bucket, pail',
 464: 'buckle',
 465: 'bulletproof vest',
 466: 'bullet train, bullet',
 467: 'butcher shop, meat market',
 468: 'cab, hack, taxi, taxicab',
 469: 'caldron, cauldron',
 470: 'candle, taper, wax light',
 471: 'cannon',
 472: 'canoe',
 473: 'can opener, tin opener',
 474: 'cardigan',
 475: 'car mirror',
 476: 'carousel, carrousel, merry-go-round, roundabout, whirligig',
 477: "carpenter's kit, tool kit",
 478: 'carton',
 479: 'car wheel',
 480: 'cash machine, cash dispenser, automated teller machine, automatic teller machine, automated teller, automatic teller, ATM',
 481: 'cassette',
 482: 'cassette player',
 483: 'castle',
 484: 'catamaran',
 485: 'CD player',
 486: 'cello, violoncello',
 487: 'cellular telephone, cellular phone, cellphone, cell, mobile phone',
 488: 'chain',
 489: 'chainlink fence',
 490: 'chain mail, ring mail, mail, chain armor, chain armour, ring armor, ring armour',
 491: 'chain saw, chainsaw',
 492: 'chest',
 493: 'chiffonier, commode',
 494: 'chime, bell, gong',
 495: 'china cabinet, china closet',
 496: 'Christmas stocking',
 497: 'church, church building',
 498: 'cinema, movie theater, movie theatre, movie house, picture palace',
 499: 'cleaver, meat cleaver, chopper',
 500: 'cliff dwelling',
 501: 'cloak',
 502: 'clog, geta, patten, sabot',
 503: 'cocktail shaker',
 504: 'coffee mug',
 505: 'coffeepot',
 506: 'coil, spiral, volute, whorl, helix',
 507: 'combination lock',
 508: 'computer keyboard, keypad',
 509: 'confectionery, confectionary, candy store',
 510: 'container ship, containership, container vessel',
 511: 'convertible',
 512: 'corkscrew, bottle screw',
 513: 'cornet, horn, trumpet, trump',
 514: 'cowboy boot',
 515: 'cowboy hat, ten-gallon hat',
 516: 'cradle',
 517: 'crane',
 518: 'crash helmet',
 519: 'crate',
 520: 'crib, cot',
 521: 'Crock Pot',
 522: 'croquet ball',
 523: 'crutch',
 524: 'cuirass',
 525: 'dam, dike, dyke',
 526: 'desk',
 527: 'desktop computer',
 528: 'dial telephone, dial phone',
 529: 'diaper, nappy, napkin',
 530: 'digital clock',
 531: 'digital watch',
 532: 'dining table, board',
 533: 'dishrag, dishcloth',
 534: 'dishwasher, dish washer, dishwashing machine',
 535: 'disk brake, disc brake',
 536: 'dock, dockage, docking facility',
 537: 'dogsled, dog sled, dog sleigh',
 538: 'dome',
 539: 'doormat, welcome mat',
 540: 'drilling platform, offshore rig',
 541: 'drum, membranophone, tympan',
 542: 'drumstick',
 543: 'dumbbell',
 544: 'Dutch oven',
 545: 'electric fan, blower',
 546: 'electric guitar',
 547: 'electric locomotive',
 548: 'entertainment center',
 549: 'envelope',
 550: 'espresso maker',
 551: 'face powder',
 552: 'feather boa, boa',
 553: 'file, file cabinet, filing cabinet',
 554: 'fireboat',
 555: 'fire engine, fire truck',
 556: 'fire screen, fireguard',
 557: 'flagpole, flagstaff',
 558: 'flute, transverse flute',
 559: 'folding chair',
 560: 'football helmet',
 561: 'forklift',
 562: 'fountain',
 563: 'fountain pen',
 564: 'four-poster',
 565: 'freight car',
 566: 'French horn, horn',
 567: 'frying pan, frypan, skillet',
 568: 'fur coat',
 569: 'garbage truck, dustcart',
 570: 'gasmask, respirator, gas helmet',
 571: 'gas pump, gasoline pump, petrol pump, island dispenser',
 572: 'goblet',
 573: 'go-kart',
 574: 'golf ball',
 575: 'golfcart, golf cart',
 576: 'gondola',
 577: 'gong, tam-tam',
 578: 'gown',
 579: 'grand piano, grand',
 580: 'greenhouse, nursery, glasshouse',
 581: 'grille, radiator grille',
 582: 'grocery store, grocery, food market, market',
 583: 'guillotine',
 584: 'hair slide',
 585: 'hair spray',
 586: 'half track',
 587: 'hammer',
 588: 'hamper',
 589: 'hand blower, blow dryer, blow drier, hair dryer, hair drier',
 590: 'hand-held computer, hand-held microcomputer',
 591: 'handkerchief, hankie, hanky, hankey',
 592: 'hard disc, hard disk, fixed disk',
 593: 'harmonica, mouth organ, harp, mouth harp',
 594: 'harp',
 595: 'harvester, reaper',
 596: 'hatchet',
 597: 'holster',
 598: 'home theater, home theatre',
 599: 'honeycomb',
 600: 'hook, claw',
 601: 'hoopskirt, crinoline',
 602: 'horizontal bar, high bar',
 603: 'horse cart, horse-cart',
 604: 'hourglass',
 605: 'iPod',
 606: 'iron, smoothing iron',
 607: "jack-o'-lantern",
 608: 'jean, blue jean, denim',
 609: 'jeep, landrover',
 610: 'jersey, T-shirt, tee shirt',
 611: 'jigsaw puzzle',
 612: 'jinrikisha, ricksha, rickshaw',
 613: 'joystick',
 614: 'kimono',
 615: 'knee pad',
 616: 'knot',
 617: 'lab coat, laboratory coat',
 618: 'ladle',
 619: 'lampshade, lamp shade',
 620: 'laptop, laptop computer',
 621: 'lawn mower, mower',
 622: 'lens cap, lens cover',
 623: 'letter opener, paper knife, paperknife',
 624: 'library',
 625: 'lifeboat',
 626: 'lighter, light, igniter, ignitor',
 627: 'limousine, limo',
 628: 'liner, ocean liner',
 629: 'lipstick, lip rouge',
 630: 'Loafer',
 631: 'lotion',
 632: 'loudspeaker, speaker, speaker unit, loudspeaker system, speaker system',
 633: "loupe, jeweler's loupe",
 634: 'lumbermill, sawmill',
 635: 'magnetic compass',
 636: 'mailbag, postbag',
 637: 'mailbox, letter box',
 638: 'maillot',
 639: 'maillot, tank suit',
 640: 'manhole cover',
 641: 'maraca',
 642: 'marimba, xylophone',
 643: 'mask',
 644: 'matchstick',
 645: 'maypole',
 646: 'maze, labyrinth',
 647: 'measuring cup',
 648: 'medicine chest, medicine cabinet',
 649: 'megalith, megalithic structure',
 650: 'microphone, mike',
 651: 'microwave, microwave oven',
 652: 'military uniform',
 653: 'milk can',
 654: 'minibus',
 655: 'miniskirt, mini',
 656: 'minivan',
 657: 'missile',
 658: 'mitten',
 659: 'mixing bowl',
 660: 'mobile home, manufactured home',
 661: 'Model T',
 662: 'modem',
 663: 'monastery',
 664: 'monitor',
 665: 'moped',
 666: 'mortar',
 667: 'mortarboard',
 668: 'mosque',
 669: 'mosquito net',
 670: 'motor scooter, scooter',
 671: 'mountain bike, all-terrain bike, off-roader',
 672: 'mountain tent',
 673: 'mouse, computer mouse',
 674: 'mousetrap',
 675: 'moving van',
 676: 'muzzle',
 677: 'nail',
 678: 'neck brace',
 679: 'necklace',
 680: 'nipple',
 681: 'notebook, notebook computer',
 682: 'obelisk',
 683: 'oboe, hautboy, hautbois',
 684: 'ocarina, sweet potato',
 685: 'odometer, hodometer, mileometer, milometer',
 686: 'oil filter',
 687: 'organ, pipe organ',
 688: 'oscilloscope, scope, cathode-ray oscilloscope, CRO',
 689: 'overskirt',
 690: 'oxcart',
 691: 'oxygen mask',
 692: 'packet',
 693: 'paddle, boat paddle',
 694: 'paddlewheel, paddle wheel',
 695: 'padlock',
 696: 'paintbrush',
 697: "pajama, pyjama, pj's, jammies",
 698: 'palace',
 699: 'panpipe, pandean pipe, syrinx',
 700: 'paper towel',
 701: 'parachute, chute',
 702: 'parallel bars, bars',
 703: 'park bench',
 704: 'parking meter',
 705: 'passenger car, coach, carriage',
 706: 'patio, terrace',
 707: 'pay-phone, pay-station',
 708: 'pedestal, plinth, footstall',
 709: 'pencil box, pencil case',
 710: 'pencil sharpener',
 711: 'perfume, essence',
 712: 'Petri dish',
 713: 'photocopier',
 714: 'pick, plectrum, plectron',
 715: 'pickelhaube',
 716: 'picket fence, paling',
 717: 'pickup, pickup truck',
 718: 'pier',
 719: 'piggy bank, penny bank',
 720: 'pill bottle',
 721: 'pillow',
 722: 'ping-pong ball',
 723: 'pinwheel',
 724: 'pirate, pirate ship',
 725: 'pitcher, ewer',
 726: "plane, carpenter's plane, woodworking plane",
 727: 'planetarium',
 728: 'plastic bag',
 729: 'plate rack',
 730: 'plow, plough',
 731: "plunger, plumber's helper",
 732: 'Polaroid camera, Polaroid Land camera',
 733: 'pole',
 734: 'police van, police wagon, paddy wagon, patrol wagon, wagon, black Maria',
 735: 'poncho',
 736: 'pool table, billiard table, snooker table',
 737: 'pop bottle, soda bottle',
 738: 'pot, flowerpot',
 739: "potter's wheel",
 740: 'power drill',
 741: 'prayer rug, prayer mat',
 742: 'printer',
 743: 'prison, prison house',
 744: 'projectile, missile',
 745: 'projector',
 746: 'puck, hockey puck',
 747: 'punching bag, punch bag, punching ball, punchball',
 748: 'purse',
 749: 'quill, quill pen',
 750: 'quilt, comforter, comfort, puff',
 751: 'racer, race car, racing car',
 752: 'racket, racquet',
 753: 'radiator',
 754: 'radio, wireless',
 755: 'radio telescope, radio reflector',
 756: 'rain barrel',
 757: 'recreational vehicle, RV, R.V.',
 758: 'reel',
 759: 'reflex camera',
 760: 'refrigerator, icebox',
 761: 'remote control, remote',
 762: 'restaurant, eating house, eating place, eatery',
 763: 'revolver, six-gun, six-shooter',
 764: 'rifle',
 765: 'rocking chair, rocker',
 766: 'rotisserie',
 767: 'rubber eraser, rubber, pencil eraser',
 768: 'rugby ball',
 769: 'rule, ruler',
 770: 'running shoe',
 771: 'safe',
 772: 'safety pin',
 773: 'saltshaker, salt shaker',
 774: 'sandal',
 775: 'sarong',
 776: 'sax, saxophone',
 777: 'scabbard',
 778: 'scale, weighing machine',
 779: 'school bus',
 780: 'schooner',
 781: 'scoreboard',
 782: 'screen, CRT screen',
 783: 'screw',
 784: 'screwdriver',
 785: 'seat belt, seatbelt',
 786: 'sewing machine',
 787: 'shield, buckler',
 788: 'shoe shop, shoe-shop, shoe store',
 789: 'shoji',
 790: 'shopping basket',
 791: 'shopping cart',
 792: 'shovel',
 793: 'shower cap',
 794: 'shower curtain',
 795: 'ski',
 796: 'ski mask',
 797: 'sleeping bag',
 798: 'slide rule, slipstick',
 799: 'sliding door',
 800: 'slot, one-armed bandit',
 801: 'snorkel',
 802: 'snowmobile',
 803: 'snowplow, snowplough',
 804: 'soap dispenser',
 805: 'soccer ball',
 806: 'sock',
 807: 'solar dish, solar collector, solar furnace',
 808: 'sombrero',
 809: 'soup bowl',
 810: 'space bar',
 811: 'space heater',
 812: 'space shuttle',
 813: 'spatula',
 814: 'speedboat',
 815: "spider web, spider's web",
 816: 'spindle',
 817: 'sports car, sport car',
 818: 'spotlight, spot',
 819: 'stage',
 820: 'steam locomotive',
 821: 'steel arch bridge',
 822: 'steel drum',
 823: 'stethoscope',
 824: 'stole',
 825: 'stone wall',
 826: 'stopwatch, stop watch',
 827: 'stove',
 828: 'strainer',
 829: 'streetcar, tram, tramcar, trolley, trolley car',
 830: 'stretcher',
 831: 'studio couch, day bed',
 832: 'stupa, tope',
 833: 'submarine, pigboat, sub, U-boat',
 834: 'suit, suit of clothes',
 835: 'sundial',
 836: 'sunglass',
 837: 'sunglasses, dark glasses, shades',
 838: 'sunscreen, sunblock, sun blocker',
 839: 'suspension bridge',
 840: 'swab, swob, mop',
 841: 'sweatshirt',
 842: 'swimming trunks, bathing trunks',
 843: 'swing',
 844: 'switch, electric switch, electrical switch',
 845: 'syringe',
 846: 'table lamp',
 847: 'tank, army tank, armored combat vehicle, armoured combat vehicle',
 848: 'tape player',
 849: 'teapot',
 850: 'teddy, teddy bear',
 851: 'television, television system',
 852: 'tennis ball',
 853: 'thatch, thatched roof',
 854: 'theater curtain, theatre curtain',
 855: 'thimble',
 856: 'thresher, thrasher, threshing machine',
 857: 'throne',
 858: 'tile roof',
 859: 'toaster',
 860: 'tobacco shop, tobacconist shop, tobacconist',
 861: 'toilet seat',
 862: 'torch',
 863: 'totem pole',
 864: 'tow truck, tow car, wrecker',
 865: 'toyshop',
 866: 'tractor',
 867: 'trailer truck, tractor trailer, trucking rig, rig, articulated lorry, semi',
 868: 'tray',
 869: 'trench coat',
 870: 'tricycle, trike, velocipede',
 871: 'trimaran',
 872: 'tripod',
 873: 'triumphal arch',
 874: 'trolleybus, trolley coach, trackless trolley',
 875: 'trombone',
 876: 'tub, vat',
 877: 'turnstile',
 878: 'typewriter keyboard',
 879: 'umbrella',
 880: 'unicycle, monocycle',
 881: 'upright, upright piano',
 882: 'vacuum, vacuum cleaner',
 883: 'vase',
 884: 'vault',
 885: 'velvet',
 886: 'vending machine',
 887: 'vestment',
 888: 'viaduct',
 889: 'violin, fiddle',
 890: 'volleyball',
 891: 'waffle iron',
 892: 'wall clock',
 893: 'wallet, billfold, notecase, pocketbook',
 894: 'wardrobe, closet, press',
 895: 'warplane, military plane',
 896: 'washbasin, handbasin, washbowl, lavabo, wash-hand basin',
 897: 'washer, automatic washer, washing machine',
 898: 'water bottle',
 899: 'water jug',
 900: 'water tower',
 901: 'whiskey jug',
 902: 'whistle',
 903: 'wig',
 904: 'window screen',
 905: 'window shade',
 906: 'Windsor tie',
 907: 'wine bottle',
 908: 'wing',
 909: 'wok',
 910: 'wooden spoon',
 911: 'wool, woolen, woollen',
 912: 'worm fence, snake fence, snake-rail fence, Virginia fence',
 913: 'wreck',
 914: 'yawl',
 915: 'yurt',
 916: 'web site, website, internet site, site',
 917: 'comic book',
 918: 'crossword puzzle, crossword',
 919: 'street sign',
 920: 'traffic light, traffic signal, stoplight',
 921: 'book jacket, dust cover, dust jacket, dust wrapper',
 922: 'menu',
 923: 'plate',
 924: 'guacamole',
 925: 'consomme',
 926: 'hot pot, hotpot',
 927: 'trifle',
 928: 'ice cream, icecream',
 929: 'ice lolly, lolly, lollipop, popsicle',
 930: 'French loaf',
 931: 'bagel, beigel',
 932: 'pretzel',
 933: 'cheeseburger',
 934: 'hotdog, hot dog, red hot',
 935: 'mashed potato',
 936: 'head cabbage',
 937: 'broccoli',
 938: 'cauliflower',
 939: 'zucchini, courgette',
 940: 'spaghetti squash',
 941: 'acorn squash',
 942: 'butternut squash',
 943: 'cucumber, cuke',
 944: 'artichoke, globe artichoke',
 945: 'bell pepper',
 946: 'cardoon',
 947: 'mushroom',
 948: 'Granny Smith',
 949: 'strawberry',
 950: 'orange',
 951: 'lemon',
 952: 'fig',
 953: 'pineapple, ananas',
 954: 'banana',
 955: 'jackfruit, jak, jack',
 956: 'custard apple',
 957: 'pomegranate',
 958: 'hay',
 959: 'carbonara',
 960: 'chocolate sauce, chocolate syrup',
 961: 'dough',
 962: 'meat loaf, meatloaf',
 963: 'pizza, pizza pie',
 964: 'potpie',
 965: 'burrito',
 966: 'red wine',
 967: 'espresso',
 968: 'cup',
 969: 'eggnog',
 970: 'alp',
 971: 'bubble',
 972: 'cliff, drop, drop-off',
 973: 'coral reef',
 974: 'geyser',
 975: 'lakeside, lakeshore',
 976: 'promontory, headland, head, foreland',
 977: 'sandbar, sand bar',
 978: 'seashore, coast, seacoast, sea-coast',
 979: 'valley, vale',
 980: 'volcano',
 981: 'ballplayer, baseball player',
 982: 'groom, bridegroom',
 983: 'scuba diver',
 984: 'rapeseed',
 985: 'daisy',
 986: "yellow lady's slipper, yellow lady-slipper, Cypripedium calceolus, Cypripedium parviflorum",
 987: 'corn',
 988: 'acorn',
 989: 'hip, rose hip, rosehip',
 990: 'buckeye, horse chestnut, conker',
 991: 'coral fungus',
 992: 'agaric',
 993: 'gyromitra',
 994: 'stinkhorn, carrion fungus',
 995: 'earthstar',
 996: 'hen-of-the-woods, hen of the woods, Polyporus frondosus, Grifola frondosa',
 997: 'bolete',
 998: 'ear, spike, capitulum',
 999: 'toilet tissue, toilet paper, bathroom tissue'}

# YOLO
classNames = ['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 
              'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 
              'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 
              'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 
              'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 
              'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 
              'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 
              'diningtable', 'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 
              'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 
              'teddy bear', 'hair drier', 'toothbrush']

classNames_seg = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}

color_map = {'person': (144, 154, 186),
 'bicycle': (92, 254, 94),
 'car': (11, 14, 212),
 'motorbike': (14, 135, 178),
 'aeroplane': (138, 26, 244),
 'bus': (183, 53, 158),
 'train': (67, 139, 121),
 'truck': (255, 147, 183),
 'boat': (55, 185, 55),
 'traffic light': (52, 152, 147),
 'fire hydrant': (149, 195, 221),
 'stop sign': (122, 217, 219),
 'parking meter': (119, 127, 91),
 'bench': (63, 171, 255),
 'bird': (80, 51, 255),
 'cat': (170, 109, 244),
 'dog': (222, 75, 235),
 'horse': (244, 90, 5),
 'sheep': (18, 143, 115),
 'cow': (33, 90, 34),
 'elephant': (144, 225, 204),
 'bear': (115, 7, 153),
 'zebra': (23, 202, 35),
 'giraffe': (66, 175, 14),
 'backpack': (32, 169, 249),
 'umbrella': (83, 251, 165),
 'handbag': (224, 165, 52),
 'tie': (146, 75, 63),
 'suitcase': (176, 166, 51),
 'frisbee': (207, 173, 132),
 'skis': (123, 134, 118),
 'snowboard': (121, 207, 139),
 'sports ball': (134, 140, 220),
 'kite': (161, 4, 100),
 'baseball bat': (51, 56, 163),
 'baseball glove': (4, 165, 191),
 'skateboard': (79, 157, 219),
 'surfboard': (15, 129, 24),
 'tennis racket': (85, 136, 62),
 'bottle': (88, 86, 11),
 'wine glass': (56, 8, 164),
 'cup': (138, 87, 138),
 'fork': (84, 234, 185),
 'knife': (65, 30, 168),
 'spoon': (185, 246, 22),
 'bowl': (74, 30, 248),
 'banana': (185, 199, 52),
 'apple': (126, 20, 161),
 'sandwich': (200, 214, 52),
 'orange': (27, 105, 74),
 'broccoli': (67, 235, 98),
 'carrot': (228, 181, 94),
 'hot dog': (15, 78, 220),
 'pizza': (126, 155, 64),
 'donut': (191, 242, 146),
 'cake': (184, 237, 96),
 'chair': (134, 143, 161),
 'sofa': (24, 112, 158),
 'pottedplant': (215, 244, 80),
 'bed': (86, 182, 76),
 'diningtable': (34, 201, 193),
 'toilet': (194, 187, 151),
 'tvmonitor': (114, 78, 91),
 'laptop': (253, 36, 235),
 'mouse': (133, 209, 212),
 'remote': (12, 121, 127),
 'keyboard': (53, 74, 155),
 'cell phone': (66, 193, 126),
 'microwave': (82, 11, 216),
 'oven': (160, 77, 130),
 'toaster': (9, 167, 16),
 'sink': (4, 196, 139),
 'refrigerator': (204, 243, 133),
 'book': (138, 183, 64),
 'clock': (223, 159, 249),
 'vase': (140, 191, 92),
 'scissors': (34, 83, 114),
 'teddy bear': (130, 145, 56),
 'hair drier': (37, 202, 189),
 'toothbrush': (28, 118, 17)}
color_map_seg = {0: (28, 46, 43),
 1: (184, 86, 157),
 2: (128, 108, 18),
 3: (81, 220, 201),
 4: (190, 227, 137),
 5: (18, 14, 186),
 6: (238, 163, 194),
 7: (216, 84, 90),
 8: (120, 118, 12),
 9: (90, 166, 88),
 10: (69, 184, 93),
 11: (228, 212, 186),
 12: (181, 185, 228),
 13: (82, 204, 236),
 14: (127, 250, 142),
 15: (255, 181, 232),
 16: (236, 179, 233),
 17: (249, 113, 166),
 18: (85, 137, 245),
 19: (158, 155, 208),
 20: (159, 106, 250),
 21: (187, 38, 174),
 22: (4, 97, 54),
 23: (30, 25, 139),
 24: (116, 54, 69),
 25: (136, 125, 107),
 26: (30, 216, 16),
 27: (29, 185, 184),
 28: (88, 127, 12),
 29: (42, 58, 34),
 30: (12, 20, 10),
 31: (191, 130, 65),
 32: (80, 94, 0),
 33: (197, 22, 126),
 34: (77, 18, 2),
 35: (176, 57, 146),
 36: (172, 250, 15),
 37: (157, 229, 23),
 38: (135, 205, 78),
 39: (242, 115, 47),
 40: (161, 52, 12),
 41: (229, 65, 201),
 42: (249, 167, 73),
 43: (174, 132, 134),
 44: (214, 9, 71),
 45: (29, 129, 17),
 46: (67, 82, 87),
 47: (49, 232, 118),
 48: (16, 126, 119),
 49: (227, 37, 128),
 50: (41, 116, 184),
 51: (131, 216, 142),
 52: (2, 77, 18),
 53: (196, 209, 82),
 54: (56, 44, 123),
 55: (52, 51, 10),
 56: (93, 118, 53),
 57: (111, 12, 237),
 58: (232, 158, 194),
 59: (108, 107, 222),
 60: (217, 10, 26),
 61: (214, 92, 48),
 62: (245, 187, 9),
 63: (60, 187, 148),
 64: (190, 157, 9),
 65: (211, 51, 53),
 66: (156, 101, 8),
 67: (231, 30, 210),
 68: (248, 237, 106),
 69: (37, 2, 145),
 70: (12, 190, 156),
 71: (39, 112, 251),
 72: (98, 59, 191),
 73: (200, 237, 71),
 74: (176, 202, 62),
 75: (130, 62, 62),
 76: (41, 171, 200),
 77: (108, 53, 12),
 78: (240, 22, 254),
 79: (148, 183, 234)}
# Check device available
try:
    subprocess.check_output('nvidia-smi')
    print('Nvidia GPU is available.')
    DEVICE: str = 'GPU'
except:
    print('No Nvidia GPU available.')
    DEVICE: str = 'CPU'

# weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT
# auto_transforms = weights.transforms()
# model = torchvision.models.efficientnet_b0(weights = weights).to(device)

app = FastAPI()

# ONNX model path
# model_cls_path = "./model/cls/efficientnet_b0.onnx"
model_obj_path = "./model/obj/yolov8n.onnx"
model_seg_path = "./model/seg/yolov8s-seg.onnx"

class ClsImageRequest(BaseModel):
    image: str  # Base64 encoded image
    model: str

class ObjSegImageRequest(BaseModel):
    image: str  # Base64 encoded image

# decode function
def decode_base64(image_base64: bytes = None) -> Image:
    try:
        image_data = base64.b64decode(image_base64)
        return Image.open(BytesIO(image_data))
    except Exception as e:
        raise ValueError(f"Failed to decode base64 image: {e}")
    # return Image.open(BytesIO(base64.b64decode(image_base64)))

def encode_base64(image):
    # Encode PIL image to base64
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Endpoint for testing server connectivity
@app.get("/servertest")
async def hello():
    return "Hi server is working now"


@app.post("/cls_predict", status_code=status.HTTP_200_OK)
async def predict(request: ClsImageRequest):
    # print(request)
    model = request.model
    print(model)

    try:
        cls_image = decode_base64(request.image) # PIL image
        # return {"type": type(image), "width": image.width, "height": image.height}
    except:
        return {"predictions": "Fail to decode_base64 image"}
    
    if model == 'Efficientnet B0':
        model_cls_path = "./model/cls/efficientnet_b0.onnx"
    elif model == 'Efficientnet B1':
        model_cls_path = "./model/cls/efficientnet_b1.onnx"
    elif model == 'Efficientnet B2':
        model_cls_path = "./model/cls/efficientnet_b2.onnx"
    elif model == 'Efficientnet B3':
        model_cls_path = "./model/cls/efficientnet_b3.onnx"


    # Define the transformation pipeline using transforms.Compose
    transform_pipeline = transforms.Compose([
        transforms.Resize(256, interpolation=InterpolationMode.BICUBIC),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    # input to feed into onnx model
    inputs_array = (transform_pipeline(cls_image).unsqueeze(dim = 0)).numpy()

    # Run inference
    # ort_inputs = ort.OrtValue.ortvalue_from_numpy(inputs, "cuda", 0)
    if DEVICE.lower() == "gpu":
        print("GPU")
        ort_session = ort.InferenceSession(model_cls_path, providers=['AzureExecutionProvider'])
        ort_inputs = {ort_session.get_inputs()[0].name: inputs_array}
        ort_outs = ort_session.run(None, ort_inputs) # result of model
        target_image_pred_probs = ort_outs[0]
        
        target_image_pred_probs = torch.tensor(target_image_pred_probs)
        target_image_pred_probs = torch.softmax(target_image_pred_probs, dim = 1)
        # print(target_image_pred_probs[0][:5])
        top4_values, top4_indices = torch.topk(target_image_pred_probs, 4)
        top4_values_list = list(round(float(v), 4) for v in top4_values[0].cpu().numpy())
        top4_indices_list = list(top4_indices[0].cpu().numpy())
        # print(target_image_pred_probs)
        # print(type(target_image_pred_probs))
        

        
    elif DEVICE.lower() == "cpu":
        print("CPU")
        ort_session = ort.InferenceSession(model_cls_path, providers=['CPUExecutionProvider'])
        ort_inputs = {ort_session.get_inputs()[0].name: inputs_array}
        ort_outs = ort_session.run(None, ort_inputs)
        target_image_pred_probs = ort_outs[0]
        target_image_pred_probs = torch.tensor(target_image_pred_probs)

        top4_values, top4_indices = torch.topk(target_image_pred_probs, 4)
        top4_values_list = list(round(float(v), 4) for v in top4_values[0].cpu().numpy())
        top4_indices_list = list(top4_indices[0].cpu().numpy())
    

    prediction = {
        "Class1" : class_dict[top4_indices_list[0]],
        "Prob1" : top4_values_list[0],
        "Class2": class_dict[top4_indices_list[1]],
        "Prob2": top4_values_list[1],
        "Class3": class_dict[top4_indices_list[2]],
        "Prob3": top4_values_list[2],
        "Class4": class_dict[top4_indices_list[3]],
        "Prob4": top4_values_list[3]
    }

    
    return JSONResponse(status_code = 200, content = prediction)

# @app.post("/obj_predict", status_code=status.HTTP_200_OK)
# async def predict(request: ImageRequest):
#     try:
#         obj_image = decode_base64(request.image) # PIL image
#         # return {"type": type(image), "width": image.width, "height": image.height}
#     except:
#         return {"predictions": "Fail to decode_base64 image"}
    
#     # Load the exported ONNX model
#     obj_model = YOLO(model_obj_path)

#     # Predict
#     results = obj_model(obj_image)

#     obg_img_array = np.array(obj_image)
#     obg_img_array_bgr = cv2.cvtColor(obg_img_array, cv2.COLOR_RGB2BGR)

#     boxes = results[0].boxes.xyxy.cpu()
#     confidences = results[0].boxes.conf.cpu().tolist()
#     classes = results[0].boxes.cls.cpu().tolist()
#     object_list = []
#     for box, conf, cls in zip(boxes, confidences, classes):
    
#         box = list(map(int, box))
    
#         cls_name = classNames[int(cls)]

#         object_list.append(cls_name)

#         color = color_map[cls_name]
#         # Prepare text
#         label = f"{cls_name} {conf:.4f}"
#         (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_ITALIC  , 0.5, 2)
#         top_left = (box[0], box[1] - text_height - baseline)
#         bottom_right = (box[0] + text_width, box[1])
#         cv2.rectangle(obg_img_array_bgr, (box[0], box[1]), (box[2], box[3]), color, 2) # image, coor1, coor2, color, thick
#         # Draw background rectangle
#         cv2.rectangle(obg_img_array_bgr, top_left, bottom_right, color, thickness=cv2.FILLED)
#         cv2.putText(obg_img_array_bgr, f"{cls_name} {conf:.4f}", (int(box[0]), int(box[1]) - 5), cv2.FONT_ITALIC  , 0.5, (255, 255, 255), 2)

#     obg_img_array_rgb = cv2.cvtColor(obg_img_array_bgr, cv2.COLOR_BGR2RGB)

#     # Convert the NumPy array back to a PIL image
#     final_image = Image.fromarray(obg_img_array_rgb)

#     # Encode the PIL image to base64
#     encoded_image = encode_base64(final_image)

#     prediction = {
#         "obj_image": encoded_image,
#         "objects": object_list,
#         "conf": confidences
#     }

#     return JSONResponse(status_code = 200, content = prediction)

# if __name__ == "__main__":
#     # Run the FastAPI application using uvicorn server, listening on all available network interfaces
#     uvicorn.run(app, host="0.0.0.0", port=3000)




@app.post("/obj_predict", status_code=200)
async def predict(request: ObjSegImageRequest):
    print('Here')
    try:
        obj_image = decode_base64(request.image)
    except Exception as e:
        return {"predictions": "Fail to decode_base64 image", "error": str(e)}

    # Load the exported ONNX model
    obj_model = YOLO(model_obj_path)

    # Predict
    results = obj_model(obj_image)

    obg_img_array = np.array(obj_image)
    obg_img_array_bgr = cv2.cvtColor(obg_img_array, cv2.COLOR_RGB2BGR)

    boxes = results[0].boxes.xyxy.cpu()
    confidences = results[0].boxes.conf.cpu().tolist()
    classes = results[0].boxes.cls.cpu().tolist()
    object_list = []
    for box, conf, cls in zip(boxes, confidences, classes):
        box = list(map(int, box))
        cls_name = classNames[int(cls)]
        object_list.append(cls_name)
        color = color_map[cls_name]
        label = f"{cls_name} {conf:.4f}"
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
        top_left = (box[0], box[1] - text_height - baseline)
        bottom_right = (box[0] + text_width, box[1])
        cv2.rectangle(obg_img_array_bgr, (box[0], box[1]), (box[2], box[3]), color, 5)
        cv2.rectangle(obg_img_array_bgr, top_left, bottom_right, color, thickness=cv2.FILLED)
        cv2.putText(obg_img_array_bgr, label, (int(box[0]), int(box[1]) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    obg_img_array_rgb = cv2.cvtColor(obg_img_array_bgr, cv2.COLOR_BGR2RGB)

    # Convert the NumPy array back to a PIL image
    final_image = Image.fromarray(obg_img_array_rgb)

    # Encode the PIL image to base64
    encoded_image = encode_base64(final_image)

    # Count occurrences of each unique label
    unique_labels = list(set(object_list))
    counts = [object_list.count(label) for label in unique_labels]

    cmap = plt.get_cmap('BuPu')
    colors = [cmap(i / len(unique_labels)) for i in range(1,len(unique_labels) + 1)]

    # Create a pie chart
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(counts, labels=counts, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)

    # Change the color of the text inside the pie chart to white
    for autotext in autotexts:
        autotext.set_color('white')
    
    # Draw a circle at the center to make it a donut
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Add a legend
    ax.legend(wedges, unique_labels,fontsize = "14", loc='upper center', bbox_to_anchor=(0.5, -0.003),
          ncol=3,frameon=False)

    # plt.title("Object Detection Distribution")

    # Adjust layout to include legend
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)

    # Convert buffer to base64
    chart_image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    # chart_image_base64_str = f"data:image/png;base64,{chart_image_base64}"

    prediction = {
        "obj_image": encoded_image,
        "chart_image": chart_image_base64,
    }

    return JSONResponse(status_code=200, content=prediction)

@app.post("/seg_predict", status_code=200)
async def predict(request: ObjSegImageRequest):

    try:
        seg_image = decode_base64(request.image)
    except Exception as e:
        return {"predictions": "Fail to decode_base64 image", "error": str(e)}
    
    
    seg_image = seg_image.resize((640, 640))
    seg_img_resize_array = np.array(seg_image) 

    

    
    # Load the exported ONNX model
    seg_model = YOLO(model_seg_path)
    # Predict
    results = seg_model(seg_image, conf = 0.28)
    class_tensor = results[0].boxes.cls.cpu().numpy()
    confidence_tensor = results[0].boxes.conf.cpu().numpy()
    position_tensor = (results[0].masks.to(torch.int32)).data.cpu().numpy()
    
    # print(len(class_tensor))
    # print(len(confidence_tensor))
    # print(position_tensor.shape)
    
    
    # Create a mask overlay
    mask_overlay = np.zeros_like(seg_img_resize_array)
    print(f'2: {mask_overlay.shape}')

    # Track classes that appear in the image
    present_classes1 = set()
    present_classes2 = {}
    total_pixels = seg_image.size[0] * seg_image.size[1]

    for i in range(position_tensor.shape[0]):
        class_id = int(class_tensor[i])

        # class_name = classNames_seg[class_id]
        
        mask = position_tensor[i] > 0.5

        color = color_map_seg[class_id]


        mask_overlay[mask] = color


        present_classes1.add(class_id)

        if class_id in present_classes2:
            present_classes2[class_id] += np.sum(mask)
        else:
            present_classes2[class_id] = np.sum(mask)
        

    # Calculate area percentages for each class
    area_percentages = {f"{classNames_seg[class_id]}": (area / total_pixels) * 100 for class_id, area in present_classes2.items()}
    
    # Create pie chart
    fig, ax = plt.subplots(figsize=(10, 10))

     # Plot pie chart
    labels = list(area_percentages.keys())
    unique_labels = list(set(labels))
    sizes = list(area_percentages.values())

    cmap = plt.get_cmap('BuPu')
    pie_colors = [cmap(i / len(unique_labels)) for i in range(1,len(unique_labels) + 1)]
    
    wedges, texts, autotexts = ax.pie(sizes, labels=None, colors=pie_colors, autopct='%1.1f%%', startangle=0, pctdistance=1.1, textprops=dict(color="white", fontsize=12))

# Draw a circle at the center to make it a donut

    # Draw a circle at the center to make it a donut
    inner_circle = plt.Circle((0, 0), 0.70, fc='white')  # Create a white circle at the center for the donut hole
    ax.add_artist(inner_circle)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    ax.legend(wedges, labels,fontsize = "20", loc='upper center', bbox_to_anchor=(0.5, -0.003), ncol=3, frameon=False)

    # Adjust layout to include legend
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buffer_chart = BytesIO()
    plt.savefig(buffer_chart, format='png', bbox_inches='tight', pad_inches=0)
    buffer_chart.seek(0)

    # Convert buffer to base64 for donut chart image
    chart_image = base64.b64encode(buffer_chart.read()).decode('utf-8')

    # Close the figure to free memory
    plt.close(fig)

    # Combine original image with mask overlay
    combined_image = (0.5 * seg_img_resize_array + 0.5 * mask_overlay).astype(np.uint8)

    

    
    # Plot the original and combined images
    plt.figure(figsize=(10, 10))
    plt.imshow(combined_image)
    plt.axis("off")

    # Create legend handles for present classes only
    legend_handles = []
    for cls_id in present_classes1:
        color = np.array(color_map_seg[cls_id]) / 255.0  # Normalize color values to [0, 1]
        patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=classNames_seg[cls_id])
        legend_handles.append(patch)

    # Add legend to the plot
    plt.legend(handles=legend_handles, loc='upper right', title='Classes')
    
    # Save the figure to a BytesIO object
    buffer_combined = BytesIO()
    plt.savefig(buffer_combined, format='png', bbox_inches='tight', pad_inches=0)
    buffer_combined.seek(0)

    # Convert buffer to base64
    mask_image_base64 = base64.b64encode(buffer_combined.read()).decode('utf-8')

    prediction = {
        "seg_image": mask_image_base64,
        "chart_image": chart_image,
    }

    return JSONResponse(status_code=200, content=prediction)

if __name__ == "__main__":
    uvicorn.run("aiservermaster:app", host="0.0.0.0", port=3000, reload = True)