# NYC Transportation Analytics: Taxi vs. Citi Bike

Team Members: Matthew Chen, Andrew Jiang, Adam Soliman

Directory Structure
- `data_ingest/` contains the ingestion jobs used to prepare source datasets before merging.
- `ana_code/` contains analytic (model training and visualization) code used after cleaning.
- - `ana_code/model_training/` contains code used when training the model.
  - - `ana_code/transport_model_local/` contains the model itself.
    - - `ana_code/model_viz.ipynb` is the interactive map visualization of the model. 
- `etl_code/` contains cleaning and merge jobs for the combined transportation + weather dataset.
- `profiling_code/` contains record counts, schema checks, and other quick validation scripts.
- `screenshots/` stores project screenshots for different steps of the pipeline.
- - `screenshots/model+predictions` contains screenshots specifically for the interactive map vizualization of the model. 

## Where to find results of a run: 

- Taxi ingest output defaults to `hdfs:///user/aes10130_nyu_edu/final_project/processed_taxi`.
- Bike ingest output defaults to `hdfs:///user/aes10130_nyu_edu/final_project/processed_citibike_data`.
- Weather ingest output defaults to `hdfs:///user/aes10130_nyu_edu/final_project/processed_weather`.
- The merged cleaned dataset is written to `hdfs:///user/aes10130_nyu_edu/final_project/merged_data`.
- Intermediate and analysis outputs are generally written to user-specific HDFS folders referenced inside each Scala file.

## Where you can find the input data that we used: 
- Taxi input data can be found at: `hdfs:///user/aes10130_nyu_edu/final_project/yellow_taxi_raw`.
- Bike input data can be found at: `hdfs:///user/mc9967_nyu_edu/citibike_data`.
- Weather input data can be found at: `hdfs:///user/aj3556_nyu_edu/final_project/NYC_Weather_2016_2022.csv`.

## How to run our model: 
- Download the transport_model_local folder and model_viz.ipynb, which are located in the ana_code directory
- Open model_viz.ipynb and ensure that the model_path variable points to your local transport_model_local path
- Run the notebook and select two points on the map to receive a prediction
- To test different conditions, locate the handle_click function and modify time_hours, temp_f, season, beaufort_scale, and precipitation_mm in the test_row variable 

Alternatively, to run the model without a visualization, 
- Download the transport_model_local folder located in the ana_code directory
- For Spark, load and run the model using the following code:
```bash
import org.apache.spark.ml.PipelineModel
val model = PipelineModel.load("transport_model_local")
val predictions = model.transform(inputDF)
predictions.select("prediction").show()
```
- For Python, load and run the model using the following code:
```bash
from pyspark.ml import PipelineModel
model = PipelineModel.load("transport_model_local")
predictions = model.transform(inputDF)
predictions.select("prediction").show()
```
