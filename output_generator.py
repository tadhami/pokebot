import pokebot_parser
import pokemon
import pokemon_name_checker
'''
Script containing function calls to generate an output string/response string based on certain conditionals
(relating to which tag)
'''
out = ''
exclusion_tags = ['goodbye', 'hi', 'features', 'ucl']

def list_features():
    out = "- Tell you a pokemon's pokedex number\n- Tell you a pokemon's specific in-game location\n- Tell you a pokemon's evolution criteria\n- Tell you a pokemon's strengths\n- Tell you a pokemon's weaknesses\n- Tell you a pokemon's type\n- Tell you a pokemon's height\n- Tell you a pokemon's weight\n- Tell you a pokemon's classification\n- Tell you all I know about a pokemon"
    print("output in list_features is: ", out)
    return out 
def chatbot_output_string_generator(tag, message):
    if (tag == 'dex_number'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        output = pokebot_parser.dex_num_extractor(pokemon_name)
        return output  
    elif (tag == 'location'):
        try:
            pokemon_name = pokemon_name_checker.my_name_extractor(message)
        except:
            pokemon_name = None
        try:
            game_tuple = pokebot_parser.game_checker(message)
        except:
            game_tuple = False, 'No game found: Output Generator'
        if (game_tuple[0] == True):
            pokemon_game = pokebot_parser.game_processor(game_tuple)
            item_tup = pokebot_parser.get_item_output(message, game_tuple)
            if (item_tup[1] == True):
                final_item_output = pokebot_parser.item_final_output(item_tup[0], pokemon_game)
                return final_item_output
            elif (pokemon_name != None):
                location_output = pokebot_parser.obtain_pokemon_output(pokemon_name, pokemon_game)
                return location_output 
        else:
            output = "You either can't get it in this game, you misspelled the name, or I'm not advanced enough to handle this request"
            return output 
    elif (tag == 'level_evolve'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        output = pokebot_parser.obtain_evolution_output(pokemon_name)
        return output 
    elif (tag == 'strengths'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        type_lst = pokebot_parser.type_extractor(pokemon_name, 1)
        output = pokebot_parser.strengths(type_lst)
        return output 
    elif (tag == 'weaknesses'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        type_lst = pokebot_parser.type_extractor(pokemon_name, 1)
        output = pokebot_parser.weaknesses(type_lst)
        return output 
    elif (tag == 'type'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        type_lst = pokebot_parser.type_extractor(pokemon_name, 1)
        output = type_lst[2].replace("\n", "")
        return output
    elif (tag == 'height'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        my_pokemon = pokemon.Pokemon()
        pokemon.populate_pokemon(my_pokemon, pokemon_name)
        return str(my_pokemon.height_m) + ' m tall'
    elif (tag == 'weight'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        my_pokemon = pokemon.Pokemon()
        pokemon.populate_pokemon(my_pokemon, pokemon_name)
        return str(my_pokemon.weight_kg) + 'kg'
    elif (tag == 'classification'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        my_pokemon = pokemon.Pokemon()
        pokemon.populate_pokemon(my_pokemon, pokemon_name)
        return str(my_pokemon.classification)
    elif (tag == 'all info'):
        pokemon_name = pokemon_name_checker.my_name_extractor(message)
        my_pokemon = pokemon.Pokemon()
        pokemon.populate_pokemon(my_pokemon, pokemon_name)
        out = pokemon.all_string_builder(my_pokemon)
        return out 
    elif (tag == 'move learning'):
        output = 'move learning is a Work in Progress'
        return output
    elif (tag == 'list_out'):
        print("entered list out")
        output = list_features()
        print("output is: ", output)
        return output 

def json_modifier(json_data, tag, message):
    print("tag in json_modifier is: ", tag)
    json_dict = {'hi':0, 'features':1, 'list_out':2, 'dex_number':3, 'location':4, 'level_evolve':5, 'strengths':6, 
    'weaknesses':7, 'type':8, 'height':9, 'weight':10, 'classification':11, 'all info':12, 'move learning':13, 'goodbye':14, 'ucl':15}
    if (tag not in exclusion_tags):
        print("ENTERED")
        output = chatbot_output_string_generator(tag, message)
        print("AFTER ENTER: OUTPUT IS: ", output) 
        json_data['intents'][json_dict[tag]]['responses'][0] = output
    return json_data 



