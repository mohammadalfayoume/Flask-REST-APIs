from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id= fields.Str(dump_only=True)
    name= fields.Str(required=True)
    price= fields.Float(required=True)
    
class PlainStoreSchema(Schema):
    id= fields.Str(dump_only=True)
    name= fields.Str(required=True)
    
class ItemUpdateSchema(Schema):
    name= fields.Str()
    price= fields.Float()
    store_id= fields.Int()

class ItemSchema(PlainItemSchema):
    store_id= fields.Int(required=True, load_only=True)
    store= fields.Nested(PlainStoreSchema(), dump_only=True)

# class PlainTagSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str()
    
class StoreSchema(PlainStoreSchema):
    items= fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
#     tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

# class TagSchema(PlainTagSchema):
#     store_id = fields.Int(load_only=True)
#     store = fields.Nested(PlainStoreSchema(), dump_only=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username= fields.Str(required=True)
    password= fields.Str(required=True, load_only=True)
    # load_only=True it means that I don't want return the password in the response
    # dump_only=True it means that the client doesn't have to insert the id because it is auto generated 