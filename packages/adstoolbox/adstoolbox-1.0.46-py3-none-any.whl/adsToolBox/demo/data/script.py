import adsToolBox as ads
import fs

logger = ads.Logger(ads.Logger.INFO, "AdsLogger")

database = "Temp_DIVALTO"
schema = "dbo"
table = "REF_NOF"

db = ads.dbMssql({
    "host": "10.101.5.62",
    "port": "1433",
    "user": "sa",
    "password": "1PetitCafe",
    "database": database
}, logger)

def alim_NUMOF_X3():
    """Met à jour la table REF_NOF"""
    db.connect()
    logger.info(f"Suppression des anciennes données de {table}.")
    db.sqlExec(f"DELETE FROM {database}.{schema}.{table}")
    logger.info(f"Insertion des nouvelles données dans {table}.")
    db.sqlExec(f"""
    INSERT INTO {database}.{schema}.{table}
    SELECT 'SLVA', r2.REF, o.NUMEROOF, o.STATUS, o.DATEHEUREDEBUTPREVUE, o.DATEHEUREFINPREVUE,
           o.DATEHEUREDEBUTREELLE, o.DATEHEUREFINREELLE
    FROM SLVA.{schema}.OF_ENTETE_V o
    JOIN (
        SELECT MAX(b.BF_ID) AS ID, r1.REF, r1.dtdr
        FROM (
            SELECT RTRIM(REFERENCE) + RTRIM(SREFERENCE1) AS REF,
                   MIN(DATEHEUREFINPREVUE) AS dtdr
            FROM SLVA.{schema}.OF_ENTETE_V
            WHERE REFERENCE LIKE 'PF%' AND DATEHEUREFINPREVUE >= CURRENT_TIMESTAMP AND STATUS <> 5
            GROUP BY RTRIM(REFERENCE) + RTRIM(SREFERENCE1)
        ) r1
        JOIN SLVA.{schema}.OF_ENTETE_V b
        ON r1.REF = RTRIM(b.REFERENCE) + RTRIM(b.SREFERENCE1)
        AND r1.dtdr = b.DATEHEUREFINPREVUE
        GROUP BY r1.REF, r1.dtdr
    ) r2 ON o.BF_ID = r2.ID""")
    logger.info(f"Mise à jour de {table} terminée.")

def process_SSCC_Auzances_X():
    """Traite les fichiers SSCC pour Auzances"""
    logger.info("Démarrage du traitement SSCC Auzances.")
    try:
        wrk_root_fs = fs.smbfs.SMBFS(host="10.101.5.72", username="admintaskads", passwd="b3xSNzB7YLDFXq56wa2l")
        wrk_fs = fs.subfs.SubFS(wrk_root_fs, "/ECHANGE/ETIQ/AUZANCES/ENVOI")
        dist_root_fs = fs.ftpfs.FTPFS("175.123.5.220", user="admintaskads", passwd="tartine@22!")
        dist_fs = fs.subfs.SubFS(dist_root_fs, "/SSCCETIQ/EMISSION")
        com_fs = fs.mountfs.MountFS()
        com_fs.mount('wrk', wrk_fs)
        com_fs.moun('dist', dist_fs)
        flagtl_filename = "FlagTL.txt"
        com_fs.open("/wrk/" + flagtl_filename, "a").close()
        sscc_src_filename = "SSCC"
        sscc_exists = any(f == sscc_src_filename for f in com_fs.listdir("/dist"))
        if not sscc_exists:
            logger.warning("Fichier SSCC non trouvé. Fin du traitement.")
            return
        logger.info("Fichier SSCC trouvé, début du traitement.")
        trg_lines = ["Ligne transformée\n"]
        with com_fs.open("/wrk/SSCC.txt", "w") as trg:
            trg.writelines(trg_lines)
        logger.info("Traitement terminé avec succès.")
    except Exception as e:
        logger.error(f"Erreur lors du traitement SSCC Auzances: {str(e)}.")
    finally:
        com_fs.remove("/wrk/" + flagtl_filename)
        com_fs.close()

alim_NUMOF_X3()
process_SSCC_Auzances_X()
logger.info("Script terminé avec succès")

