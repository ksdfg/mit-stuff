# Lab Assignment 1

- **BDA Panel Number** : 3

- **Roll Number** : PB31

- **Name** : Kshitish Deshpande

## Outputs

### use

#### Purpose

Switch current database to a given db.

#### Input

```
> use ksdfg
```

#### Output

```
switched to db ksdfg
```

### createCollection

#### Purpose

Creates a new collection

#### Input

```
> db.createCollection("anime")
```

#### Output

```
{ "ok" : 1 }
```

### show collections

#### Purpose

Print a list of all collections for current database

#### Input

```
> show collections
```

#### Output

```
anime
```

### insert

#### Purpose

Insert a document or documents into a collection

#### Input

```
> db.anime.insert(
...     {
...         name: "Hunter x Hunter",
...         status: "finished",
...         episodes: 148,
...         studio: "Madhouse"
...     }
... )
```

#### Output

```
WriteResult({ "nInserted" : 1 })
```

### insertMany

#### Purpose

Insert multiple documents into a collection

#### Input

```
> db.anime.insertMany(
...     [
...         {
...             name: "Naruto",
...             status: "finished",
...             episodes: 220,
...             studio: "Studio Pierrot"
...         },
...         {
...             name: "Naruto Shippuden",
...             episodes: 500,
...             status: "finished",
...             studio: "Studio Pierrot"
...         }
...     ]
... )
```

#### Output

```
{
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("5f24304abd8dd9ff39206b5c"),
                ObjectId("5f24304abd8dd9ff39206b5d")
        ]
}
```

### insertOne

#### Purpose

Insert a single document into a collection

#### Input

```
> db.anime.insertOne(
...     {
...         name: "Afro Samurai",
...         status: "finished",
...         type: "Movie",
...         studio: "Gonzo"
...     }
... )
```

#### Output

```
{
        "acknowledged" : true,
        "insertedId" : ObjectId("5f243262bd8dd9ff39206b5e")
}
```

### deleteOne

#### Purpose

Removes a single document from a collection

#### Input

```
> db.anime.deleteOne({name: "Girly Air Force"})
```

#### Output

```
{ "acknowledged" : true, "deletedCount" : 1 }
```

### deleteMany

#### Purpose

Remove all documents that match the filter from a collection

#### Input

```
> db.anime.deleteMany({episodes: 12})
```

#### Output

```
{ "acknowledged" : true, "deletedCount" : 2 }
```

### dropDatabase

#### Purpose

Removes current database, deleting all associated data files

#### Input

```
> db.dropDatabase()
```

#### Output

```
{ "ok" : 1 }
```

### rmeove

#### Purpose

Removes documents from a collection

#### Input

```
> db.anime.remove(
...     {
...         episodes: { $lt: 100 }
...     }
... )
```

#### Output

```
WriteResult({ "nRemoved" : 2 })
```

### update

#### Purpose

Modifies existing document(s) in a collection

#### Input

```
> db.anime.update(
...     { type: { $exists: false } },
...     { $set: { type: "TV" } },
...     { multi: true }
... )
```

#### Output

```
WriteResult({ "nMatched" : 3, "nUpserted" : 0, "nModified" : 3 })
```

### updateOne

#### Purpose

Updates a single document in the collection based on the filter

#### Input

```
> db.anime.updateOne(
...     { status: "finished" },
...     { $set: { status: "Finished airing" } }
... )
```

#### Output

```
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

### updateMany

#### Purpose

Updates all documents that match the specified filter for a collection

#### Input

```
> db.anime.updateMany(
...     { status: "finished" },
...     { $set: { status: "Finished airing" } }
... )
```

#### Output

```
{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }
```

### save

#### Purpose

Updates an existing document or inserts a new one if it doesn't exist

#### Input

```
> db.anime.save(
...     {
...         name: "Girl's Last Tour",
...         type: "TV",
...         status: "Finished Airing",
...         episodes: 12,
...         studio: "White Fox"
...     }
... )
```

#### Output

```
WriteResult({ "nInserted" : 1 })
```

### find

#### Purpose

Selects documents in a collection and returns a cursor to the selected documents

#### Input

```
> db.anime.find( { type: "TV" } )
```

#### Output

```
{ "_id" : ObjectId("5f24304abd8dd9ff39206b5c"), "name" : "Naruto", "status" : "Finished airing", "episodes" : 220, "studio" : "Studio Pierrot", "type" : "TV" }
{ "_id" : ObjectId("5f24304abd8dd9ff39206b5d"), "name" : "Naruto Shippuden", "episodes" : 500, "status" : "Finished airing", "studio" : "Studio Pierrot", "type" : "TV" }
{ "_id" : ObjectId("5f243742bd8dd9ff39206b64"), "name" : "Hunter x Hunter", "status" : "Finished airing", "episodes" : 148, "studio" : "Madhouse", "type" : "TV" }
{ "_id" : ObjectId("5f243a1dbd8dd9ff39206b65"), "name" : "Girl's Last Tour", "type" : "TV", "status" : "Finished Airing", "episodes" : 12, "studio" : "White Fox" }
```

### findOne

#### Purpose

Returns one document that satisfies the specified query criteria on the collection

#### Input

```
> db.anime.findOne( { type: "TV" } )
```

#### Output

```
{
        "_id" : ObjectId("5f24304abd8dd9ff39206b5c"),
        "name" : "Naruto",
        "status" : "Finished airing",
        "episodes" : 220,
        "studio" : "Studio Pierrot",
        "type" : "TV"
}
```

### drop

#### Purpose

Removes a collection from the database

#### Input

```
> db.review.drop()
```

#### Output

```
true
```