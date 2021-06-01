# Football-API-prediction-sofascore-

This is complete Football API

we get complete ready API with json file, And we can run our MACHINE learning model on the json data.

Description of file Detail.

get-h2hScore-API.py

    from this we will make the API of H2H score,which ever date we want,just enter the < dateOfTheMatch = {{ $date }} >
    And this will create a json file and store it into sofa-API folder with H2H-API-$date.json
    
  
get-prediction-API.py

    here we can fetch the json data from sofa-api folder and run our machine learning model on the json data.
    
  
update-predictionResult.py

    here we update our result in prediction folder json file, with comparing the prediction and actual result. and making the prediction False or True.
    
  
seprateResult.py

      if we want to run our model on old dataset, the we can fetch the api with result and it will separate the match
      (i,e. h2hscore API and actual result in different file)
      h2h sofa api will go to the seprate file and result will go to the separate folder that is result folder.

      Run your model on h2h-API score and compare with the actual result API that is in result folder.
  

status.py

      we have make the prediction, fetch the actual result, update the True, False on our prediction data.
      Then we want to see our prediction status or graph, that how many % our model working correctly.
      This will show us the total match, no of win, no of loss and then % of winning.
  
# And you can even get more detail, like away score, home score and more....

Instead of making this many json file, you can even store that json in your db, And here Django Restframework will be easy, where you can create model, and serialize for model and push your data with help serializer  to backend.

    MongoDB and for that mongo-engine will be good, because this is document(non-structure data).


  
    
  
