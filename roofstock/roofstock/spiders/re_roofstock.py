from time import daylight
import scrapy
import json

class ReRoofstockSpider(scrapy.Spider):
    name = 're_roofstock'

    payload = {
   "operationName":"originalFilteredListings",
   "variables":{
      "filteredListingsInput":{
         "id":"all-properties",
         "criteria":{
            "hasCriteriaOverrides":False,
            "paging":{
               "pageNumber":0,
               "pageSize":25,
               "orderBy":{
                  "field":"property.computed.sortOrder.marketplace",
                  "direction":"ASC"
               }
            },
            "allowableSaleTypes":None,
            "availableEquityShares":{
               "max":None,
               "min":None
            },
            "cbsaCodes":None,
            "equityOwnershipType":"All",
            "financial":{
               "annualAppreciation":{
                  "max":None,
                  "min":None
               },
               "capRate":{
                  "max":None,
                  "min":None
               },
               "downPayment":{
                  "max":None,
                  "min":None
               },
               "grossYield":{
                  "max":None,
                  "min":None
               },
               "inspectionEstRepairCost":{
                  "max":None,
                  "min":None
               },
               "isCashOnly":None,
               "listPrice":{
                  "max":None,
                  "min":None
               },
               "listPriceLowerThanPropertyValue":None,
               "marketRent":{
                  "max":None,
                  "min":None
               },
               "monthlyHoa":{
                  "max":None,
                  "min":None
               },
               "monthlyRent":{
                  "max":None,
                  "min":None
               },
               "rentToPropertyValuePercentage":{
                  "max":None,
                  "min":None
               }
            },
            "isBestSchools":None,
            "isFeatured":None,
            "isHoa":None,
            "isInspectionContingency":None,
            "isNewlyListed":None,
            "isOpenHouse":None,
            "isPriceReduced":None,
            "isRentersWarehouse":None,
            "isRentGuaranteed":None,
            "isTurnKey":None,
            "lease":{
               "isSection8":None,
               "occupancy":[

               ],
               "remainingMonthsOnLease":None
            },
            "listingId":None,
            "listingSource":None,
            "listingStatus":[
               "ForSale",
               "ComingSoon"
            ],
            "marketId":None,
            "markets":None,
            "physical":{
               "bathRooms":{
                  "max":None,
                  "min":None
               },
               "bedRooms":{
                  "max":None,
                  "min":None
               },
               "isPool":None,
               "squareFeet":{
                  "max":None,
                  "min":None
               },
               "yearBuilt":{
                  "max":None,
                  "min":None
               }
            },
            "propertyType":None,
            "score":{
               "avgSchool":{
                  "max":None,
                  "min":None
               },
               "neighborhood":{
                  "max":None,
                  "min":None
               },
               "propertyCondition":{
                  "max":None,
                  "min":None
               }
            },
            "visibility":[
               "Public"
            ]
         }
      },
      "assumptionInput":{
         "downPaymentPercentage":None,
         "loanInterestRate":None
      }
   },
        "query": "query originalFilteredListings($filteredListingsInput: FilteredListingsInput!, $assumptionInput: ListingAssumptionInput!) {\n  filteredListings(input: $filteredListingsInput) {\n    isGlobalFilter\n    isUserFilter\n    criteria {\n      hasCriteriaOverrides\n      allowableSaleTypes\n      availableEquityShares {\n        max\n        min\n        __typename\n      }\n      cbsaCodes\n      equityOwnershipType\n      financial {\n        annualAppreciation {\n          max\n          min\n          __typename\n        }\n        capRate {\n          max\n          min\n          __typename\n        }\n        downPayment {\n          max\n          min\n          __typename\n        }\n        grossYield {\n          max\n          min\n          __typename\n        }\n        inspectionEstRepairCost {\n          max\n          min\n          __typename\n        }\n        isCashOnly\n        listPrice {\n          max\n          min\n          __typename\n        }\n        listPriceLowerThanPropertyValue\n        marketRent {\n          max\n          min\n          __typename\n        }\n        monthlyHoa {\n          max\n          min\n          __typename\n        }\n        monthlyRent {\n          max\n          min\n          __typename\n        }\n        rentToPropertyValuePercentage {\n          max\n          min\n          __typename\n        }\n        __typename\n      }\n      isBestSchools\n      isFeatured\n      isHoa\n      isInspectionContingency\n      isNewlyListed\n      isOpenHouse\n      isPriceReduced\n      isRentersWarehouse\n      isRentGuaranteed\n      isTurnKey\n      lease {\n        isSection8\n        occupancy\n        remainingMonthsOnLease\n        __typename\n      }\n      listingId\n      listingSource\n      listingStatus\n      marketId\n      markets\n      paging {\n        orderBy {\n          direction\n          field\n          __typename\n        }\n        pageNumber\n        pageSize\n        __typename\n      }\n      physical {\n        bathRooms {\n          max\n          min\n          __typename\n        }\n        bedRooms {\n          max\n          min\n          __typename\n        }\n        isPool\n        squareFeet {\n          max\n          min\n          __typename\n        }\n        yearBuilt {\n          max\n          min\n          __typename\n        }\n        __typename\n      }\n      propertyType\n      score {\n        avgSchool {\n          max\n          min\n          __typename\n        }\n        neighborhood {\n          max\n          min\n          __typename\n        }\n        propertyCondition {\n          max\n          min\n          __typename\n        }\n        __typename\n      }\n      visibility\n      __typename\n    }\n    data {\n      id\n      visibility\n      isRack\n      isHoa\n      status\n      mainImageUrl\n      marketId\n      marketName\n      propertyType\n      buyerAccountId\n      sellerAccountId\n      sellerAccountName\n      isPriceReduced\n      priceReductionAmount\n      daysOnMarket\n      geoLocation {\n        latitude\n        longitude\n        __typename\n      }\n      lease {\n        isSection8\n        occupancy\n        leaseStartDate\n        leaseEndDate\n        __typename\n      }\n      financial {\n        capRate\n        grossYield\n        isCashOnly\n        inspectionEstRepairCost\n        leveredIrr\n        listPrice\n        marketRent\n        monthlyRent\n        totalReturn\n        salePrice\n        __typename\n      }\n      openHouseProgram {\n        isOpenHouseOfferPeriod\n        isOpenHouseReviewPeriod\n        __typename\n      }\n      physical {\n        bedRooms\n        bathRooms\n        squareFeet\n        yearBuilt\n        __typename\n      }\n      score {\n        neighborhood\n        highSchool\n        middleSchool\n        elementarySchool\n        __typename\n      }\n      address {\n        address1\n        address2\n        city\n        country\n        county\n        state\n        zip\n        __typename\n      }\n      calculated(assumptions: $assumptionInput) {\n        propertyValue\n        listPrice\n        monthlyRent\n        rentType\n        capRate\n        grossYield\n        inspectionEstRepairCost\n        leveredIrr\n        totalReturn\n        hasPotentialRentGrowth\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      orderBy {\n        field\n        direction\n        __typename\n      }\n      pageNumber\n      pageSize\n      recordsTotal\n      __typename\n    }\n    __typename\n  }\n}\n"
   }

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.roofstock.com/graphql',
            method='POST',
            headers={
                'content-type': 'application/json'
            },
            body=json.dumps(self.payload),
            callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.body)
        listings = data.get('data').get('filteredListings').get('data')
        # total_records = data.get('data').get('filteredListings').get('pageInfo').get('recordsTotal')
        # page_size = data.get('data').get('filteredListings').get('pageInfo').get('pageSize')
        # print(type(total_records))
        # print(type(page_size))
        for listing in listings:
            yield {
                #'address': listing.get('address'),
                #Generic
                'id': listing.get('id'),
                'visability': listing.get('visability'),
                'is_rack': listing.get('isRack'),
                'hoa': listing.get('isHoa'),
                'status': listing.get('status'),
                'img_url': listing.get('mainImageUrl'),
                'marketName': listing.get('marketName'),
                'property_type': listing.get('propertyType'),
                'Seller': listing.get('sellerAccountName'),
                'daysOnMarket': listing.get('daysOnMarket'),
                'propertyType': listing.get('propertyType'),


                #Address
                'street1': listing.get('address').get('address1'),
                'unit': listing.get('address').get('address2'),
                'city': listing.get('address').get('city'),
                'country': listing.get('address').get('country'),
                'county': listing.get('address').get('county'),
                'state': listing.get('address').get('state'),
                'zip_code': listing.get('address').get('zip'),

                #Calculated
                'CAP_Rate1': listing.get('calculated').get('capRate'),
                'gross_yield1': listing.get('calculated').get('grossYield'),
                'potential_rent_growth':  listing.get('calculated').get('hasPotentialRentGrowth'),
                'est_repair_cost1': listing.get('calculated').get('inspectionEstRepairCost'),
                'levered_IRR': listing.get('calculated').get('leveredIrr'),
                'list_price1': listing.get('calculated').get('listPrice'),
                'monthly_rent': listing.get('calculated').get('monthlyRent'),
                'property_value': listing.get('calculated').get('propertyValue'),
                'rent_type': listing.get('calculated').get('rentType'),
                'total_return1': listing.get('calculated').get('totalReturn'),

                #Financial
                'CAP_Rate2': listing.get('financial').get('capRate'),
                'gross_yield2': listing.get('financial').get('grossYield'),
                'est_repair_cost2': listing.get('financial').get('inspectionEstRepairCost'),
                'cash_only?': listing.get('financial').get('isCashOnly'),
                'levered_irr': listing.get('financial').get('leveredIrr'),
                'list_price3': listing.get('financial').get('listPrice'),
                'market_rent': listing.get('financial').get('marketRent'),
                'charged_rent': listing.get('financial').get('monthlyRent'),
                'sales_price': listing.get('financial').get('salePrice'),
                'total_return2': listing.get('financial').get('totalReturn'),

                #GeoLocation
                'latitude': listing.get('geoLocation').get('latitude'),
                'longitude': listing.get('geoLocation').get('longitude'),

                #Lease
                'Section8?': listing.get('lease').get('isSection8'),
                'lease_state': listing.get('lease').get('leaseStartDate'),
                'lease_end': listing.get('lease').get('leaseEndDate'),
                'occupancy': listing.get('lease').get('occupancy'),

                #Physical
                'bathrooms': listing.get('physical').get('bathRooms'),
                'bedrooms': listing.get('physical').get('bedrooms'),
                'sq_foot': listing.get('physical').get('squareFeet'),
                'yr_built': listing.get('physical').get('yearBuilt'),

                #Schools
                'elementary_school': listing.get('score').get('elementarySchool'),
                'middle_school': listing.get('score').get('middleSchool'),
                'high_school': listing.get('score').get('highSchool'),
                'neighborhood': listing.get('score').get('neighborhood')

            }

        total_records = data.get('data').get('filteredListings').get('pageInfo').get('recordsTotal')
        page_size = data.get('data').get('filteredListings').get('pageInfo').get('pageSize')
        pagination = total_records//page_size

        if self.payload['variables']['filteredListingsInput']['criteria']['paging']['pageNumber'] <= pagination:
            self.payload['variables']['filteredListingsInput']['criteria']['paging']['pageNumber'] += 1
            print('x')
            print('x')
            print(self.payload['variables']['filteredListingsInput']['criteria']['paging']['pageNumber'])
            print('x')
            print('x')

            yield scrapy.Request(
                url="https://www.roofstock.com/graphql",
                method="POST",
                body=json.dumps(self.payload),
                headers={
                    'Content-Type': 'application/json'
                },
                dont_filter=True,
                callback=self.parse
            )





