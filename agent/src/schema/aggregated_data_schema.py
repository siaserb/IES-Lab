from marshmallow import Schema, fields
from schema.accelerometer_schema import AccelerometerSchema
from schema.gps_schema import GpsSchema
from domain.aggregated_data import AggregatedData
from schema.parking_schema import ParkingSchema

class AggregatedDataSchema(Schema):
    accelerometer = fields.Nested(AccelerometerSchema)
    gps = fields.Nested(GpsSchema)
    parking = fields.Nested(ParkingSchema)
    timestamp = fields.DateTime('iso')
    user_id = fields.Int()

# class AggregatedDataSchema(Schema):
#     road_state = fields.Str() # Added road_state field
#     agent_data = fields.Nested({
#         "user_id": fields.Int(),
#         "accelerometer": fields.Nested(AccelerometerSchema),
#         "gps": fields.Nested(GpsSchema),
#         "timestamp": fields.DateTime('iso')
#     })