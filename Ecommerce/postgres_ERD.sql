CREATE SCHEMA "admins";

CREATE SCHEMA "orders";

CREATE SCHEMA "payemnt";

CREATE SCHEMA "shippings";

CREATE TYPE "admins"."roles" AS ENUM (
  'super_admin',
  'admin',
  'user'
);

CREATE TYPE "admins"."departments" AS ENUM (
  'sales',
  'accounts',
  'logistics'
);

CREATE TYPE "orders"."status" AS ENUM (
  'pending',
  'processing',
  'shipped',
  'delivered',
  'confirmed',
  'reviewed',
  'canceled'
);

CREATE TYPE "payemnt"."satus" AS ENUM (
  'pending',
  'completed',
  'failed'
);

CREATE TYPE "shippings"."shipping_status" AS ENUM (
  'pending',
  'out_for_delivery',
  'lost',
  'delivered'
);

CREATE TABLE "customers" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "first_name" varchar(30),
  "last_name" varchar(30),
  "username" varchar(30) UNIQUE NOT NULL,
  "email" varchar(60) UNIQUE NOT NULL,
  "phone_number" varchar(30) UNIQUE NOT NULL,
  "password_hash" varchar(40),
  "date_created" datetime DEFAULT (now())
);

CREATE TABLE "vendors" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "first_name" varchar(30),
  "last_name" varchar(30),
  "username" varchar(30) UNIQUE NOT NULL,
  "email" varchar(60) UNIQUE NOT NULL,
  "phone_number" varchar(30) UNIQUE NOT NULL,
  "address" varchar(60),
  "password_hash" varchar(40),
  "date_created" datetime DEFAULT (now())
);

CREATE TABLE "admins" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "first_name" varchar(30),
  "last_name" varchar(30),
  "username" varchar(30) UNIQUE NOT NULL,
  "email" varchar(60) UNIQUE NOT NULL,
  "phone_number" varchar(30) UNIQUE NOT NULL,
  "address" varchar(60),
  "department" varchar,
  "role" varchar,
  "password_hash" varchar(40),
  "date_created" varchar
);

CREATE TABLE "orders" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "status" varchar,
  "customer_id" int,
  "created_at" varchar,
  "updated_at" varchar,
  "price" numeric
);

CREATE TABLE "order_items" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "order_id" int,
  "product_id" int,
  "quantity" int,
  "unit_price" numeric,
  "total_amt" numeric
);

CREATE TABLE "payments" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "order_id" int,
  "amount" numeric,
  "status" varchar,
  "payment_method" varchar,
  "transaction_id" int UNIQUE NOT NULL DEFAULT (uuid),
  "created_at" var
);

CREATE TABLE "carts" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "customer_id" int
);

CREATE TABLE "cart_items" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "cart_id" int,
  "product_id" int,
  "quantity" int
);

CREATE TABLE "products" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar,
  "description" text,
  "price" numeric,
  "catogory_id" int,
  "vendor_id" int,
  "status" varchar,
  "created_at" datetime,
  "updated_at" datetime DEFAULT (now()),
  "image_url" varchar
);

CREATE TABLE "shippings" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "order_id" int,
  "customer_address_id" int,
  "shipment_status" varchar,
  "tracking_id" int UNIQUE NOT NULL,
  "estimated_delivery" datetime
);

CREATE TABLE "categories" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar,
  "parentcategory" varchar
);

CREATE TABLE "inventories" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "product_id" int,
  "quantity" int,
  "last_updated" varchar
);

CREATE TABLE "reviews" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "product_id" int,
  "customer_id" int,
  "comment" text,
  "rating" int,
  "created_at" datetime DEFAULT (now())
);

CREATE TABLE "promotions" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "code" varchar,
  "product_id" int,
  "discount_percentage" numeric,
  "description" text,
  "start_date" datetime,
  "end_date" datetime
);

CREATE TABLE "customer_addresses" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "residence_number" int,
  "customer_id" int,
  "street" varchar,
  "city" varchar,
  "postal_code" varchar,
  "country" vatchar,
  "description" text
);

ALTER TABLE "orders" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "order_items" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("id");

ALTER TABLE "order_items" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("id");

ALTER TABLE "payments" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("id");

ALTER TABLE "carts" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "cart_items" ADD FOREIGN KEY ("cart_id") REFERENCES "carts" ("id");

ALTER TABLE "cart_items" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("id");

ALTER TABLE "products" ADD FOREIGN KEY ("catogory_id") REFERENCES "categories" ("id");

ALTER TABLE "products" ADD FOREIGN KEY ("vendor_id") REFERENCES "vendors" ("id");

ALTER TABLE "shippings" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("id");

ALTER TABLE "customer_addresses" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

CREATE TABLE "shippings_customer_addresses" (
  "shippings_customer_address_id" int,
  "customer_addresses_id" int,
  PRIMARY KEY ("shippings_customer_address_id", "customer_addresses_id")
);

ALTER TABLE "shippings_customer_addresses" ADD FOREIGN KEY ("shippings_customer_address_id") REFERENCES "shippings" ("customer_address_id");

ALTER TABLE "shippings_customer_addresses" ADD FOREIGN KEY ("customer_addresses_id") REFERENCES "customer_addresses" ("id");


ALTER TABLE "inventories" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("id");

CREATE TABLE "products_promotions" (
  "products_id" int,
  "promotions_product_id" int,
  PRIMARY KEY ("products_id", "promotions_product_id")
);

ALTER TABLE "products_promotions" ADD FOREIGN KEY ("products_id") REFERENCES "products" ("id");

ALTER TABLE "products_promotions" ADD FOREIGN KEY ("promotions_product_id") REFERENCES "promotions" ("product_id");

