# Add Field and Template IDs

This add-on for Anki 23.09+ lets you add IDs to notetype fields and templates.

**WARNING**: Only add IDs to notetypes you have authored yourself! (See below.)

## Motivation

Before Anki 23.09, if a deck author or consumer had changed the schema of a shared
notetype, it became impossible for the deck consumer to receive updates for notes with that
notetype.

> Example 1
>
> Alice exports a deck D, including note N with notetype NT. Bob imports D.
> Then Alice adds a new field to NT, and thus to N, and exports the deck again.
> Bob imports the updated version of D. However, because his version of NT is now
> conflicting with Alice's new version of NT, Anki cannot update his note N.

Anki 23.09 introduced the concept of merging notetypes. This allows the importing user
to receive schema updates for previously imported notetypes, and thus updates for notes
with these notetypes.

For this purpose, Anki now adds IDs to new fields and templates. It is also
possible to merge notetypes created with earlier releases, which do not have field and
template IDs. But then merging is name-based, and thus comes with a few limitations.

With this add-on, you can take advantage of ID-based merging for any notetype.

## How Merging Works

Merging one notetype into another means adding any missing fields or templates from the
former to the latter. To determine whether one is missing, Anki tries to find a matching
one in the second notetype. Two fields or templates match if

1. their IDs are identical, or
2. at least one of them does not have an ID, _and_ their names are identical.

> Example 2
>
> Alice shared her notetype NT with Bob. It has fields F1 and F2, and template T1.
> Now, Alice removes field F2 and adds another template, T2. Also, Bob adds the field F3
> to his local version. Then he imports Alice's updated version, enabling the `Merge notetypes`
> option. His notetype now has fields F1, F2 and F2, and templates T1 and T2.

Furthermore, when merging notetypes, Anki also merges any versions that have been created
during previous imports, because there was a conflict and the `Merge` option had not been enabled.

### Adding IDs to Imported Notetypes (_don't do it_)

If you import a notetype, where both you and the deck sharer used this add-on to add IDs
retroactively, no fields or notetype will match, and each one will be duplicated in your
local notetype.

To avoid this situation, only add IDs to notetypes you have created yourself, **do not
add IDs to notetypes you have imported** at some point.

## Limitations

You may be familiar with schema changes, which alter a notetype in such a way that a
one-way sync is required. Roughly, these are the same modifications that prevent
you from updating an existing notetype when importing. On the other hand, merging will
always be possible, but there are still a few caveats.

The following table provides an overview over what constitutes a schema change, and what
prevents you from updating.

| Operation                  | Preserve schema | Import without merge | Import with merge |
| -------------------------- | --------------- | -------------------- | ----------------- |
| Modify field / template    | ✅              | ✅                   | ✅                |
| Rename field / template    | ✅              | ❌ (1)               | ✅ (2)            |
| Add field / template       | ❌              | ❌                   | ✅                |
| Remove field / template    | ❌              | ❌                   | ✅ (3)            |
| Reorder fields / templates | ❌              | ❌                   | ✅                |
| Change sort field          | ❌              | ✅                   | ✅                |

**1:** Importing is still possible if matching is ID-based.  
**2:** If matching is name-based the renamed field will be added as a new one, duplicating
the field in the importer's collection.  
**3:** The removed field will not be deleted from the importer's collection.
