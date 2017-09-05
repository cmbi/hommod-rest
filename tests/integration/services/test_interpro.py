from hommod_rest.services.interpro import interpro


def test_interpro():

    interpro.storage_dir = '/tmp'

    interpro.get_domain_locations(
'MASLFHQLQILVWKNWLGVKRQPLWTLVLILWPVIIFIILAITRTKFPPTAKPTCYLA' +
'PRNLPSTGFFPFLQTLLCDTDSKCKDTPYGPQDLLRRKGIDDALFKDSEILRKSSNLD' +
'KDSSLSFQSTQVPERRHASLATVFPSPSSDLEIPGTYTFNGSQVLARILGLEKLLKQN' +
'STSEDIRRELCDSYSGYIVDDAFSWTFLGRNVFNKFCLSNMTLLESSLQELNKQFSQL' +
'SSDPNNQKIVFQEIVRMLSFFSQVQEQKAVWQLLSSFPNVFQNDTSLSNLFDVLRKAN' +
'SVLLVVQKVYPRFATNEGFRTLQKSVKHLLYTLDSPAQGDSDNITHVWNEDDGQTLSP' +
'SSLAAQLLILENFEDALLNISANSPYIPYLACVRNVTDSLARGSPENLRLLQSTIRFK' +
'KSFLRNGSYEDYFPPVPEVLKSKLSQLRNLTELLCESETFSLIEKSCQLSDMSFGSLC' +
'EESEFDLQLLEAAELGTEIAASLLYHDNVISKKVRDLLTGDPSKINLNMDQFLEQALQ' +
'MNYLENITQLIPIIEAMLHVNNSADASEKPGQLLEMFKNVEELKEDLRRTTGMSNRTI' +
'DKLLAIPIPDNRAEIISQVFWLHSCDTNITTPKLEDAMKEFCNLSLSERSRQSYLIGL' +
'TLLHYLNIYNFTYKVFFPRKDQKPVEKMMELFIRLKEILNQMASGTHPLLDKMRSLKQ' +
'MHLPRSVPLTQAMYRSNRMNTPQGSFSTISQALCSQGITTEYLTAMLPSSQRPKGNHT' +
'KDFLTYKLTKEQIASKYGIPINSTPFCFSLYKDIINMPAGPVIWAFLKPMLLGRILYA' +
'PYNPVTKAIMEKSNVTLRQLAELREKSQEWMDKSPLFMNSFHLLNQAIPMLQNTLRNP' +
'FVQVFVKFSVGLDAVELLKQIDELDILRLKLENNIDIIDQLNTLSSLTVNISSCVLYD' +
'RIQAAKTIDEMEREAKRLYKSNELFGSVIFKLPSNRSWHRGYDSGNVFLPPVIKYTIR' +
'MSLKTAQTTRSLRTKIWAPGPHNSPSHNQIYGRAFIYLQDSIERAIIELQTGRNSQEI' +
'AVQVQAIPYPCFMKDNFLTSVSYSLPIVLMVAWVVFIAAFVKKLVYEKDLRLHEYMKM' +
'MGVNSCSHFFAWLIESVGFLLVTIVILIIILKFGNILPKTNGFILFLYFSDYSFSVIA' +
'MSYLISVFFNNTNIAALIGSLIYIIAFFPFIVLVTVENELSYVLKVFMSLLSPTAFSY' +
'ASQYIARYEEQGIGLQWENMYTSPVQDDTTSFGWLCCLILADSFIYFLIAWYVRNVFP' +
'GTYGMAAPWYFPILPSYWKERFGCAEVKPEKSNGLMFTNIMMQNTNPSASPEYMFSSN' +
'IEPEPKDLTVGVALHGVTKIYGSKVAVDNLNLNFYEGHITSLLGPNGAGKTTTISMLT' +
'GLFGASAGTIFVYGKDIKTDLHTVRKNMGVCMQHDVLFSYLTTKEHLLLYGSIKVPHW' +
'TKKQLHEEVKRTLKDTGLYSHRHKRVGTLSGGMKRKLSISIALIGGSRVVILDEPSTG' +
'VDPCSRRSIWDVISKNKTARTIILSTHHLDEAEVLSDRIAFLEQGGLRCCGSPFYLKE' +
'AFGDGYHLTLTKKKSPNLNANAVCDTMAVTAMIQSHLPEAYLKEDIGGELVYVLPPFS' +
'TKVSGAYLSLLRALDNGMGDLNIGCYGISDTTVEEVFLNLTKESQKNSAMSLEHLTQK' +
'KIGNSNANGISTPDDLSVSSSNFTDRDDKILTRGERLDGFGLLLKKIMAILIKRFHHT' +
'RRNWKGLIAQVILPIVFVTTAMGLGTLRNSSNSYPEIQISPSLYGTSEQTAFYANYHP' +
'STEALVSAMWDFPGIDNMCLNTSDLQCLNKDSLEKWNTSGEPITNFGVCSCSENVQEC' +
'PKFNYSPPHRRTYSSQVIYNLTGQRVENYLISTANEFVQKRYGGWSFGLPLTKDLRFD' +
'ITGVPANRTLAKVWYDPEGYHSLPAYLNSLNNFLLRVNMSKYDAARHGIIMYSHPYPG' +
'VQDQEQATISSLIDILVALSILMGYSVTTASFVTYVVREHQTKAKQLQHISGIGVTCY' +
'WVTNFIYDMVFYLVPVAFSIGIIAIFKLPAFYSENNLGAVSLLLLLFGYATFSWMYLL' +
'AGLFHETGMAFITYVCVNLFFGINSIVSLSVVYFLSKEKPNDPTLELISETLKRIFLI' +
'FPQFCFGYGLIELSQQQSVLDFLKAYGVEYPNETFEMNKLGAMFVALVSQGTMFFSLR' +
'LLINESLIKKLRLFFRKFNSSHVRETIDEDEDVRAERLRVESGAAEFDLVQLYCLTKT' +
'YQLIHKKIIAVNNISIGIPAGECFGLLGVNGAGKTTIFKMLTGDIIPSSGNILIRNKT' +
'GSLGHVDSHSSLVGYCPQEDALDDLVTVEEHLYFYARVHGIPEKDIKETVHKLLRRLH' +
'LMPFKDRATSMCSYGTKRKLSTALALIGKPSILLLDEPSSGMDPKSKRHLWKIISEEV' +
'QNKCSVILTSHSMEECEALCTRLAIMVNGKFQCIGSLQHIKSRFGRGFTVKVHLKNNK' +
'VTMETLTKFMQLHFPKTYLKDQHLSMLEYHVPVTAGGVANIFDLLETNKTALNITNFL' +
'VSQTTLEEVFINFAKDQKSYETADTSSQGSTISVDSQDDQMES')

