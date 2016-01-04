---
layout: post
title: "Postgres"
date: 2014-03-16 19:59:15 +0100
comments: true
categories:
---
# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Dump

This example will backup erp database that belongs to user geekstuff, to the file mydb.sql:
`pg_dump -U geekstuff erp -f mydb.sql`

## Restore

