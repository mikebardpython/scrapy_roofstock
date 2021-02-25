from time import daylight
import scrapy
import json


class ReRoofstockSpider(scrapy.Spider):
    name = 're_roofstock'

    payload = {
        "operationName": "originalFilteredListings",
        "variables": {
            "filteredListingsInput": {
                "id": "all-properties",
                "criteria": {
                    "hasCriteriaOverrides": False,
                    "paging": {
                        "pageNumber": 0,
                        "pageSize": 25,
                        "orderBy": {
                            "field": "property.computed.sortOrder.marketplace",
                            "direction": "ASC"
                        }
                    },
                    "allowableSaleTypes": None,
                    "availableEquityShares": {
                        "max": None,
                        "min": None
                    },
                    "cbsaCodes": None,
                    "equityOwnershipType": "All",
                    "financial": {
                        "annualAppreciation": {
                            "max": None,
                            "min": None
                        },
                        "capRate": {
                            "max": None,
                            "min": None
                        },
                        "downPayment": {
                            "max": None,
                            "min": None
                        },
                        "grossYield": {
                            "max": None,
                            "min": None
                        },
                        "inspectionEstRepairCost": {
                            "max": None,
                            "min": None
                        },
                        "isCashOnly": None,
                        "listPrice": {
                            "max": None,
                            "min": None
                        },
                        "listPriceLowerThanPropertyValue": None,
                        "marketRent": {
                            "max": None,
                            "min": None
                        },
                        "monthlyHoa": {
                            "max": None,
                            "min": None
                        },
                        "monthlyRent": {
                            "max": None,
                            "min": None
                        },
                        "rentToPropertyValuePercentage": {
                            "max": None,
                            "min": None
                        }
                    },
                    "isBestSchools": None,
                    "isFeatured": None,
                    "isHoa": None,
                    "isInspectionContingency": None,
                    "isNewlyListed": None,
                    "isOpenHouse": None,
                    "isPriceReduced": None,
                    "isRentersWarehouse": None,
                    "isRentGuaranteed": None,
                    "isTurnKey": None,
                    "lease": {
                        "isSection8": None,
                        "occupancy": [

                        ],
                        "remainingMonthsOnLease": None
                    },
                    "listingId": None,
                    "listingSource": None,
                    "listingStatus": [
                        "ForSale",
                        "ComingSoon"
                    ],
                    "marketId": None,
                    "markets": None,
                    "physical": {
                        "bathRooms": {
                            "max": None,
                            "min": None
                        },
                        "bedRooms": {
                            "max": None,
                            "min": None
                        },
                        "isPool": None,
                        "squareFeet": {
                            "max": None,
                            "min": None
                        },
                        "yearBuilt": {
                            "max": None,
                            "min": None
                        }
                    },
                    "propertyType": None,
                    "score": {
                        "avgSchool": {
                            "max": None,
                            "min": None
                        },
                        "neighborhood": {
                            "max": None,
                            "min": None
                        },
                        "propertyCondition": {
                            "max": None,
                            "min": None
                        }
                    },
                    "visibility": [
                        "Public"
                    ]
                }
            },
            "assumptionInput": {
                "downPaymentPercentage": None,
                "loanInterestRate": None
            }
        },
        "query": "query originalFilteredListings($filteredListingsInput: FilteredListingsInput!, $assumptionInput: ListingAssumptionInput!) {\n  filteredListings(input: $filteredListingsInput) {\n    isGlobalFilter\n    isUserFilter\n    criteria {\n      hasCriteriaOverrides\n      allowableSaleTypes\n      availableEquityShares {\n        max\n        min\n        __typename\n      }\n      cbsaCodes\n      equityOwnershipType\n      financial {\n        annualAppreciation {\n          max\n          min\n          __typename\n        }\n        capRate {\n          max\n          min\n          __typename\n        }\n        downPayment {\n          max\n          min\n          __typename\n        }\n        grossYield {\n          max\n          min\n          __typename\n        }\n        inspectionEstRepairCost {\n          max\n          min\n          __typename\n        }\n        isCashOnly\n        listPrice {\n          max\n          min\n          __typename\n        }\n        listPriceLowerThanPropertyValue\n        marketRent {\n          max\n          min\n          __typename\n        }\n        monthlyHoa {\n          max\n          min\n          __typename\n        }\n        monthlyRent {\n          max\n          min\n          __typename\n        }\n        rentToPropertyValuePercentage {\n          max\n          min\n          __typename\n        }\n        __typename\n      }\n      isBestSchools\n      isFeatured\n      isHoa\n      isInspectionContingency\n      isNewlyListed\n      isOpenHouse\n      isPriceReduced\n      isRentersWarehouse\n      isRentGuaranteed\n      isTurnKey\n      lease {\n        isSection8\n        occupancy\n        remainingMonthsOnLease\n        __typename\n      }\n      listingId\n      listingSource\n      listingStatus\n      marketId\n      markets\n      paging {\n        orderBy {\n          direction\n          field\n          __typename\n        }\n        pageNumber\n        pageSize\n        __typename\n      }\n      physical {\n        bathRooms {\n          max\n          min\n          __typename\n        }\n        bedRooms {\n          max\n          min\n          __typename\n        }\n        isPool\n        squareFeet {\n          max\n          min\n          __typename\n        }\n        yearBuilt {\n          max\n          min\n          __typename\n        }\n        __typename\n      }\n      propertyType\n      score {\n        avgSchool {\n          max\n          min\n          __typename\n        }\n        neighborhood {\n          max\n          min\n          __typename\n        }\n        propertyCondition {\n          max\n          min\n          __typename\n        }\n        __typename\n      }\n      visibility\n      __typename\n    }\n    data {\n      id\n      visibility\n      isRack\n      isHoa\n      status\n      mainImageUrl\n      marketId\n      marketName\n      propertyType\n      buyerAccountId\n      sellerAccountId\n      sellerAccountName\n      isPriceReduced\n      priceReductionAmount\n      daysOnMarket\n      geoLocation {\n        latitude\n        longitude\n        __typename\n      }\n      lease {\n        isSection8\n        occupancy\n        leaseStartDate\n        leaseEndDate\n        __typename\n      }\n      financial {\n        capRate\n        grossYield\n        isCashOnly\n        inspectionEstRepairCost\n        leveredIrr\n        listPrice\n        marketRent\n        monthlyRent\n        totalReturn\n        salePrice\n        __typename\n      }\n      openHouseProgram {\n        isOpenHouseOfferPeriod\n        isOpenHouseReviewPeriod\n        __typename\n      }\n      physical {\n        bedRooms\n        bathRooms\n        squareFeet\n        yearBuilt\n        __typename\n      }\n      score {\n        neighborhood\n        highSchool\n        middleSchool\n        elementarySchool\n        __typename\n      }\n      address {\n        address1\n        address2\n        city\n        country\n        county\n        state\n        zip\n        __typename\n      }\n      calculated(assumptions: $assumptionInput) {\n        propertyValue\n        listPrice\n        monthlyRent\n        rentType\n        capRate\n        grossYield\n        inspectionEstRepairCost\n        leveredIrr\n        totalReturn\n        hasPotentialRentGrowth\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      orderBy {\n        field\n        direction\n        __typename\n      }\n      pageNumber\n      pageSize\n      recordsTotal\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    payload_house_json = {
        "operationName": "originalListing",
        "variables": {
            "listingInput": {
                "listingId": 1783324,
                "portfolioId": None
            },
            "listingAssumptionInput": {
                "totalReturnInYears": None,
                "rentType": None,
                "propertyValue": None,
                "downPaymentPercentage": None,
                "loanInterestRate": None,
                "contingencyCost": None,
                "appreciationType": None,
                "appreciationRate": None,
                "closingCostRate": None,
                "rentGrowthRate": None,
                "propertyTaxType": None,
                "financialsInYear": None,
                "expensesAssumptions": None
            }
        },
        "query": "query originalListing($listingInput: ListingInput!, $listingAssumptionInput: ListingAssumptionInput!) {\n  listing(input: $listingInput) {\n    id\n    visibility\n    isHoa\n    isPartnerListing\n    isRentGuaranteed\n    isTurnKey\n    status\n    cbsaCode\n    marketId\n    propertyType\n    isRack\n    marketName\n    offerFloorRate\n    offerMaxRate\n    offers {\n      id\n      status\n      __typename\n    }\n    inPortfolios {\n      id\n      name\n      __typename\n    }\n    tickerSymbol\n    certificationLevel\n    isAllowOffer\n    sellerAccountId\n    buyerAccountId\n    priceVisibility\n    allowableSaleTypes\n    mlsId\n    mlsName\n    isPriceReduced\n    priceReductionAmount\n    stakeholder {\n      buyerBroker {\n        email\n        firstName\n        lastName\n        phone\n        __typename\n      }\n      sellerBroker {\n        companyName\n        firstName\n        lastName\n        __typename\n      }\n      __typename\n    }\n    inspectionContingencyRequired\n    openHouseProgram {\n      openHouseEndTime\n      openHouseOfferPeriodEndTime\n      isOpenHouseOfferPeriod\n      isOpenHouseReviewPeriod\n      __typename\n    }\n    listingSource\n    cbsaSummary {\n      rentGrowthGraph {\n        values {\n          value\n          date\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    physical {\n      bathRooms\n      bedRooms\n      yearBuilt\n      squareFeet\n      lotSize\n      __typename\n    }\n    geoLocation {\n      hasStreetView\n      latitude\n      longitude\n      povLatitude\n      povLongitude\n      povHeading\n      povPitch\n      __typename\n    }\n    marketing {\n      marketingPoints\n      __typename\n    }\n    calculated(assumptions: $listingAssumptionInput) {\n      annualAppreciation\n      annualLoanInterestRate\n      appreciationType\n      capRate\n      cashFlow {\n        annualExpectedRent {\n          key\n          value\n          __typename\n        }\n        monthlyExpectedRent {\n          key\n          value\n          __typename\n        }\n        propertyTaxes {\n          key\n          value\n          __typename\n        }\n        repairsAndMaintenance {\n          key\n          value\n          __typename\n        }\n        otherExpenses {\n          key\n          value\n          __typename\n        }\n        annualNoi {\n          key\n          value\n          __typename\n        }\n        monthlyNoi {\n          key\n          value\n          __typename\n        }\n        capitalExpenses {\n          key\n          value\n          __typename\n        }\n        unleveredCashFlow {\n          key\n          value\n          __typename\n        }\n        annualLoanPayments {\n          key\n          value\n          __typename\n        }\n        monthlyLoanPayments {\n          key\n          value\n          __typename\n        }\n        annualNetCashFlow {\n          key\n          value\n          __typename\n        }\n        monthlyNetCashFlow {\n          key\n          value\n          __typename\n        }\n        __typename\n      }\n      cashOnCash\n      cashFlowGraph {\n        cashFlows\n        netRevenues\n        totalExpenses\n        loanPayments\n        __typename\n      }\n      closingCostAmount\n      closingCostPercent\n      downPayment\n      downPaymentPercentage\n      expectedRent\n      expensesAndReserves\n      financialsInYear\n      grossYield\n      initialInvestment\n      inspectionEstRepairCost\n      leverage\n      leveragePercentage\n      leveredCashFlow\n      leveredIrr\n      listPrice\n      loanAndAcquisitionFees\n      loanPayment\n      marketRent\n      marketRentSource\n      monthlyHoa\n      monthlyPropertyManagement\n      monthlyRent\n      netCashFlow\n      netCumCashFlow\n      netYield\n      proforma {\n        revenue {\n          grossRent {\n            key\n            value\n            __typename\n          }\n          economicVacancyFactor {\n            key\n            value\n            __typename\n          }\n          expectedRent {\n            key\n            value\n            __typename\n          }\n          monthlyExpectedRent {\n            key\n            value\n            __typename\n          }\n          __typename\n        }\n        expenses {\n          propertyManagement {\n            key\n            value\n            __typename\n          }\n          leasingFees {\n            key\n            value\n            __typename\n          }\n          hoaFees {\n            key\n            value\n            __typename\n          }\n          propertyTaxes {\n            key\n            value\n            __typename\n          }\n          insurance {\n            key\n            value\n            __typename\n          }\n          repairsAndMaintenance {\n            key\n            value\n            __typename\n          }\n          operatingExpenses {\n            key\n            value\n            __typename\n          }\n          monthlyNetOperatingIncome {\n            key\n            value\n            __typename\n          }\n          netOperatingIncome {\n            key\n            value\n            __typename\n          }\n          __typename\n        }\n        capitalExpenditures {\n          capitalExpenses {\n            key\n            value\n            __typename\n          }\n          totalExpenses {\n            key\n            value\n            __typename\n          }\n          unleveredCashFlow {\n            key\n            value\n            __typename\n          }\n          monthlyUnleveredCashFlow {\n            key\n            value\n            __typename\n          }\n          loanPayments {\n            key\n            value\n            __typename\n          }\n          monthlyLoanPayments {\n            key\n            value\n            __typename\n          }\n          leveredCashFlow {\n            key\n            value\n            __typename\n          }\n          monthlyLeveredCashFlow {\n            key\n            value\n            __typename\n          }\n          __typename\n        }\n        purchaseAndSale {\n          purchasePrice\n          salePrice\n          acquisitionFees\n          immediateRepairs\n          dispositionFees\n          closingCosts\n          netPurchase\n          saleProceeds\n          __typename\n        }\n        financing {\n          downPayment\n          loanFees\n          loanPayments {\n            key\n            value\n            __typename\n          }\n          loanBalance {\n            key\n            value\n            __typename\n          }\n          totalFinancing {\n            key\n            value\n            __typename\n          }\n          __typename\n        }\n        returns {\n          unleveredCashFlow {\n            key\n            value\n            __typename\n          }\n          leveredCashFlow {\n            key\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      propertyTaxes\n      propertyTaxType\n      propertyValue\n      rentType\n      reserveDeposit\n      reserveDepositPercentage\n      saleProceeds\n      saleProceedsTable {\n        propertyValueForecastInYear\n        propertyValueForecast\n        loanBalance\n        dispositionFees\n        __typename\n      }\n      totalReturn\n      totalReturnYear\n      valuationSource\n      yearlyInsuranceCost\n      yearlyPropertyTaxes\n      assumption {\n        assetManagement {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        rentGrowthRate\n        vacancyFactor {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        rent {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        expectedRent {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        propertyTaxes {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        propertyManagement {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        leasingFees {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        hoaFees {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        insurance {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        repairsAndMaintenance {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        operatingExpenses {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        netOperatingIncome {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        capitalExpenditures {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        totalUnleveredCashFlow {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        mortgage {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        totalNetCashFlow {\n          period\n          values {\n            dataType\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      totalReturnGraph {\n        cumulativeAppreciationGain\n        equityBuildUp\n        cumulativeNetCashFlow\n        totalInvestmentValue\n        __typename\n      }\n      totalReturnTable {\n        yearlyCumulativeNetCashFlow {\n          key\n          value\n          __typename\n        }\n        monthlyCumulativeNetCashFlow {\n          key\n          value\n          __typename\n        }\n        __typename\n      }\n      equityGraph {\n        propertyValues\n        loanBalances\n        equity\n        __typename\n      }\n      __typename\n    }\n    financial {\n      downPayment\n      reserveDepositPercentage\n      initialInvestment\n      isCashOnly\n      listPrice\n      propertyValuationHigh\n      propertyValuationLow\n      rentEstimateHigh\n      rentEstimateLow\n      __typename\n    }\n    score {\n      neighborhood\n      highSchool\n      middleSchool\n      elementarySchool\n      propertyCondition\n      floodZone\n      school\n      __typename\n    }\n    marketing {\n      description\n      featuredReason\n      highlights\n      isFeatured\n      marketingPoints\n      __typename\n    }\n    condition {\n      attic\n      basement\n      bathrooms\n      bedrooms\n      electrical\n      exterior\n      garage\n      hvac\n      kitchen\n      landscaping\n      plumbing\n      roof\n      structural\n      __typename\n    }\n    lease {\n      hasPet\n      isLeaseConcessions\n      isPetsDeposit\n      isRentersInsuranceRequired\n      isSection8\n      isTenantBackgroundChecked\n      isTenantIncomeAbove3x\n      isTenantMayTerminateEarly\n      isTenantPurchaseOption\n      latePaymentMonths\n      leaseEndDate\n      leaseStartDate\n      leasingStatus\n      marketedRent\n      monthlyRent\n      occupancy\n      paymentStatus\n      petFeeAmount\n      petsDepositAmount\n      securityDepositAmount\n      applianceOwnership {\n        dishwasher\n        dryer\n        microwave\n        refrigerator\n        stove\n        washer\n        __typename\n      }\n      utilitiesOwnership {\n        electric\n        garbage\n        gas\n        landscaping\n        pestControl\n        pool\n        water\n        __typename\n      }\n      __typename\n    }\n    resources {\n      floorPlans {\n        url\n        __typename\n      }\n      photos {\n        url\n        __typename\n      }\n      threeDRenderings {\n        url\n        __typename\n      }\n      diligenceVaultDocuments {\n        contentType\n        description\n        filename\n        guid\n        resourceType\n        sasUrl\n        textContent\n        url\n        __typename\n      }\n      __typename\n    }\n    address {\n      address1\n      address2\n      city\n      country\n      county\n      state\n      zip\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.roofstock.com/graphql',
            method='POST',
            headers={
                'Content-Type': 'application/json'
            },
            body=json.dumps(self.payload),
            callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.body)
        listings = data.get('data').get('filteredListings').get('data')
        for listing in listings:

            id = listing.get('id')
            
            ### 
            # 2 define variables to scrape
            visability1 = listing.get('visability'),
            is_rack= listing.get('isRack')
            hoa= listing.get('isHoa')
            status= listing.get('status')
            img_url= listing.get('mainImageUrl')
            marketName= listing.get('marketName')
            property_type= listing.get('propertyType')
            Seller= listing.get('sellerAccountName')
            daysOnMarket= listing.get('daysOnMarket')
            propertyType= listing.get('propertyType')

            # Address
            street1= listing.get('address').get('address1')
            unit= listing.get('address').get('address2')
            city= listing.get('address').get('city')
            country= listing.get('address').get('country')
            county= listing.get('address').get('county')
            state= listing.get('address').get('state')
            zip_code= listing.get('address').get('zip')
            # Calculated
            CAP_Rate1= listing.get('calculated').get('capRate')
            gross_yield1= listing.get('calculated').get('grossYield')
            potential_rent_growth= listing.get('calculated').get('hasPotentialRentGrowth')
            est_repair_cost1= listing.get('calculated').get('inspectionEstRepairCost')
            levered_IRR= listing.get('calculated').get('leveredIrr')
            list_price1= listing.get('calculated').get('listPrice')
            monthly_rent= listing.get('calculated').get('monthlyRent')
            property_value= listing.get('calculated').get('propertyValue')
            rent_type= listing.get('calculated').get('rentType')
            total_return1= listing.get('calculated').get('totalReturn')

            # Financial
            CAP_Rate2= listing.get('financial').get('capRate')
            gross_yield2= listing.get('financial').get('grossYield')
            est_repair_cost2= listing.get('financial').get('inspectionEstRepairCost')
            cash_only= listing.get('financial').get('isCashOnly')
            levered_irr= listing.get('financial').get('leveredIrr')
            list_price3= listing.get('financial').get('listPrice')
            market_rent= listing.get('financial').get('marketRent')
            charged_rent= listing.get('financial').get('monthlyRent')
            sales_price= listing.get('financial').get('salePrice')
            total_return2= listing.get('financial').get('totalReturn')

            # GeoLocation
            latitude= listing.get('geoLocation').get('latitude')
            longitude= listing.get('geoLocation').get('longitude')

            # Lease
            Section8= listing.get('lease').get('isSection8')
            lease_state= listing.get('lease').get('leaseStartDate')
            lease_end= listing.get('lease').get('leaseEndDate')
            occupancy= listing.get('lease').get('occupancy')

            # Physical
            bathrooms= listing.get('physical').get('bathRooms')
            bedrooms= listing.get('physical').get('bedrooms')
            sq_foot= listing.get('physical').get('squareFeet')
            yr_built= listing.get('physical').get('yearBuilt')

            # Schools
            elementary_school= listing.get('score').get('elementarySchool')
            middle_school= listing.get('score').get('middleSchool')
            high_school= listing.get('score').get('highSchool')
            neighborhood= listing.get('score').get('neighborhood')

            # update teh payload with the current house_id
            self.payload_house_json['variables']['listingInput']['listingId'] = id

            # add a callback method where we can catch the response
            # from each request sent to each house
            yield scrapy.Request(
                url='https://www.roofstock.com/graphql',
                method='POST',
                headers={
                    'content-type': 'application/json'
                },
                body=json.dumps(self.payload_house_json),
                callback=self.parse_house,
                # add meta
                meta={
                    'visability1': visability1,
                    'is_rack': is_rack,
                    'hoa': hoa,
                    'status': status ,
                    'img_url': img_url ,
                    'marketName': marketName ,
                    'property_type': property_type ,
                    'Seller': Seller ,
                    'daysOnMarket': daysOnMarket ,
                    'propertyType': propertyType ,

                    # Address
                    'street1': street1,
                    'unit': unit,
                    'city': city,
                    'country': country,
                    'county': county,
                    'state': state,
                    'zip_code': zip_code,

                    # Calculated
                    'CAP_Rate1': CAP_Rate1,
                    'gross_yield1': gross_yield1,
                    'potential_rent_growth': potential_rent_growth,
                    'est_repair_cost1': est_repair_cost1,
                    'levered_IRR': levered_IRR,
                    'list_price1': list_price1,
                    'monthly_rent': monthly_rent,
                    'property_value': property_value,
                    'rent_type': rent_type,
                    'total_return1': total_return1,

                    # Financial
                    'CAP_Rate2': CAP_Rate2,
                    'gross_yield2': gross_yield2,
                    'est_repair_cost2': est_repair_cost2,
                    'cash_only?':cash_only ,
                    'levered_irr': levered_irr,
                    'list_price3': list_price3,
                    'market_rent': market_rent,
                    'charged_rent': charged_rent,
                    'sales_price': sales_price,
                    'total_return2': total_return2,

                    # GeoLocation
                    'latitude': latitude,
                    'longitude': longitude,

                    # Lease
                    'Section8':Section8 ,
                    'lease_state': lease_state,
                    'lease_end': lease_end,
                    'occupancy': occupancy,

                    # Physical
                    'bathrooms': bathrooms,
                    'bedrooms': bedrooms,
                    'sq_foot': sq_foot,
                    'yr_built': yr_built,

                    # Schools
                    'elementary_school': elementary_school,
                    'middle_school': middle_school,
                    'high_school': high_school,
                    'neighborhood': neighborhood,
                }
            )

        total_records = data.get('data').get('filteredListings').get('pageInfo').get('recordsTotal')
        page_size = data.get('data').get('filteredListings').get('pageInfo').get('pageSize')
        pagination = total_records // page_size

        if self.payload['variables']['filteredListingsInput']['criteria']['paging']['pageNumber'] <= pagination:
            self.payload['variables']['filteredListingsInput']['criteria']['paging']['pageNumber'] += 1


            yield scrapy.Request(
                url="https://www.roofstock.com/graphql",
                method="POST",
                body=json.dumps(self.payload),
                headers={
                    'Content-Type': 'application/json'
                },
                dont_filter=True

            )

    # parse each house
    def parse_house(self, response):
        house = json.loads(response.body)
        id = house.get('data').get('listing').get('id')
        visibility = house.get('data').get('listing').get('visibility')
        isHoa = house.get('data').get('listing').get('isHoa')
        partner_listing = house.get('data').get('listing').get('isPartnerListing')
        rent_guaranteed = house.get('data').get('listing').get('isRentGuaranteed')

        # Address
        address1 = house.get('data').get('listing').get('address').get('address1')
        address2 = house.get('data').get('listing').get('address').get('address2')
        city = house.get('data').get('listing').get('address').get('city')
        county = house.get('data').get('listing').get('address').get('county')
        state = house.get('data').get('listing').get('address').get('state')
        zip = house.get('data').get('listing').get('address').get('zip')

        # calculated
        annual_appreciation = house.get('data').get('listing').get('calculated').get('annualAppreciation')
        annual_loan_int_rate = house.get('data').get('listing').get('calculated').get('annualLoanInterestRate')
        appreciation_type = house.get('data').get('listing').get('calculated').get('appreciationType')

        # Assumption
        asset_mgmt = house.get('data').get('listing').get('calculated').get('assumption').get('assetManagement')
        rent_growth_rate = house.get('data').get('listing').get('calculated').get('assumption').get('rentGrowthRate')

        # Capital Expenditures
        cap_ex_period = house.get('data').get('listing').get('calculated').get('assumption').get('capitalExpenditures')[0].get('period')
        cap_ex_percentage = house.get('data').get('listing').get('calculated').get('assumption').get('capitalExpenditures')[0].get('values')[0].get('value')
        cap_ex_amount = house.get('data').get('listing').get('calculated').get('assumption').get('capitalExpenditures')[0].get('values')[1].get('value')

        # Expected Rent
        expected_annual_rent = house.get('data').get('listing').get('calculated').get('assumption').get('expectedRent')[0].get('values')[1].get('value')
        expected_monthly_rent = house.get('data').get('listing').get('calculated').get('assumption').get('expectedRent')[1].get('values')[1].get('value')

        # Insurance
        insurance_annual_percent = house.get('data').get('listing').get('calculated').get('assumption').get('insurance')[0].get('values')[0].get('value')
        insurance_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('insurance')[0].get('values')[1].get('value')
        insurance_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('insurance')[1].get('values')[0].get('value')
        insurance_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('insurance')[1].get('values')[1].get('value')

        # Leasing Fees
        leasing_fee_annual_percent = house.get('data').get('listing').get('calculated').get('assumption').get('leasingFees')[0].get('values')[0].get('value')
        leasing_fee_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('leasingFees')[0].get('values')[1].get('value')
        leasing_fee_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('leasingFees')[1].get('values')[0].get('value')
        leasing_fee_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('leasingFees')[1].get('values')[1].get('value')

        # netOperatingIncome
        noi_annual_percent = house.get('data').get('listing').get('calculated').get('assumption').get('netOperatingIncome')[0].get('values')[0].get('value')
        noi_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('netOperatingIncome')[0].get('values')[1].get('value')
        noi_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('netOperatingIncome')[1].get('values')[0].get('value')
        noi_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('netOperatingIncome')[1].get('values')[1].get('value')

        # op expenses
        op_exp_annual_percent = house.get('data').get('listing').get('calculated').get('assumption').get('operatingExpenses')[0].get('values')[0].get('value')
        op_exp_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('operatingExpenses')[0].get('values')[1].get('value')
        op_exp_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('operatingExpenses')[1].get('values')[0].get('value')
        op_exp_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('operatingExpenses')[1].get('values')[1].get('value')

        # property management
        property_mgmt_annual_percent = house.get('data').get('listing').get('calculated').get('assumption').get('propertyManagement')[0].get('values')[0].get('value')
        property_mgmt_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('propertyManagement')[0].get('values')[1].get('value')
        property_mgmt_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('propertyManagement')[1].get('values')[0].get('value')
        property_mgmt_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('propertyManagement')[1].get('values')[1].get('value')

        # property taxes
        property_tax_annual_percent = house.get('data').get('listing').get('calculated').get('assumption').get('propertyTaxes')[0].get('values')[0].get('value')
        property_tax_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('propertyTaxes')[0].get('values')[1].get('value')
        property_tax_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('propertyTaxes')[1].get('values')[0].get('value')
        property_tax_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('propertyTaxes')[1].get('values')[1].get('value')

        # rent
        rent_annual_percent = house.get('data').get('listing').get('calculated').get('assumption').get('rent')[0].get('values')[0].get('value')
        rent_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('rent')[0].get('values')[1].get('value')
        rent_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('rent')[1].get('values')[0].get('value')
        rent_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('rent')[1].get('values')[1].get('value')

        # repairs
        repairs_percent = house.get('data').get('listing').get('calculated').get('assumption').get('repairsAndMaintenance')[0].get('values')[0].get('value')
        repairs_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('repairsAndMaintenance')[0].get('values')[1].get('value')
        repairs_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('repairsAndMaintenance')[1].get('values')[0].get('value')
        repairs_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('repairsAndMaintenance')[1].get('values')[1].get('value')

        # total net cash flow
        total_net_cash_flow_percent = house.get('data').get('listing').get('calculated').get('assumption').get('totalNetCashFlow')[0].get('values')[0].get('value')
        total_net_cash_flow_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('totalNetCashFlow')[0].get('values')[1].get('value')
        total_net_cash_flow_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('totalNetCashFlow')[1].get('values')[0].get('value')
        total_net_cash_flow_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('totalNetCashFlow')[1].get('values')[1].get('value')

        # total_unlevered_cash_flow
        total_unlevered_cash_flow_percent = house.get('data').get('listing').get('calculated').get('assumption').get('totalUnleveredCashFlow')[0].get('values')[0].get('value')
        total_unlevered_cash_flow_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('totalUnleveredCashFlow')[0].get('values')[1].get('value')
        total_unlevered_cash_flow_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('totalUnleveredCashFlow')[1].get('values')[0].get('value')
        total_unlevered_cash_flow_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('totalUnleveredCashFlow')[1].get('values')[1].get('value')

        # total_unlevered_cash_flow
        total_unlevered_cash_flow_percent = house.get('data').get('listing').get('calculated').get('assumption').get('totalUnleveredCashFlow')[0].get('values')[0].get('value')
        total_unlevered_cash_flow_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('totalUnleveredCashFlow')[0].get('values')[1].get('value')
        total_unlevered_cash_flow_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('totalUnleveredCashFlow')[1].get('values')[0].get('value')
        total_unlevered_cash_flow_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('totalUnleveredCashFlow')[1].get('values')[1].get('value')

        # vacancy factor
        vacancy_factor_percent = house.get('data').get('listing').get('calculated').get('assumption').get('vacancyFactor')[0].get('values')[0].get('value')
        vacancy_factor_annual_amt = house.get('data').get('listing').get('calculated').get('assumption').get('vacancyFactor')[0].get('values')[1].get('value')
        vacancy_factor_monthly_percent = house.get('data').get('listing').get('calculated').get('assumption').get('vacancyFactor')[1].get('values')[0].get('value')
        vacancy_factor_monthly_amt = house.get('data').get('listing').get('calculated').get('assumption').get('vacancyFactor')[1].get('values')[1].get('value')

        # capRate
        cap_rate = house.get('data').get('listing').get('calculated').get('assumption').get('capRate')

        # cash flow expected annual rent
        y1_annual_exp_rent = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualExpectedRent')[0].get('value')
        y5_annual_exp_rent = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualExpectedRent')[1].get('value')
        y10_annual_exp_rent = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualExpectedRent')[2].get('value')

        # cash flow expected annual loan payments
        y1_annual_loan_pmt = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualLoanPayments')[0].get('value')
        y5_annual_loan_pmt = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualLoanPayments')[1].get('value')
        y10_annual_loan_pmt = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualLoanPayments')[2].get('value')

        # cash flow expected annual net cash flow
        y1_annual_net_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualNetCashFlow')[0].get('value')
        y5_annual_net_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualNetCashFlow')[1].get('value')
        y10_annual_net_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualNetCashFlow')[2].get('value')

        # cash flow expected annual noi
        y1_annual_noi = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualNoi')[0].get('value')
        y5_annual_noi = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualNoi')[1].get('value')
        y10_annual_noi = house.get('data').get('listing').get('calculated').get('cashFlow').get('annualNoi')[2].get('value')

        # cash flow expected capital Expenses
        y1_annual_cap_exp = house.get('data').get('listing').get('calculated').get('cashFlow').get('capitalExpenses')[0].get('value')
        y5_annual_cap_exp = house.get('data').get('listing').get('calculated').get('cashFlow').get('capitalExpenses')[1].get('value')
        y10_annual_cap_exp = house.get('data').get('listing').get('calculated').get('cashFlow').get('capitalExpenses')[2].get('value')

        # cash flow expected monthly exp rent
        y1_monthly_exp_rent = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyExpectedRent')[0].get('value')
        y5_monthly_exp_rent = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyExpectedRent')[1].get('value')
        y10_monthly_exp_rent = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyExpectedRent')[2].get('value')

        # cash flow monthly loan pmts
        y1_monthly_loan_pmts = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyLoanPayments')[0].get('value')
        y5_monthly_loan_pmts = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyLoanPayments')[1].get('value')
        y10_monthly_loan_pmts = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyLoanPayments')[2].get('value')

        # cash flow expected monthly net cash flow
        y1_monthly_net_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyNetCashFlow')[0].get('value')
        y5_monthly_net_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyNetCashFlow')[1].get('value')
        y10_monthly_net_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyNetCashFlow')[2].get('value')

        # cash flow expected monthly noi
        y1_monthly_noi = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyNoi')[0].get('value')
        y5_monthly_noi = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyNoi')[1].get('value')
        y10_monthly_noi = house.get('data').get('listing').get('calculated').get('cashFlow').get('monthlyNoi')[2].get('value')

        # cash flow annual other expenses
        y1_annual_other_exp = house.get('data').get('listing').get('calculated').get('cashFlow').get('otherExpenses')[0].get('value')
        y5_annual_other_exp = house.get('data').get('listing').get('calculated').get('cashFlow').get('otherExpenses')[1].get('value')
        y10_annual_other_exp = house.get('data').get('listing').get('calculated').get('cashFlow').get('otherExpenses')[2].get('value')

        # cash flow expected annual property taxes
        y1_annual_property_taxes = house.get('data').get('listing').get('calculated').get('cashFlow').get('propertyTaxes')[0].get('value')
        y5_annual_property_taxes = house.get('data').get('listing').get('calculated').get('cashFlow').get('propertyTaxes')[1].get('value')
        y10_annual_property_taxes = house.get('data').get('listing').get('calculated').get('cashFlow').get('propertyTaxes')[2].get('value')

        # cash flow expected annual repairs and maintenance
        y1_annual_maintenance = house.get('data').get('listing').get('calculated').get('cashFlow').get('repairsAndMaintenance')[0].get('value')
        y5_annual_maintenance = house.get('data').get('listing').get('calculated').get('cashFlow').get('repairsAndMaintenance')[1].get('value')
        y10_annual_maintenance = house.get('data').get('listing').get('calculated').get('cashFlow').get('repairsAndMaintenance')[2].get('value')

        # cash flow expected unlevered cf
        y1_annual_unlevered_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('unleveredCashFlow')[0].get('value')
        y5_annual_unlevered_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('unleveredCashFlow')[1].get('value')
        y10_annual_unlevered_cf = house.get('data').get('listing').get('calculated').get('cashFlow').get('unleveredCashFlow')[2].get('value')

        # cash flow graph cashflows
        y1_annual_cf = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('cashFlows')[0]
        y2_annual_cf = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('cashFlows')[1]
        y3_annual_cf = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('cashFlows')[2]
        y4_annual_cf = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('cashFlows')[3]
        y5_annual_cf = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('cashFlows')[4]

        # cash flow graph loan payments
        y1_annual_loan_pmt = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('loanPayments')[0]
        y2_annual_loan_pmt = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('loanPayments')[1]
        y3_annual_loan_pmt = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('loanPayments')[2]
        y4_annual_loan_pmt = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('loanPayments')[3]
        y5_annual_loan_pmt = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('loanPayments')[4]

        # cash flow graph net rev
        y1_annual_net_rev = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('netRevenues')[0]
        y2_annual_net_rev = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('netRevenues')[1]
        y3_annual_net_rev = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('netRevenues')[2]
        y4_annual_net_rev = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('netRevenues')[3]
        y5_annual_net_rev = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('netRevenues')[4]

        # cash flow graph total exp
        y1_annual_total_epx = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('totalExpenses')[0]
        y2_annual_total_epx = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('totalExpenses')[1]
        y3_annual_total_epx = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('totalExpenses')[2]
        y4_annual_total_epx = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('totalExpenses')[3]
        y5_annual_total_epx = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('totalExpenses')[4]

        #misc
        cash_on_cash = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('cashOnCash')
        closing_cost_amt = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('closingCostAmount')
        closing_cost_perc = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('closingCostPercent')
        down_pmt_amt = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('downPayment')
        down_pmt_perc = house.get('data').get('listing').get('calculated').get('cashFlowGraph').get('downPaymentPercentage')

        # equity graph - equity
        y1_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[0]
        y2_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[1]
        y3_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[2]
        y4_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[3]
        y5_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[4]
        y6_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[5]
        y7_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[6]
        y8_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[7]
        y9_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[8]
        y10_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[9]
        y11_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[10]
        y12_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[11]
        y13_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[12]
        y14_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[13]
        y15_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[14]
        y16_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[15]
        y17_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[16]
        y18_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[17]
        y19_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[18]
        y20_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[19]
        y21_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[20]
        y22_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[21]
        y23_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[22]
        y24_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[23]
        y25_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[24]
        y26_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[25]
        y27_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[26]
        y28_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[27]
        y29_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[28]
        y30_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[29]
        y31_equity = house.get('data').get('listing').get('calculated').get('equityGraph').get('equity')[30]

        # equity graph - loan balance
        y1_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[0]
        y2_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[1]
        y3_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[2]
        y4_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[3]
        y5_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[4]
        y6_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[5]
        y7_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[6]
        y8_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[7]
        y9_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[8]
        y10_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[9]
        y11_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[10]
        y12_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[11]
        y13_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[12]
        y14_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[13]
        y15_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[14]
        y16_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[15]
        y17_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[16]
        y18_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[17]
        y19_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[18]
        y20_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[19]
        y21_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[20]
        y22_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[21]
        y23_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[22]
        y24_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[23]
        y25_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[24]
        y26_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[25]
        y27_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[26]
        y28_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[27]
        y29_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[28]
        y30_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[29]
        y31_loan_balance = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanBalances')[30]

        # equity graph - property values
        y1_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[0]
        y2_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[1]
        y3_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[2]
        y4_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[3]
        y5_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[4]
        y6_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[5]
        y7_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[6]
        y8_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[7]
        y9_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[8]
        y10_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[9]
        y11_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[10]
        y12_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[11]
        y13_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[12]
        y14_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[13]
        y15_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[14]
        y16_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[15]
        y17_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[16]
        y18_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[17]
        y19_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[18]
        y20_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[19]
        y21_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[20]
        y22_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[21]
        y23_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[22]
        y24_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[23]
        y25_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[24]
        y26_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[25]
        y27_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[26]
        y28_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[27]
        y29_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[28]
        y30_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[29]
        y31_property_value = house.get('data').get('listing').get('calculated').get('equityGraph').get('propertyValues')[30]

        # equity graph - misc
        expected_rent = house.get('data').get('listing').get('calculated').get('equityGraph').get('expectedRent')
        exp_and_reserves = house.get('data').get('listing').get('calculated').get('equityGraph').get('expensesAndReserves')
        financials_yr1 = house.get('data').get('listing').get('calculated').get('equityGraph').get('financialsInYear')
        gross_yield = house.get('data').get('listing').get('calculated').get('equityGraph').get('grossYield')
        initial_investment = house.get('data').get('listing').get('calculated').get('equityGraph').get('initialInvestment')
        inspection_repair_cost = house.get('data').get('listing').get('calculated').get('equityGraph').get('inspectionEstRepairCost')
        leverage = house.get('data').get('listing').get('calculated').get('equityGraph').get('leverage')
        leverage_percent = house.get('data').get('listing').get('calculated').get('equityGraph').get('leveragePercentage')
        levered_CF = house.get('data').get('listing').get('calculated').get('equityGraph').get('leveredCashFlow')
        levered_IRR = house.get('data').get('listing').get('calculated').get('equityGraph').get('leveredIrr')
        list_price = house.get('data').get('listing').get('calculated').get('equityGraph').get('listPrice')
        loan_acquisition_fee = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanAndAcquisitionFees')
        loan_pmt = house.get('data').get('listing').get('calculated').get('equityGraph').get('loanPayment')
        mkt_rent = house.get('data').get('listing').get('calculated').get('equityGraph').get('marketRent')
        mkt_rent_source = house.get('data').get('listing').get('calculated').get('equityGraph').get('marketRentSource')
        monthly_HOA = house.get('data').get('listing').get('calculated').get('equityGraph').get('monthlyHoa')
        monthly_property_mgmt = house.get('data').get('listing').get('calculated').get('equityGraph').get('monthlyPropertyManagement')
        monthly_rent = house.get('data').get('listing').get('calculated').get('equityGraph').get('monthlyRent')
        net_CF = house.get('data').get('listing').get('calculated').get('equityGraph').get('netCashFlow')
        net_cum_CF = house.get('data').get('listing').get('calculated').get('equityGraph').get('netCumCashFlow')
        net_yield = house.get('data').get('listing').get('calculated').get('equityGraph').get('net')

        # proforma cap exp
        y1_proforma_cap_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('capitalExpenses')[0].get('value')
        y2_proforma_cap_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('capitalExpenses')[1].get('value')
        y3_proforma_cap_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('capitalExpenses')[2].get('value')
        y4_proforma_cap_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('capitalExpenses')[3].get('value')
        y5_proforma_cap_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('capitalExpenses')[4].get('value')

        # proforma levered CF
        y1_proforma_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('leveredCashFlow')[0].get('value')
        y2_proforma_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('leveredCashFlow')[1].get('value')
        y3_proforma_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('leveredCashFlow')[2].get('value')
        y4_proforma_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('leveredCashFlow')[3].get('value')
        y5_proforma_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('leveredCashFlow')[4].get('value')

        # proforma loan pmts
        y1_proforma_loan_pmts = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('loanPayments')[0].get('value')
        y2_proforma_loan_pmts = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('loanPayments')[1].get('value')
        y3_proforma_loan_pmts = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('loanPayments')[2].get('value')
        y4_proforma_loan_pmts = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('loanPayments')[3].get('value')
        y5_proforma_loan_pmts = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('loanPayments')[4].get('value')

        # proforma monthly levered CF
        y1_proforma_monthly_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('monthlyUnleveredCashFlow')[0].get('value')
        y2_proforma_monthly_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('monthlyUnleveredCashFlow')[1].get('value')
        y3_proforma_monthly_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('monthlyUnleveredCashFlow')[2].get('value')
        y4_proforma_monthly_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('monthlyUnleveredCashFlow')[3].get('value')
        y5_proforma__monthly_levered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('monthlyUnleveredCashFlow')[4].get('value')

        # proforma total expenses
        y1_proforma_total_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('totalExpenses')[0].get('value')
        y2_proforma_total_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('totalExpenses')[1].get('value')
        y3_proforma_total_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('totalExpenses')[2].get('value')
        y4_proforma_total_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('totalExpenses')[3].get('value')
        y5_proforma_total_exp = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('totalExpenses')[4].get('value')

        # proforma unlevered CF
        y1_proforma_unlevered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('unleveredCashFlow')[0].get('value')
        y2_proforma_unlevered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('unleveredCashFlow')[1].get('value')
        y3_proforma_unlevered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('unleveredCashFlow')[2].get('value')
        y4_proforma_unlevered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('unleveredCashFlow')[3].get('value')
        y5_proforma_unlevered_CF = house.get('data').get('listing').get('calculated').get('proforma').get('capitalExpenditures').get('unleveredCashFlow')[4].get('value')

        # Condition
        condition_attic = house.get('data').get('listing').get('condition').get('attic')
        condition_basement = house.get('data').get('listing').get('condition').get('basement')
        condition_bathrooms = house.get('data').get('listing').get('condition').get('bathrooms')
        condition_bedrooms = house.get('data').get('listing').get('condition').get('bedrooms')
        condition_electrical = house.get('data').get('listing').get('condition').get('electrical')
        condition_exterior = house.get('data').get('listing').get('condition').get('exterior')
        condition_hvac = house.get('data').get('listing').get('condition').get('hvac')
        condition_kitchen = house.get('data').get('listing').get('condition').get('kitchen')
        condition_landscaping = house.get('data').get('listing').get('condition').get('landscaping')
        condition_plumbing = house.get('data').get('listing').get('condition').get('plumbing')
        condition_roof = house.get('data').get('listing').get('condition').get('roof')
        condition_structural = house.get('data').get('listing').get('condition').get('structural')

        # Marketing
        marketing_points = house.get('data').get('listing').get('marketing').get('marketingPoints')

        #resources
        dd0_content_type = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[0].get('contentType')
        dd0_description = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[0].get('description')
        dd0_filename = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[0].get('filename')
        dd0_guid = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[0].get('guid')
        dd0_resourceType = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[0].get('resourceType')
        dd0_sasUrl = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[0].get('sasUrl')
        dd0_textContent = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[0].get('textContent')
        dd0_url = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[0].get('url')

        dd1_content_type = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[1].get('contentType')
        dd1_description = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[1].get('description')
        dd1_filename = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[1].get('filename')
        dd1_guid = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[1].get('guid')
        dd1_resourceType = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[1].get('resourceType')
        dd1_sasUrl = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[1].get('sasUrl')
        dd1_textContent = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[1].get('textContent')
        dd1_url = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[1].get('url')

        dd2_content_type = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[2].get('contentType')
        dd2_description = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[2].get('description')
        dd2_filename = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[2].get('filename')
        dd2_guid = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[2].get('guid')
        dd2_resourceType = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[2].get('resourceType')
        dd2_sasUrl = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[2].get('sasUrl')
        dd2_textContent = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[2].get('textContent')
        dd2_url = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[2].get('url')

        dd3_content_type = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[3].get('contentType')
        dd3_description = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[3].get('description')
        dd3_filename = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[3].get('filename')
        dd3_guid = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[3].get('guid')
        dd3_resourceType = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[3].get('resourceType')
        dd3_sasUrl = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[3].get('sasUrl')
        dd3_textContent = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[3].get('textContent')
        dd3_url = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[3].get('url')

        dd4_content_type = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[4].get('contentType')
        dd4_description = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[4].get('description')
        dd4_filename = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[4].get('filename')
        dd4_guid = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[4].get('guid')
        dd4_resourceType = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[4].get('resourceType')
        dd4_sasUrl = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[4].get('sasUrl')
        dd4_textContent = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[4].get('textContent')
        dd4_url = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[4].get('url')

        dd5_content_type = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[5].get('contentType')
        dd5_description = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[5].get('description')
        dd5_filename = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[5].get('filename')
        dd5_guid = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[5].get('guid')
        dd5_resourceType = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[5].get('resourceType')
        dd5_sasUrl = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[5].get('sasUrl')
        dd5_textContent = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[5].get('textContent')
        dd5_url = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[5].get('url')

        try:
            dd6_content_type = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[6].get('contentType')
        except IndexError:
            pass
        try:
            dd6_description = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[6].get('description')
        except IndexError:
            pass

        try:
            dd6_filename = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[6].get('filename')
        except IndexError:
            pass

        try:
            dd6_guid = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[6].get('guid')
        except IndexError:
            pass

        try:
            dd6_resourceType = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[6].get('resourceType')
        except IndexError:
            pass

        try:
            dd6_sasUrl = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[6].get('sasUrl')
        except IndexError:
            pass

        try:
            dd6_textContent = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[6].get('textContent')
        except IndexError:
            pass

        try:
            dd6_url = house.get('data').get('listing').get('resources').get('diligenceVaultDocuments')[6].get('url')
        except IndexError:
            pass


        # Photos
        photo1 = house.get('data').get('listing').get('resources').get('photos')[0].get('url')
        # photo2 = house.get('data').get('listing').get('resources').get('photos')[1].get('url')
        # photo3 = house.get('data').get('listing').get('resources').get('photos')[2].get('url')
        # photo4 = house.get('data').get('listing').get('resources').get('photos')[3].get('url')
        # photo5 = house.get('data').get('listing').get('resources').get('photos')[4].get('url')

        # schools and neighboor
        elementry_score = house.get('data').get('listing').get('score').get('elementarySchool')
        floodZone = house.get('data').get('listing').get('score').get('floodZone')
        highschool_score = house.get('data').get('listing').get('score').get('highSchool')
        middle_score = house.get('data').get('listing').get('score').get('middleSchool')
        neighborhood_score = house.get('data').get('listing').get('score').get('neighborhood')
        property_condition_score = house.get('data').get('listing').get('score').get('propertyCondition')
        school_score = house.get('data').get('listing').get('score').get('school')




        property_type = house.get('data').get('listing').get('propertyType')
        cbsa_code = house.get('data').get('listing').get('cbsaCode')
        try:
            yield {
                # add meta objects
                'visability1': response.meta['visability1'],
                'is_rack': response.meta['is_rack'],
                'hoa': response.meta['hoa'],
                'status': response.meta['status'],
                'img_url': response.meta['img_url'],
                'marketName': response.meta['marketName'],
                'property_type': response.meta['property_type'],
                'Seller': response.meta['Seller'],
                'daysOnMarket': response.meta['daysOnMarket'],
                'propertyType': response.meta['propertyType'],

                # Address
                'street1': response.meta['street1'],
                'unit': response.meta['unit'],
                'city': response.meta['city'],
                'country': response.meta['country'],
                'county': response.meta['county'],
                'state': response.meta['state'],
                'zip_code': response.meta['zip_code'],

                # Calculated
                'CAP_Rate1': response.meta['CAP_Rate1'],
                'gross_yield1': response.meta['gross_yield1'],
                'potential_rent_growth': response.meta['potential_rent_growth'],
                'est_repair_cost1': response.meta['est_repair_cost1'],
                'levered_IRR': response.meta['levered_IRR'],
                'list_price1': response.meta['list_price1'],
                'monthly_rent': response.meta['monthly_rent'],
                'property_value': response.meta['property_value'],
                'rent_type': response.meta['rent_type'],
                'total_return1': response.meta['total_return1'],

                # Financial
                'CAP_Rate2': response.meta['CAP_Rate2'],
                'gross_yield2': response.meta['gross_yield2'],
                'est_repair_cost2': response.meta['est_repair_cost2'],
                # 'cash_only1':response.meta['cash_only'],
                'levered_irr': response.meta['levered_irr'],
                'list_price3': response.meta['list_price3'],
                'market_rent': response.meta['market_rent'],
                'charged_rent': response.meta['charged_rent'],
                'sales_price': response.meta['sales_price'],
                'total_return2': response.meta['total_return2'],

                # GeoLocation
                'latitude': response.meta['latitude'],
                'longitude': response.meta['longitude'],

                # Lease
                'Section8':response.meta['Section8'],
                'lease_state': response.meta['lease_state'],
                'lease_end': response.meta['lease_end'],
                'occupancy': response.meta['occupancy'],

                # Physical
                'bathrooms': response.meta['bathrooms'],
                'bedrooms': response.meta['bedrooms'],
                'sq_foot': response.meta['sq_foot'],
                'yr_built': response.meta['yr_built'],

                # Schools
                'elementary_school': response.meta['elementary_school'],
                'middle_school': response.meta['middle_school'],
                'high_school': response.meta['high_school'],
                'neighborhood': response.meta['neighborhood'],



                'id': id,
                'isHoa' : isHoa,
                'partner_listing' : partner_listing,
                'rent_guaranteed' : rent_guaranteed,
                'address1' : address1,
                'address2' : address2,
                'city1' : city,
                'county1' : county,
                'state1' : state,
                'zip' : zip,
                'annual_appreciation' : annual_appreciation,
                'annual_loan_int_rate' : annual_loan_int_rate,
                'appreciation_type' : appreciation_type,
                'asset_mgmt' : asset_mgmt,
                'rent_growth_rate' : rent_growth_rate,
                'cap_ex_period' : cap_ex_period,
                'cap_ex_percentage' : cap_ex_percentage,
                'cap_ex_amount' : cap_ex_amount,
                'expected_annual_rent' : expected_annual_rent,
                'expected_monthly_rent' : expected_monthly_rent,
                'insurance_annual_percent' : insurance_annual_percent,
                'insurance_annual_amt' : insurance_annual_amt,
                'insurance_monthly_percent' : insurance_monthly_percent,
                'insurance_monthly_amt' : insurance_monthly_amt,
                'leasing_fee_annual_percent' : leasing_fee_annual_percent,
                'leasing_fee_annual_amt' : leasing_fee_annual_amt,
                'leasing_fee_monthly_percent' : leasing_fee_monthly_percent,
                'leasing_fee_monthly_amt' : leasing_fee_monthly_amt,
                'noi_annual_percent' : noi_annual_percent,
                'noi_annual_amt' : noi_annual_amt,
                'noi_monthly_percent' : noi_monthly_percent,
                'noi_monthly_amt' : noi_monthly_amt,
                'op_exp_annual_percent' : op_exp_annual_percent,
                'op_exp_annual_amt' : op_exp_annual_amt,
                'op_exp_monthly_percent' : op_exp_monthly_percent,
                'op_exp_monthly_amt' : op_exp_monthly_amt,
                'property_mgmt_annual_percent' : property_mgmt_annual_percent,
                'property_mgmt_annual_amt' : property_mgmt_annual_amt,
                'property_mgmt_monthly_percent' : property_mgmt_monthly_percent,
                'property_mgmt_monthly_amt' : property_mgmt_monthly_amt,
                'property_tax_annual_percent' : property_tax_annual_percent,
                'property_tax_annual_amt' : property_tax_annual_amt,
                'property_tax_monthly_percent' : property_tax_monthly_percent,
                'property_tax_monthly_amt' : property_tax_monthly_amt,
                'rent_annual_percent' : rent_annual_percent,
                'rent_annual_amt' : rent_annual_amt,
                'rent_monthly_percent' : rent_monthly_percent,
                'rent_monthly_amt' : rent_monthly_amt,
                'repairs_percent' : repairs_percent,
                'repairs_annual_amt' : repairs_annual_amt,
                'repairs_monthly_percent' : repairs_monthly_percent,
                'repairs_monthly_amt' : repairs_monthly_amt,
                'total_net_cash_flow_percent' : total_net_cash_flow_percent,
                'total_net_cash_flow_annual_amt' : total_net_cash_flow_annual_amt,
                'total_net_cash_flow_monthly_percent' : total_net_cash_flow_monthly_percent,
                'total_net_cash_flow_monthly_amt' : total_net_cash_flow_monthly_amt,
                'total_unlevered_cash_flow_percent' : total_unlevered_cash_flow_percent,
                'total_unlevered_cash_flow_annual_amt' : total_unlevered_cash_flow_annual_amt,
                'total_unlevered_cash_flow_monthly_percent' : total_unlevered_cash_flow_monthly_percent,
                'total_unlevered_cash_flow_monthly_amt' : total_unlevered_cash_flow_monthly_amt,
                'vacancy_factor_percent' : vacancy_factor_percent,
                'vacancy_factor_annual_amt' : vacancy_factor_annual_amt,
                'vacancy_factor_monthly_percent' : vacancy_factor_monthly_percent,
                'vacancy_factor_monthly_amt' : vacancy_factor_monthly_amt,
                'cap_rate' : cap_rate,
                'y1_annual_exp_rent' : y1_annual_exp_rent,
                'y5_annual_exp_rent' : y5_annual_exp_rent,
                'y10_annual_exp_rent' : y10_annual_exp_rent,
                'y10_annual_loan_pmt' : y10_annual_loan_pmt,
                'y1_annual_net_cf' : y1_annual_net_cf,
                'y5_annual_net_cf' : y5_annual_net_cf,
                'y10_annual_net_cf' : y10_annual_net_cf,
                'y1_annual_noi' : y1_annual_noi,
                'y5_annual_noi' : y5_annual_noi,
                'y10_annual_noi' : y10_annual_noi,
                'y1_annual_cap_exp' : y1_annual_cap_exp,
                'y5_annual_cap_exp' : y5_annual_cap_exp,
                'y10_annual_cap_exp' : y10_annual_cap_exp,
                'y1_monthly_exp_rent' : y1_monthly_exp_rent,
                'y5_monthly_exp_rent' : y5_monthly_exp_rent,
                'y10_monthly_exp_rent' : y10_monthly_exp_rent,
                'y1_monthly_loan_pmts' : y1_monthly_loan_pmts,
                'y5_monthly_loan_pmts' : y5_monthly_loan_pmts,
                'y10_monthly_loan_pmts' : y10_monthly_loan_pmts,
                'y1_monthly_net_cf' : y1_monthly_net_cf,
                'y5_monthly_net_cf' : y5_monthly_net_cf,
                'y10_monthly_net_cf' : y10_monthly_net_cf,
                'y1_monthly_noi' : y1_monthly_noi,
                'y5_monthly_noi' : y5_monthly_noi,
                'y10_monthly_noi' : y10_monthly_noi,
                'y1_annual_other_exp' : y1_annual_other_exp,
                'y5_annual_other_exp' : y5_annual_other_exp,
                'y10_annual_other_exp' : y10_annual_other_exp,
                'y1_annual_property_taxes' : y1_annual_property_taxes,
                'y5_annual_property_taxes' : y5_annual_property_taxes,
                'y10_annual_property_taxes' : y10_annual_property_taxes,
                'y1_annual_maintenance' : y1_annual_maintenance,
                'y5_annual_maintenance' : y5_annual_maintenance,
                'y10_annual_maintenance' : y10_annual_maintenance,
                'y1_annual_unlevered_cf' : y1_annual_unlevered_cf,
                'y5_annual_unlevered_cf' : y5_annual_unlevered_cf,
                'y10_annual_unlevered_cf' : y10_annual_unlevered_cf,
                'y1_annual_cf' : y1_annual_cf,
                'y2_annual_cf' : y2_annual_cf,
                'y3_annual_cf' : y3_annual_cf,
                'y4_annual_cf' : y4_annual_cf,
                'y5_annual_cf' : y5_annual_cf,
                'y1_annual_loan_pmt' : y1_annual_loan_pmt,
                'y2_annual_loan_pmt' : y2_annual_loan_pmt,
                'y3_annual_loan_pmt' : y3_annual_loan_pmt,
                'y4_annual_loan_pmt' : y4_annual_loan_pmt,
                'y5_annual_loan_pmt' : y5_annual_loan_pmt,
                'y1_annual_net_rev' : y1_annual_net_rev,
                'y2_annual_net_rev' : y2_annual_net_rev,
                'y3_annual_net_rev' : y3_annual_net_rev,
                'y4_annual_net_rev' : y4_annual_net_rev,
                'y5_annual_net_rev' : y5_annual_net_rev,
                'y1_annual_total_epx' : y1_annual_total_epx,
                'y2_annual_total_epx' : y2_annual_total_epx,
                'y3_annual_total_epx' : y3_annual_total_epx,
                'y4_annual_total_epx' : y4_annual_total_epx,
                'y5_annual_total_epx' : y5_annual_total_epx,
                'cash_on_cash' : cash_on_cash,
                'closing_cost_amt' : closing_cost_amt,
                'closing_cost_perc' : closing_cost_perc,
                'down_pmt_amt' : down_pmt_amt,
                'down_pmt_perc' : down_pmt_perc,
                'y1_equity' : y1_equity,
                'y2_equity' : y2_equity,
                'y3_equity' : y3_equity,
                'y4_equity' : y4_equity,
                'y5_equity' : y5_equity,
                'y6_equity' : y6_equity,
                'y7_equity' : y7_equity,
                'y8_equity' : y8_equity,
                'y9_equity' : y9_equity,
                'y10_equity' : y10_equity,
                'y11_equity' : y11_equity,
                'y12_equity' : y12_equity,
                'y13_equity' : y13_equity,
                'y14_equity' : y14_equity,
                'y15_equity' : y15_equity,
                'y16_equity' : y16_equity,
                'y17_equity' : y17_equity,
                'y18_equity' : y18_equity,
                'y19_equity' : y19_equity,
                'y20_equity' : y20_equity,
                'y21_equity' : y21_equity,
                'y22_equity' : y22_equity,
                'y23_equity' : y23_equity,
                'y24_equity' : y24_equity,
                'y25_equity' : y25_equity,
                'y26_equity' : y26_equity,
                'y27_equity' : y27_equity,
                'y28_equity' : y28_equity,
                'y29_equity' : y29_equity,
                'y30_equity' : y30_equity,
                'y31_equity' : y31_equity,
                'y1_loan_balance' : y1_loan_balance,
                'y2_loan_balance' : y2_loan_balance,
                'y3_loan_balance' : y3_loan_balance,
                'y4_loan_balance' : y4_loan_balance,
                'y5_loan_balance' : y5_loan_balance,
                'y6_loan_balance' : y6_loan_balance,
                'y7_loan_balance' : y7_loan_balance,
                'y8_loan_balance' : y8_loan_balance,
                'y9_loan_balance' : y9_loan_balance,
                'y10_loan_balance' : y10_loan_balance,
                'y11_loan_balance' : y11_loan_balance,
                'y12_loan_balance' : y12_loan_balance,
                'y13_loan_balance' : y13_loan_balance,
                'y14_loan_balance' : y14_loan_balance,
                'y15_loan_balance' : y15_loan_balance,
                'y16_loan_balance' : y16_loan_balance,
                'y17_loan_balance' : y17_loan_balance,
                'y18_loan_balance' : y18_loan_balance,
                'y19_loan_balance' : y19_loan_balance,
                'y20_loan_balance' : y20_loan_balance,
                'y21_loan_balance' : y21_loan_balance,
                'y22_loan_balance' : y22_loan_balance,
                'y23_loan_balance' : y23_loan_balance,
                'y24_loan_balance' : y24_loan_balance,
                'y25_loan_balance' : y25_loan_balance,
                'y26_loan_balance' : y26_loan_balance,
                'y27_loan_balance' : y27_loan_balance,
                'y28_loan_balance' : y28_loan_balance,
                'y29_loan_balance' : y29_loan_balance,
                'y30_loan_balance' : y30_loan_balance,
                'y31_loan_balance' : y31_loan_balance,
                'y1_property_value' : y1_property_value,
                'y2_property_value' : y2_property_value,
                'y3_property_value' : y3_property_value,
                'y4_property_value' : y4_property_value,
                'y5_property_value' : y5_property_value,
                'y6_property_value' : y6_property_value,
                'y7_property_value' : y7_property_value,
                'y8_property_value' : y8_property_value,
                'y9_property_value' : y9_property_value,
                'y10_property_value' : y10_property_value,
                'y11_property_value' : y11_property_value,
                'y12_property_value' : y12_property_value,
                'y13_property_value' : y13_property_value,
                'y14_property_value' : y14_property_value,
                'y15_property_value' : y15_property_value,
                'y16_property_value' : y16_property_value,
                'y17_property_value' : y17_property_value,
                'y18_property_value' : y18_property_value,
                'y19_property_value' : y19_property_value,
                'y20_property_value' : y20_property_value,
                'y21_property_value' : y21_property_value,
                'y22_property_value' : y22_property_value,
                'y23_property_value' : y23_property_value,
                'y24_property_value' : y24_property_value,
                'y25_property_value' : y25_property_value,
                'y26_property_value' : y26_property_value,
                'y27_property_value' : y27_property_value,
                'y28_property_value' : y28_property_value,
                'y29_property_value' : y29_property_value,
                'y30_property_value' : y30_property_value,
                'y31_property_value' : y31_property_value,
                'expected_rent' : expected_rent,
                'exp_and_reserves' : exp_and_reserves,
                'financials_yr1' : financials_yr1,
                'gross_yield' : gross_yield,
                'initial_investment' : initial_investment,
                'inspection_repair_cost' : inspection_repair_cost,
                'leverage' : leverage,
                'leverage_percent' : leverage_percent,
                'levered_CF' : levered_CF,
                'levered_IRR1' : levered_IRR,
                'list_price' : list_price,
                'loan_acquisition_fee' : loan_acquisition_fee,
                'loan_pmt' : loan_pmt,
                'mkt_rent' : mkt_rent,
                'mkt_rent_source' : mkt_rent_source,
                'monthly_HOA' : monthly_HOA,
                'monthly_property_mgmt' : monthly_property_mgmt,
                'monthly_rent1' : monthly_rent,
                'net_CF' : net_CF,
                'net_cum_CF' : net_cum_CF,
                'net_yield' : net_yield,
                'y1_proforma_cap_exp' : y1_proforma_cap_exp,
                'y2_proforma_cap_exp' : y2_proforma_cap_exp,
                'y3_proforma_cap_exp' : y3_proforma_cap_exp,
                'y4_proforma_cap_exp' : y4_proforma_cap_exp,
                'y5_proforma_cap_exp' : y5_proforma_cap_exp,
                'y1_proforma_levered_CF' : y1_proforma_levered_CF,
                'y2_proforma_levered_CF' : y2_proforma_levered_CF,
                'y3_proforma_levered_CF' : y3_proforma_levered_CF,
                'y4_proforma_levered_CF' : y4_proforma_levered_CF,
                'y5_proforma_levered_CF' : y5_proforma_levered_CF,
                'y1_proforma_loan_pmts' : y1_proforma_loan_pmts,
                'y2_proforma_loan_pmts' : y2_proforma_loan_pmts,
                'y3_proforma_loan_pmts' : y3_proforma_loan_pmts,
                'y4_proforma_loan_pmts' : y4_proforma_loan_pmts,
                'y5_proforma_loan_pmts' : y5_proforma_loan_pmts,
                'y1_proforma_monthly_levered_CF' : y1_proforma_monthly_levered_CF,
                'y2_proforma_monthly_levered_CF' : y2_proforma_monthly_levered_CF,
                'y3_proforma_monthly_levered_CF' : y3_proforma_monthly_levered_CF,
                'y4_proforma_monthly_levered_CF' : y4_proforma_monthly_levered_CF,
                'y5_proforma__monthly_levered_CF' : y5_proforma__monthly_levered_CF,
                'y1_proforma_total_exp' : y1_proforma_total_exp,
                'y2_proforma_total_exp' : y2_proforma_total_exp,
                'y3_proforma_total_exp' : y3_proforma_total_exp,
                'y4_proforma_total_exp' : y4_proforma_total_exp,
                'y5_proforma_total_exp' : y5_proforma_total_exp,
                'y1_proforma_unlevered_CF' : y1_proforma_unlevered_CF,
                'y2_proforma_unlevered_CF' : y2_proforma_unlevered_CF,
                'y3_proforma_unlevered_CF' : y3_proforma_unlevered_CF,
                'y4_proforma_unlevered_CF' : y4_proforma_unlevered_CF,
                'y5_proforma_unlevered_CF' : y5_proforma_unlevered_CF,
                'condition_attic' : condition_attic,
                'condition_basement' : condition_basement,
                'condition_bathrooms' : condition_bathrooms,
                'condition_bedrooms' : condition_bedrooms,
                'condition_electrical' : condition_electrical,
                'condition_exterior' : condition_exterior,
                'condition_hvac' : condition_hvac,
                'condition_kitchen' : condition_kitchen,
                'condition_landscaping' : condition_landscaping,
                'condition_plumbing' : condition_plumbing,
                'condition_roof' : condition_roof,
                'condition_structural' : condition_structural,
                'marketing_points' : marketing_points,
                'dd0_content_type' : dd0_content_type,
                'dd0_description' : dd0_description,
                'dd0_filename' : dd0_filename,
                'dd0_guid' : dd0_guid,
                'dd0_resourceType' : dd0_resourceType,
                'dd0_sasUrl' : dd0_sasUrl,
                'dd0_textContent' : dd0_textContent,
                'dd0_url' : dd0_url,
                'dd1_content_type' : dd1_content_type,
                'dd1_description' : dd1_description,
                'dd1_filename' : dd1_filename,
                'dd1_guid' : dd1_guid,
                'dd1_resourceType' : dd1_resourceType,
                'dd1_sasUrl' : dd1_sasUrl,
                'dd1_textContent' : dd1_textContent,
                'dd1_url' : dd1_url,
                'dd2_content_type' : dd2_content_type,
                'dd2_description' : dd2_description,
                'dd2_filename' : dd2_filename,
                'dd2_guid' : dd2_guid,
                'dd2_resourceType' : dd2_resourceType,
                'dd2_sasUrl' : dd2_sasUrl,
                'dd2_textContent' : dd2_textContent,
                'dd2_url' : dd2_url,
                'dd3_content_type' : dd3_content_type,
                'dd3_description' : dd3_description,
                'dd3_filename' : dd3_filename,
                'dd3_guid' : dd3_guid,
                'dd3_resourceType' : dd3_resourceType,
                'dd3_sasUrl' : dd3_sasUrl,
                'dd3_textContent' : dd3_textContent,
                'dd3_url' : dd3_url,
                'dd4_content_type' : dd4_content_type,
                'dd4_description' : dd4_description,
                'dd4_filename' : dd4_filename,
                'dd4_guid' : dd4_guid,
                'dd4_resourceType' : dd4_resourceType,
                'dd4_sasUrl' : dd4_sasUrl,
                'dd4_textContent' : dd4_textContent,
                'dd4_url' : dd4_url,
                'dd5_content_type' : dd5_content_type,
                'dd5_description' : dd5_description,
                'dd5_filename' : dd5_filename,
                'dd5_guid' : dd5_guid,
                'dd5_resourceType' : dd5_resourceType,
                'dd5_sasUrl' : dd5_sasUrl,
                'dd5_textContent' : dd5_textContent,
                'dd5_url' : dd5_url,
                # 'dd6_content_type' : dd6_content_type,
                # 'dd6_description' : dd6_description,
                # 'dd6_filename' : dd6_filename,
                # 'dd6_guid' : dd6_guid,
                # 'dd6_resourceType' : dd6_resourceType,
                # 'dd6_sasUrl' : dd6_sasUrl,
                # 'dd6_textContent' : dd6_textContent,
                # 'dd6_url' : dd6_url,
                'photo1' : photo1,
                # 'photo2' : photo2,
                # 'photo3' : photo3,
                # 'photo4' : photo4,
                # 'photo5' : photo5,
                'elementry_score' : elementry_score,
                'floodZone' : floodZone,
                'highschool_score' : highschool_score,
                'middle_score' : middle_score,
                'neighborhood_score' : neighborhood_score,
                'property_condition_score' : property_condition_score,
                'school_score' : school_score,
                'property_type1' : property_type,
                'cbsa_code' : cbsa_code,
        }
        except (IndexError, UnboundLocalError):
            print("element missing")
