from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gnujdb", "0003_gnuj_miejsce"),
    ]

    operations = [
        migrations.RunSQL(
            # https://sqlite.org/fts5.html
            sql="""
CREATE VIRTUAL TABLE gnujdb_gnuj_fts_idx USING fts5(tytul, dodatkowe_info, content='gnujdb_gnuj');
INSERT INTO gnujdb_gnuj_fts_idx(gnujdb_gnuj_fts_idx) VALUES('rebuild');

CREATE TRIGGER tbl_ai AFTER INSERT ON gnujdb_gnuj BEGIN
  INSERT INTO gnujdb_gnuj_fts_idx(rowid, tytul, dodatkowe_info) VALUES (new.rowid, new.tytul, new.dodatkowe_info);
END;
CREATE TRIGGER tbl_ad AFTER DELETE ON gnujdb_gnuj BEGIN
  INSERT INTO gnujdb_gnuj_fts_idx(gnujdb_gnuj_fts_idx, rowid, tytul, dodatkowe_info) VALUES('delete', old.rowid, old.tytul, old.dodatkowe_info);
END;
CREATE TRIGGER tbl_au AFTER UPDATE ON gnujdb_gnuj BEGIN
  INSERT INTO gnujdb_gnuj_fts_idx(gnujdb_gnuj_fts_idx, rowid, tytul, dodatkowe_info) VALUES('delete', old.rowid, old.tytul, old.dodatkowe_info);
  INSERT INTO gnujdb_gnuj_fts_idx(rowid, tytul, dodatkowe_info) VALUES (new.rowid, new.tytul, new.dodatkowe_info);
END;
                """,
            reverse_sql=migrations.RunSQL.noop,
        )
    ]
