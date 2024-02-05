# Resolutions are not fully standardised 
# I. e. one beneficiary can be mentioned by using different names. 

# I would like to apologise for what you are about to see in this file.

standardisation_dict = {}

akt_rozdroze = "AKT Rozdroże"
rozdroze_dict = {
"Akademickiemu Klubowi Turystycznemu Rozdroże przy Uniwersytecie Jagiellońskim":
    akt_rozdroze,
    "Stowarzyszeniu AKT \"Rozdroże\"": akt_rozdroze,
    "Stowarzyszeniu AKT Rozdroże": akt_rozdroze,
    "Akademickiemu Klubowi Turystycznemu ROZDROŻE przy Uniwersytecie Jagiellońskim": akt_rozdroze,
}

standardisation_dict.update(rozdroze_dict)

czapka = "Bractwu Czapki Studenckiej UJ"
czapka_dict = {
    "Bractwu Czapki Studenckiej": czapka,
    "Bractwu Czapki Studenckiej Uniwersytetu": czapka,
    "Bractwu Czapki Studenckiej Uniwersytetu Jagiellońskiego": czapka,
    "Bractwu Czapki Studenckiej Uniwersytetu Jagiellońskiego w Krakowie": czapka,
    "Stowarzyszeniu Bractwo Czapki Studenckiej Uniwersytetu Jagiellońskiego": czapka,
}

standardisation_dict.update(czapka_dict)

wrss_wgig = "WRSS WGiG"

wrss_wgig_dict = {
    "WRSS WGIG": wrss_wgig,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Geografii i Geologii"
    "Wydziałowej Radzie Samorządu Studentów Wydziału Geografii i Geologii Uni wersytetu Jagiellońskiego": wrss_wgig,
    "Wydziałowej Radzie Samorządu Studentów Wydzialu Geografii i Geologii Uniwersytetu Jagiellońskiego": wrss_wgig,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Geografii i Geologii Uniwersytetu Jagiellońskiego": wrss_wgig,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Geografii i Geologii": wrss_wgig,
}

standardisation_dict.update(wrss_wgig_dict)

wrss_wp = "WRSS WP"

wrss_wp_dict = {
    "Wydziałowej Rady Samorządu Studentów Wydziału Polonistyki Uniwersytetu Jagiellońskiego" : wrss_wp,
    "Wydziałowej Radzie Samorządu Studentów Polonistyki Uniwersytetu Jagiellońskiego" : wrss_wp,
    "Wydziałowej Radzie Samorządu Studentów Wydzialu Polonistyki Uniwersytetu Jagiellońskiego": wrss_wp,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Polonistyki Uniwersytetu Jagiellońskiego": wrss_wp,
}

standardisation_dict.update(wrss_wp_dict)

wrss_wziks = "WRSS WZiKS"

wrss_wziks_dict = {
    "Wydziałowej Rady Samorządu Studentów Wydziału Zarządzania i Komunikacji Społecznej Uniwersytetu Jagiellońskiego": wrss_wziks,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Zarządzania i Komuni kacji Społecznej Uniwersytetu Jagiellońskiego": wrss_wziks,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Zarządzania i Komunika cji Społecznej Uniwersytetu Jagiellońskiego": wrss_wziks,
    "Wydziałowej Radzie Samorządu Studentów Wydzialu Zarządzania i Komunikacji Społecz nej Uniwersytetu Jagiellońskiego": wrss_wziks,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Zarządzania i Komunikacji Społecznej Uniwersytetu Jagiellońskiego": wrss_wziks,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Zarządzania i Komunikacji Uniwersytetu Jagiellońskiego": wrss_wziks,
}

standardisation_dict.update(wrss_wziks_dict)

wbbib = "WRSS WBBiB"

wbbib_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Biochemii, Biofizyki i Biotechnologii Uniwersytetu Jagiellońskiego": wbbib
}

standardisation_dict.update(wbbib_dict)

wb = "WRSS WB"

wb_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Biologii Uniwersytetu Jagiellońskiego": wb,
}

standardisation_dict.update(wb_dict)

wch = "WRSS WCh"

wch_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Chemii UJ": wch,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Chemii Uniwersytetu Jagiellońskiego": wch,
}

standardisation_dict.update(wch_dict)

filology = "WRSS Filologia"

filology_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Filologicznego Uniwersytetu Jagiellońskiego": filology,
    "Zarządowi Komisarycznemu Wydziałowej Rady Samorządu Studentów Wydziału Filologicznego Uniwersytetu Jagiellońskiego": filology,
    "Zarządowi Komisarycznemu Wydziału Filologicznego Uniwersytetu Jagiellońskiego": filology,
}

standardisation_dict.update(filology_dict)

philosophy = "WRSS Filozofia"

philosophy_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Filozoficznego Uniwersytetu Jagiellońskiego": philosophy,
}

standardisation_dict.update(philosophy_dict)

wrss_fais = "WRSS FAIS"

wrss_fais_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Fizyki, Astronomii i Informatyki Stosowanej Uniwersytetu Jagiellońskiego": wrss_fais,
}

standardisation_dict.update(wrss_fais_dict)

wrss_wh = "WRSS WH"

wrss_wh_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Historii Uniwersytetu Jagiellońskiego": wrss_wh,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Historycznego": wrss_wh,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Historycznego Uniwersytetu Jagiellońskiego": wrss_wh,
}

standardisation_dict.update(wrss_wh_dict)

wrss_wmii = "WRSS WMiI"

wrss_wmii_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Matematyki i Informatyki UJ": wrss_wmii,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Matematyki i Informatyki Uniwersytetu Jagiellońskiego": wrss_wmii,
}

standardisation_dict.update(wrss_wmii_dict)

wrss_wpia = "WRSS WPiA"

wrss_wpia_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Prawa i Administracji UJ": wrss_wpia,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Prawa i Administracji": wrss_wpia,
    "Wydziałowej Radzie Samorządu Studentów Wydziału Prawa i Administracji Uniwersytetu Jagiellońskiego": wrss_wpia,

}

standardisation_dict.update(wrss_wpia_dict)

wrss_wsmip = "WRSS WSMiP"

wrss_wsmip_dict = {
    "Wydziałowej Radzie Samorządu Studentów Wydziału Studiów Międzynarodowych i Politycznych Uniwersytetu Jagiellońskiego": wrss_wsmip,
}

standardisation_dict.update(wrss_wsmip_dict)

rss_mish = "Radzie Samorządu Studentów Międzywydziałowych Indywidualnych Studiów Humanistycznych Uniwersytetu Jagiellońskiego"

rss_mish_dict = {
    "Radzie Samorządu Studentów Międzywydziałowych Indywidualnych Studiów Humanistycznych Uniwersytetu Jagiellońskiego": rss_mish,
    "Radzie Samorządu Studentów Międzywydziałowych Indywidualnych Studiów Humanistycznych UJ": rss_mish,
}

standardisation_dict.update(rss_mish_dict)

management = "Zarządowi SSUJ"

management_dict = {
    "Zarządowi Samorządu Studentów Uniwersytetu Jagiellońskiego": management,
}

vicepresident = "Wiceprzewodniczący(a) SSUJ"

vicepresident_dict = {
    "Wiceprzewodniczącego Samorządu Studentów Uniwersytetu Jagiellońskiego": vicepresident,
    "Wiceprzewodniczącej Samorządu Studentów": vicepresident,
    "Wiceprzewodniczącej Samorządu Studentów Uniwersytetu Jagiellońskiego": vicepresident,
    "Wiceprzewodniczącemu Samorządu Studentów Uniwersytetu Jagiellońskiego": vicepresident,
}

standardisation_dict.update(vicepresident_dict)

all_in_uj = "Stowarzyszeniu All in UJ"

all_in_uj_dict = {
    "Stowarzyszenie All in UJ": all_in_uj,
    "Stowarzyszeniu All In UJ Kraków": all_in_uj,
}

standardisation_dict.update(all_in_uj_dict)

esn_uj = "Stowarzyszeniu Erasmus Student Network UJ Kraków"

esn_uj_dict = {
    "Stowarzyszeniu ESN UJ": esn_uj,
    "Stowarzyszeniu ESN UJ Kraków": esn_uj,
    "Stowarzyszeniu ESN Kraków": esn_uj,
}

standardisation_dict.update(esn_uj_dict)

teczuj = "Stowarzyszeniu TęczUJ"

teczuj_dict = {
    "Organizacja Studentów LGBT i Sojuszników TęczUJ": teczuj,
    "Organizacji Studentów LGBT i Sojuszników TęczUJ": teczuj,

}

standardisation_dict.update(teczuj_dict)

dkms = "Stowarzyszeniu DKMS Polska"

dkms_dict = {
    "DKMS Polska": dkms,
}

standardisation_dict.update(dkms_dict)


aegee = "Stowarzyszeniu Europejskie Forum Studentów AEGEE"

aegee_dict = {
    "Stowarzyszeniu AEGEE Kraków": aegee,
    "Stowarzyszeniu Europejskie Forum Studentów AEGEE": aegee,
    "Stowarzyszeniu Europejskie Forum Studentów AEGEE Kraków": aegee,
    "Stowarzyszeniu Europejskiemu Forum Studentów AEGEE Kraków": aegee,
    "Stowarzyszeniu Europejskie Forum Studentów AEGEE KRAKÓW": aegee,
}

standardisation_dict.update(aegee_dict)

culture = "Uczelnianej Komisji Kultury Samorządu Studentów Uniwersytetu Jagiellońskiego"

culture_dict = {
    "Uczelnianej Komisji Kultury": culture,
    "Przewodniczącej Uczelnianej Komisji Kultury Samorządu Studentów Uniwersytetu Jagiellońskiego": culture,
    "Przewodniczącej Uczelnianej Komisji Kultury Uniwersytetu Jagiellońskiego": culture,
    "Przewodniczącej Uczelnianej Komisji Kultury": culture,
    "Przewodniczącej Komisji Kultury Samorządu Studentów Uniwersytetu Jagiellońskiego": culture,
    "Pełnomocnikowi ds. kultury Samorządu Studentów Uniwersytetu Jagiellońskiego": culture,
}

standardisation_dict.update(culture_dict)

didactics = "Uczelnianej Komisji Dydaktycznej Samorządu Studentów Uniwersytetu Jagiellońskiego"

didactics_dict = {
    "Przewodniczącej Uczelianej Komisji Dydaktycznej Samorządu Studentów Uniwersytetu Jagiellońskiego": didactics,
    "Przewodniczącej Uczelnianej Komisji Dydaktycznej Samorządu Studentów Uniwersytetu Jagiellońskiego": didactics,
    "Przewodniczącemu Uczelnianej Komisji Dydaktycznej Samorządu Studentów Uniwersytetu Jagiellońskiego": didactics,
}

standardisation_dict.update(didactics_dict)

promotion = "Zespołowi Informacji i Promocji Samorządu Studentów UJ"

promotion_dict = {
    "Przewodniczącej Zespołu Informacji i Promocji": promotion,
    "Przewodniczącej Zespołu Informacji i Promocji Samorządu Studentów UJ": promotion,
    "Przewodniczącej Zespołu Informacji i Promocji Samorządu Studentów Uniwersytetu Jagiellońskiego": promotion,
    "Przewodniczącej Zespółu Informacji i Promocji Samorządu Studentów Uniwersytetu Jagiellońskiego": promotion,
    "Przewodniczącej Zespołu Promocji i Informacji Samorządu Studentów Uniwersytetu Jagiellońskiego": promotion,
    "Przewodniczącemu Zespołu ds. Informacji i Promocji Samorządu Studentów Uniwersytetu Jagiellońskiego": promotion,
}

standardisation_dict.update(promotion_dict)

nawojka = "Radzie Mieszkańców DS \"Nawojka\""

nawojka_dict = {
    "Przewodniczącej Radzie Mieszkańców DS. Nawojka": nawojka,
    "Radzie Domu Studenckiego Nawojka": nawojka,
    "Radzie Mieszkańców Domu Studenckiego Nawojka": nawojka,
    "Radzie Mieszkańców DS \"Nawojka\"": nawojka,
    "Radzie Mieszkańców DS Nawojka": nawojka,
}

standardisation_dict.update(nawojka_dict)

bursa = "Radzie Mieszkańców DS Bursa Jagiellońska"

bursa_dict = {
    "Przewodniczącemu Rady Mieszkańców Domu Studenckiego Bursa Jagiellońska": bursa,
    "Radzie Mieszkańców Domu Studenckiego Bursa": bursa,
    "Radzie Mieszkańców DS Bursa Jagiellońska": bursa,
    "Radzie Mieszkańców Domu Studenckiego Bursa Jagiellońska": bursa 
}

standardisation_dict.update(bursa_dict)

mobility = "Uczelnianemu Zespołowi Mobilności Samorządu Studentów Uniwersytetu Jagiellońskiego"

mobility_dict = {
    "Przewodniczącej Uczelnianego Zespołu Mobilności Samorządu Studentów Uniwersytetu Jagiellońskiego": mobility,
    "Przewodniczącej Zespołu Mobilności Samorządu Studentów Uniwersytetu Jagiellońskiego": mobility,
    "Przewodniczącemu Zespołowi Mobilności Samorządu Studentów Uniwersytetu Jagiellońskiego": mobility,
    "Przewodniczącemu Zespołu Mobilności Samorządu Studentów Uniwersytetu Jagiellońskiego": mobility,
    "Zespołowi Mobilności Samorządu Studentów Uniwersytetu Jagiellońskiego": mobility,
}

standardisation_dict.update(mobility_dict)

secretary = "Sekretarzowi Zarządu Samorządu Studentów UJ"

secretary_dict = {
    "Sekretarz Zarządu Samorządu Studentów Uniwersytetu Jagiellońskiego": secretary,
    "Sekretarzowi Zarządu Samorządu Studentów Uniwersytetu Jagiellońskiego": secretary,
}

standardisation_dict.update(secretary_dict)

bydgoska = "Radzie Mieszkańców DS Bydgoska"

bydgoska_dict = {
    "Radzie Mieszkańców Dom Studencki Bydgoska": bydgoska,
    "Radzie Mieszkańców Domu Studenckiego \"Bydgoska\"": bydgoska,
    "Radzie Mieszkańców DS Bydgoska": bydgoska,
    "Przewodniczącej Rady Mieszkańców Domu Studenckiego Bydgoska": bydgoska,
}

standardisation_dict.update(bydgoska_dict)

president = "Przewodniczącej Zarządu Samorządu Studentów UJ"

president_dict = {
    "Przewodniczącej Samorządu Studentów": president,
    "Przewodniczącej Samorządu Studentów Uniwersytetu Jagiellońskiego": president,
}

standardisation_dict.update(president_dict)



def standardize_beneficiary_record(record):
    benef = record["beneficiary"]

    if benef in standardisation_dict:
        record["beneficiary"] = standardisation_dict[benef]
    
    return record

def standardize_beneficiaries(records):
    return list(map(standardize_beneficiary_record, records))