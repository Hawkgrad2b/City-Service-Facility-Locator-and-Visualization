#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:13:40 2023

@author: Sriram Pemmaraju
"""

#-------------------------------------------------------
from project1Phase2 import *
#-------------------------------------------------------

# main program
cityList = []
coordList = []
popList = []
distanceList = []

loadData(cityList, coordList, popList, distanceList)


tests = []

# Test 1
tests.append(sorted(locateFacilities(cityList, distanceList, 5000)) == ['Youngstown OH'])

# Test 2
tests.append(sorted(locateFacilities(cityList, distanceList, 1000)) == ['Twin Falls ID', 'Vincennes IN', 'Wichita Falls TX', 'Winston-Salem NC', 'Yankton SD'])

# Test 3
tests.append(sorted(locateFacilities(cityList, distanceList, 500)) == ['Salida CO', 'Sioux City IA', 'Sterling CO', 'Steubenville OH', 'Stockton CA', 'Tucson AZ', 'Valdosta GA', 'Waco TX', 'Walla Walla WA', 'Wichita Falls TX', 'Winnipeg MB', 'Wisconsin Dells WI', 'Worcester MA'])

# Test 4
tests.append(sorted(locateFacilities(cityList, distanceList, 200)) == ['Richmond IN', 'Rockford IL', 'Salem OR', 'Salt Lake City UT', 'San Angelo TX', 'Santa Ana CA', 'Santa Fe NM', 'Sarasota FL', 'Schenectady NY', 'Sheridan WY', 'Sherman TX', 'Sterling CO', 'Stockton CA', 'Topeka KS', 'Traverse City MI', 'Trinidad CO', 'Tucson AZ', 'Tulsa OK', 'Tuscaloosa AL', 'Twin Falls ID', 'Vancouver BC', 'Vicksburg MS', 'Victoria TX', 'Vincennes IN', 'Warren PA', 'Washington DC', 'Watertown SD', 'Wausau WI', 'Waycross GA', 'Weed CA', 'Wenatchee WA', 'Williamson WV', 'Williston ND', 'Wilmington NC', 'Winnipeg MB', 'Winston-Salem NC', 'Wisconsin Dells WI', 'Yakima WA', 'Yankton SD'])

# Test 5
tests.append(sorted(locateFacilities(cityList, distanceList, 100)) == ['Red Bluff CA', 'Regina SK', 'Reno NV', 'Richfield UT', 'Richmond VA', 'Rock Springs WY', 'Rocky Mount NC', 'Roswell NM', 'Saginaw MI', 'Saint Augustine FL', 'Saint Johnsbury VT', 'Saint Louis MO', 'Saint Paul MN', 'Salem OR', 'Salida CO', 'Salisbury MD', 'Salt Lake City UT', 'San Angelo TX', 'San Antonio TX', 'San Francisco CA', 'San Jose CA', 'Santa Ana CA', 'Santa Barbara CA', 'Santa Fe NM', 'Sault Sainte Marie MI', 'Schenectady NY', 'Scottsbluff NE', 'Sedalia MO', 'Sheridan WY', 'Sherman TX', 'Shreveport LA', 'South Bend IN', 'Spokane WA', 'Springfield IL', 'Springfield MO', 'Springfield OH', 'Staunton VA', 'Sterling CO', 'Steubenville OH', 'Stevens Point WI', 'Sumter SC', 'Swainsboro GA', 'Syracuse NY', 'Tacoma WA', 'Tampa FL', 'Toledo OH', 'Topeka KS', 'Toronto ON', 'Traverse City MI', 'Trenton NJ', 'Trinidad CO', 'Tucson AZ', 'Tulsa OK', 'Tupelo MS', 'Tuscaloosa AL', 'Twin Falls ID', 'Utica NY', 'Valdosta GA', 'Valley City ND', 'Vancouver BC', 'Vicksburg MS', 'Victoria TX', 'Vincennes IN', 'Waco TX', 'Walla Walla WA', 'Warren PA', 'Waterloo IA', 'Watertown SD', 'Waukegan IL', 'Weed CA', 'Wenatchee WA', 'West Palm Beach FL', 'Wichita Falls TX', 'Wichita KS', 'Williamson WV', 'Williamsport PA', 'Williston ND', 'Wilmington NC', 'Winchester VA', 'Winnipeg MB', 'Winston-Salem NC', 'Worcester MA', 'Yakima WA', 'Yankton SD'])

# Test 6
tests.append(sorted(locateFacilities(cityList, distanceList, 50)) == ['Reading PA', 'Red Bluff CA', 'Regina SK', 'Reno NV', 'Rhinelander WI', 'Richfield UT', 'Richmond IN', 'Richmond VA', 'Roanoke VA', 'Rochester MN', 'Rochester NY', 'Rock Springs WY', 'Rockford IL', 'Rocky Mount NC', 'Roswell NM', 'Rutland VT', 'Saginaw MI', 'Saint Augustine FL', 'Saint Cloud MN', 'Saint Johnsbury VT', 'Saint Joseph MO', 'Saint Louis MO', 'Saint Paul MN', 'Salem OR', 'Salida CO', 'Salina KS', 'Salinas CA', 'Salisbury MD', 'Salt Lake City UT', 'San Angelo TX', 'San Antonio TX', 'San Bernardino CA', 'San Diego CA', 'San Jose CA', 'Sandusky OH', 'Santa Ana CA', 'Santa Barbara CA', 'Santa Fe NM', 'Santa Rosa CA', 'Sarasota FL', 'Sault Sainte Marie MI', 'Savannah GA', 'Schenectady NY', 'Scottsbluff NE', 'Sedalia MO', 'Selma AL', 'Seminole OK', 'Sheridan WY', 'Sherman TX', 'Shreveport LA', 'Sioux City IA', 'Sioux Falls SD', 'South Bend IN', 'Spokane WA', 'Springfield IL', 'Springfield MO', 'Springfield OH', 'Staunton VA', 'Sterling CO', 'Stockton CA', 'Stroudsburg PA', 'Sumter SC', 'Swainsboro GA', 'Syracuse NY', 'Tacoma WA', 'Tallahassee FL', 'Tampa FL', 'Terre Haute IN', 'Texarkana TX', 'Toledo OH', 'Topeka KS', 'Toronto ON', 'Traverse City MI', 'Trenton NJ', 'Trinidad CO', 'Tucson AZ', 'Tulsa OK', 'Tupelo MS', 'Tuscaloosa AL', 'Twin Falls ID', 'Tyler TX', 'Uniontown PA', 'Utica NY', 'Valdosta GA', 'Valley City ND', 'Vancouver BC', 'Vicksburg MS', 'Victoria TX', 'Vincennes IN', 'Waco TX', 'Walla Walla WA', 'Warren PA', 'Washington DC', 'Waterbury CT', 'Waterloo IA', 'Watertown NY', 'Watertown SD', 'Waukegan IL', 'Wausau WI', 'Waycross GA', 'Weed CA', 'Wenatchee WA', 'West Palm Beach FL', 'Wheeling WV', 'Wichita Falls TX', 'Wichita KS', 'Williamson WV', 'Williamsport PA', 'Williston ND', 'Wilmington DE', 'Wilmington NC', 'Winchester VA', 'Winnipeg MB', 'Winston-Salem NC', 'Wisconsin Dells WI', 'Worcester MA', 'Yakima WA', 'Yankton SD', 'Youngstown OH'])

# Test 7
tests.append(sorted(locateFacilities(cityList, distanceList, 10)) == ['Ravenna OH', 'Reading PA', 'Red Bluff CA', 'Regina SK', 'Reno NV', 'Rhinelander WI', 'Richfield UT', 'Richmond IN', 'Richmond VA', 'Roanoke VA', 'Rochester MN', 'Rochester NY', 'Rock Springs WY', 'Rockford IL', 'Rocky Mount NC', 'Roswell NM', 'Rutland VT', 'Sacramento CA', 'Saginaw MI', 'Saint Augustine FL', 'Saint Cloud MN', 'Saint Johnsbury VT', 'Saint Joseph MI', 'Saint Joseph MO', 'Saint Louis MO', 'Saint Paul MN', 'Salem OR', 'Salida CO', 'Salina KS', 'Salinas CA', 'Salisbury MD', 'Salt Lake City UT', 'San Angelo TX', 'San Antonio TX', 'San Bernardino CA', 'San Diego CA', 'San Francisco CA', 'San Jose CA', 'Sandusky OH', 'Santa Ana CA', 'Santa Barbara CA', 'Santa Fe NM', 'Santa Rosa CA', 'Sarasota FL', 'Sault Sainte Marie MI', 'Savannah GA', 'Schenectady NY', 'Scottsbluff NE', 'Scranton PA', 'Seattle WA', 'Sedalia MO', 'Selma AL', 'Seminole OK', 'Sheridan WY', 'Sherman TX', 'Shreveport LA', 'Sioux City IA', 'Sioux Falls SD', 'South Bend IN', 'Spokane WA', 'Springfield IL', 'Springfield MA', 'Springfield MO', 'Springfield OH', 'Staunton VA', 'Sterling CO', 'Steubenville OH', 'Stevens Point WI', 'Stockton CA', 'Stroudsburg PA', 'Sumter SC', 'Swainsboro GA', 'Syracuse NY', 'Tacoma WA', 'Tallahassee FL', 'Tampa FL', 'Terre Haute IN', 'Texarkana TX', 'Toledo OH', 'Topeka KS', 'Toronto ON', 'Traverse City MI', 'Trenton NJ', 'Trinidad CO', 'Tucson AZ', 'Tulsa OK', 'Tupelo MS', 'Tuscaloosa AL', 'Twin Falls ID', 'Tyler TX', 'Uniontown PA', 'Utica NY', 'Valdosta GA', 'Valley City ND', 'Vancouver BC', 'Vicksburg MS', 'Victoria TX', 'Vincennes IN', 'Waco TX', 'Walla Walla WA', 'Warren PA', 'Washington DC', 'Waterbury CT', 'Waterloo IA', 'Watertown NY', 'Watertown SD', 'Waukegan IL', 'Wausau WI', 'Waycross GA', 'Weed CA', 'Wenatchee WA', 'West Palm Beach FL', 'Wheeling WV', 'Wichita Falls TX', 'Wichita KS', 'Williamson WV', 'Williamsport PA', 'Williston ND', 'Wilmington DE', 'Wilmington NC', 'Winchester VA', 'Winnipeg MB', 'Winston-Salem NC', 'Wisconsin Dells WI', 'Worcester MA', 'Yakima WA', 'Yankton SD', 'Youngstown OH']

)

# Output the test results
i = 0
for result in tests:
    if not result:
        print("Test", i + 1, "failed")
    i = i + 1