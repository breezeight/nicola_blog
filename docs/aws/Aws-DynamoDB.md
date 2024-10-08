# DynamoDB

Ref:

- https://docs.google.com/document/d/1-hxluneydqSUa9lB-V5twbN0YU1aiPPys484ID28Sx4/edit#heading=h.blal95as8bro

- Test DynamDB locally: https://www.bmc.com/blogs/dynamodb-queries/


# DynamoDB Documentation summary

## What Is Amazon DynamoDB?

### How it works

#### Core components: tables, items, and attributes, Primary Key, Secondary Indexes

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey

The primary key uniquely identifies each item in the table, so that no two items can have the same key.

DynamoDB supports two different kinds of primary keys:

- Partition key

A simple primary key, composed of one attribute known as the partition key. DynamoDB uses the partition key's value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored. In a table that has only a partition key, no two items can have the same partition key value.

The People table described in Tables, Items, and Attributes is an example of a table with a simple primary key (PersonID). You can access any item in the People table directly by providing the PersonId value for that item.

- Partition key and sort key

Referred to as a composite primary key, this type of key is composed of two attributes. The first attribute is the partition key, and the second attribute is the sort key.

DynamoDB uses the partition key value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored. All items with the same partition key value are stored together, in sorted order by sort key value.

In a table that has a partition key and a sort key, it's possible for two items to have the same partition key value. However, those two items must have different sort key values.

The Music table described in Tables, Items, and Attributes is an example of a table with a composite primary key (Artist and SongTitle). You can access any item in the Music table directly, if you provide the Artist and SongTitle values for that item.

A composite primary key gives you additional flexibility when querying data. For example, if you provide only the value for Artist, DynamoDB retrieves all of the songs by that artist. To retrieve only a subset of songs by a particular artist, you can provide a value for Artist along with a range of values for SongTitle.

NOTE:

- The partition key of an item is also known as its hash attribute. The term hash attribute derives from the use of an internal hash function in DynamoDB that evenly distributes data items across partitions, based on their partition key values.

- The sort key of an item is also known as its range attribute. The term range attribute derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

- Each primary key attribute must be a scalar (meaning that it can hold only a single value). The only data types allowed for primary key attributes are string, number, or binary. There are no such restrictions for other, non-key attributes.

## Working with DynamoDB

### Working with indexes

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html

# ORM

- TypeScript: https://www.npmjs.com/package/dyngoose (refactor of dynamoose)
- JS+TS: https://github.com/dynamoose/dynamoose
  Dynamoose TypeScript Support is in beta.
  Dynamoose is built entirely in TypeScript and ships with TypeScript Typings. This means that when using Dynamoose in TypeScript you will have access to all of the autocomplete and type safety features that TypeScript offers.

# Data Modeling

https://github.com/dynamoose/dynamoose/issues/1040

Single table:

- https://serverlessfirst.com/dynamodb-modelling-single-vs-multi-table/

Single Table:

- https://www.alexdebrie.com/posts/dynamodb-single-table/
- DynamoDB remove the ability to use joins at all.
- item collection in DynamoDB refers to all the items in a table or index that share a partition key.

Come fare Single Table modeling con dynamoose:
https://github.com/dynamoose/dynamoose/issues/768

## Dynamoose

Support both JS+TS:
https://github.com/dynamoose/dynamoose
Dynamoose TypeScript Support is in beta.
Dynamoose is built entirely in TypeScript and ships with TypeScript Typings. This means that when using Dynamoose in TypeScript you will have access to all of the autocomplete and type safety features that TypeScript offers.

### Schema

https://dynamoosejs.com/guide/Schema

- Support the creation of DynamoDB tables
- (do not support migration)

https://github.com/dynamoose/dynamoose/issues/467#issuecomment-466230963
