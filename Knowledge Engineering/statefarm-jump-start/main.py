


# takes a company url
def get_company_info(url):
    # ask user to tell us who that url is for
    co_name = input(f'Please enter a name for {url}: ')

    # check for wiki
    page_name = wiki.check_for_wiki(co_name)
    if not page_name:
        # set these in cases wiki not found
        founded = ""
        num_emp = ""
        name = co_name
    else:
        name = page_name.title
        # if wiki exists get some info about the company
        # TODO: CLEAN THESE BABIES UP
        # print("fullurl: ", page_name.fullurl)
        founded = infobox.get_founded(page_name.fullurl)
        # print(founded)
        num_emp = infobox.get_emp(page_name.fullurl)
        industry = infobox.get_industry(page_name.fullurl)
        make_industry(industry, name)

    company_json = {
        "type": "company",
        "name": name,
        "url": url,
        "attributes": {
            "founded": founded,
            "numberEmployees": num_emp,
        }
    }
    return company_json, name


# create edge object
# class edge list example has duplicate keys...not sure that's valid json?
def get_edge_company(co1, co2, relation):
    edge = {
        "company1": co1,
        "relation": relation,
        "company2": co2
    }
    return edge


# create edge object
def get_edge_service(co, serv, relation):
    edge = {
        "company": co,
        "relation": relation,
        "service": serv
    }
    return edge


# create service object
def get_service_info(ser):
    service = {
        "type": "service",
        "name": ser,
        "description": ""
    }
    return service


# create industry object
def make_industry(industry, name):
    # make industry object
    ind = {
        "type": "industry",
        "name": industry,
        "attributes": {
            "NAICScode": "",
            "NAICStitle": "",
            "description": ""
        }
    }
    # write industry object
    with open('StateFarm-nodes-other.jl', 'a') as file:
        file.write(json.dumps(ind) + '\n')

    # create edge
    rel = {
        "company": name,
        "relation": "is_in",
        "industry": industry
    }
    with open('StateFarm-edges.jl', 'a') as f:
        f.write(json.dumps(rel) + '\n')


if __name__ == '__main__':
    # # Ask the user what's up
    # while True:
    #     try:
    #         menu = int(input(f'Press 1 for companies, and 2 for relationships: '))
    #     except ValueError:
    #         print('Sorry, I didn\'t understand that. Please try again')
    #         continue
    #     else:
    #         break

    # create the company objects
    # if menu == 1:
    my_co = "StateFarm"
    # TODO: add a check to see if the nodes file already includes this company so we don't loop through the whole
    #  list when we iterate
    # buyers
    # create advertising node
    ads_json = get_service_info('advertising')
    with open('StateFarm-nodes-other.jl', 'a') as f:
        f.write(json.dumps(ads_json) + '\n')
    # create advertising edge
    ads_edge = get_edge_service(my_co, 'advertising', 'sells')
    with open('StateFarm-edges.jl', 'a') as f:
        f.write(json.dumps(ads_edge) + '\n')
    print('Staring buyers')
    for buyer in buyerList.buyer_list:
        # create company obj
        json_buyer, name = get_company_info(buyer)
        with open('StateFarm-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_buyer) + '\n')
        # create service node
        # rel = input(f'What service does {name} buy from StateFarm?: ')
        # json_service = get_service_info(rel)
        # with open('StateFarm-nodes-other.jl', 'a') as f:
        #     f.write(json.dumps(json_service) + '\n')
        # create buyer relationship (edge)

        # we don't have any other services right now
        rel = 'advertising'
        buyer_edge = get_edge_service(name, rel, 'buys')
        with open('StateFarm-edges.jl', 'a') as f:
            f.write(json.dumps(buyer_edge) + '\n')
    # competitors
    print('Staring competitors')
    for competitor in competitorList.competitor_list:
        json_competitor, name = get_company_info(competitor)
        with open('StateFarm-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_competitor) + '\n')
        # create edge object
        competitor_edge = get_edge_company(my_co, name, 'competes_with')
        with open('StateFarm-edges.jl', 'a') as f:
            f.write(json.dumps(competitor_edge) + '\n')
    # potential new entrants
    print('Staring new entrants')
    for ne in newEntrantList.new_entrants_list:
        json_ne, name = get_company_info(ne)
        with open('StateFarm-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_ne) + '\n')
        # create edge object
        ne_edge = get_edge_company(my_co, name, 'has_potential_entrant')
        with open('StateFarm-edges.jl', 'a') as f:
            f.write(json.dumps(ne_edge) + '\n')
    # StateFarm itself
    print('Let us not forget StateFarm')
    # for other in otherUrlList.other_url_list:
    #     json_other, name = get_company_info(other)
    #     with open('StateFarm-nodes-company.jl', 'a') as f:
    #         f.write(json.dumps(json_other) + '\n')
    # # substitutes
    # print('Staring substitutes')
    # for sub in substituteList.substitute_list:
    #     json_sub, name = get_company_info(sub)
    #     with open('StateFarm-nodes-company.jl', 'a') as f:
    #         f.write(json.dumps(json_sub) + '\n')
    #     # create edge object
    #     sub_edge = get_edge_company(my_co, name, 'has_substitute')
    #     with open('StateFarm-edges.jl', 'a') as f:
    #         f.write(json.dumps(sub_edge) + '\n')
    # suppliers
    print('Staring suppliers')
    for supplier in supplierList.supplier_list:
        json_supplier, name = get_company_info(supplier)
        with open('StateFarm-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_supplier) + '\n')

# elif menu == 2:
#     print("menu 2")
#
# # leave this place!
# else:
#     print("You didn't chose a valid option. Goodbye")