import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node albums
albums_node1739416286952 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotifyproject-data/staging/albums.csv"], "recurse": True}, transformation_ctx="albums_node1739416286952")

# Script generated for node artist
artist_node1739416287524 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotifyproject-data/staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1739416287524")

# Script generated for node track
track_node1739416288030 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotifyproject-data/staging/track.csv"], "recurse": True}, transformation_ctx="track_node1739416288030")

# Script generated for node Join Album and Artist
JoinAlbumandArtist_node1739416431273 = Join.apply(frame1=artist_node1739416287524, frame2=albums_node1739416286952, keys1=["id"], keys2=["artist_id"], transformation_ctx="JoinAlbumandArtist_node1739416431273")

# Script generated for node Join
Join_node1739416593783 = Join.apply(frame1=track_node1739416288030, frame2=JoinAlbumandArtist_node1739416431273, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Join_node1739416593783")

# Script generated for node Drop Fields
DropFields_node1739416676196 = DropFields.apply(frame=Join_node1739416593783, paths=["track_id", "id"], transformation_ctx="DropFields_node1739416676196")

# Script generated for node Destination
EvaluateDataQuality().process_rows(frame=DropFields_node1739416676196, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1739416281146", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Destination_node1739416717710 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1739416676196, connection_type="s3", format="glueparquet", connection_options={"path": "s3://spotifyproject-data/data-warehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1739416717710")

job.commit()
