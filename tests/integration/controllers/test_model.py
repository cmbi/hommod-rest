import logging

from nose.tools import with_setup, eq_, ok_

from hommod.controllers.blast import blaster
from hommod.services.dssp import dssp
from hommod.controllers.blacklist import blacklister
from hommod.services.interpro import interpro
from hommod.controllers.domain import domain_aligner
from hommod.controllers.model import modeler
from hommod.models.template import TemplateID
from hommod.models.range import SequenceRange
from hommod.models.align import DomainAlignment
from hommod.controllers.clustal import clustal_aligner
from hommod.controllers.kmad import kmad_aligner
from hommod.controllers.method import select_best_domain_alignment
from hommod.services.helpers.cache import cache_manager as cm
import hommod.default_settings as settings


_log = logging.getLogger(__name__)


def setup():
    blaster.blastp_exe = settings.BLASTP_EXE
    dssp.dssp_dir = settings.DSSP_DIR
    blacklister.file_path = settings.BLACKLIST_FILE_PATH
    interpro.url = settings.INTERPRO_URL
    modeler.yasara_dir = settings.YASARA_DIR
    modeler.uniprot_databank = settings.UNIPROT_BLAST_DATABANK
    domain_aligner.forbidden_interpro_domains = settings.FORBIDDEN_INTERPRO_DOMAINS
    domain_aligner.similar_ranges_min_overlap_percentage = settings.SIMILAR_RANGES_MIN_OVERLAP_PERCENTAGE
    domain_aligner.similar_ranges_max_length_difference_percentage = settings.SIMILAR_RANGES_MAX_LENGTH_DIFFERENCE_PERCENTAGE
    domain_aligner.min_percentage_coverage = settings.DOMAIN_MIN_PERCENTAGE_COVERAGE
    domain_aligner.template_blast_databank = settings.TEMPLATE_BLAST_DATABANK
    domain_aligner.max_merge_distance = settings.DOMAIN_MAX_MERGE_DISTANCE
    domain_aligner.highly_homologous_percentage_identity = settings.HIGHLY_HOMOLOGOUS_PERCENTAGE_IDENTITY
    clustal_aligner.clustalw_exe = settings.CLUSTALW_EXE
    kmad_aligner.kmad_exe = settings.KMAD_EXE
    cm.redis_hostname = settings.CACHE_REDIS_HOST
    cm.redis_port = settings.CACHE_REDIS_PORT
    cm.redis_db = settings.CACHE_REDIS_DB
    cm.expiration_time = settings.CACHE_EXPIRATION_TIME
    cm.lock_timeout = settings.CACHE_LOCK_TIMEOUT

def end():
    pass


@with_setup(setup, end)
def test_no_alignment_flip():
    seq = ( 
"MGKLVALVLLGVGLSLVGEMFLAFRERVNASREVEPVEPENCHLIEELESGSEDIDILPSGLAFISSGLKYP" +
"GMPNFAPDEPGKIFLMDLNEQNPRAQALEISGGFDKELFNPHGISIFIDKDNTVYLYVVNHPHMKSTVEIFK" +
"FEEQQRSLVYLKTIKHELLKSVNDIVVLGPEQFYATRDHYFTNSLLSFFEMILDLRWTYVLFYSPREVKVVA" +
"KGFCSANGITVSADQKYVYVADVAAKNIHIMEKHDNWDLTQLKVIQLGTLVDNLTVDPATGDILAGCHPNPM" +
"KLLNYNPEDPPGSEVLRIQNVLSEKPRVSTVYANNGSVLQGTSVASVYHGKILIGTVFHKTLYCEL")

    species_id = 'human'

    range_ = SequenceRange(183, 265, seq)
    template_id = TemplateID('4zrn', 'A')
    alignment = DomainAlignment(
"YFTNSLLSFFEMILDLRWT---YVLFYSPRE-----VKVVA---KGFCSANGITVSAD-Q--K-YVYVADVAAKNIHIMEKHDNWDLTQLKVIQLGT",
"YSTEMYLEFFAREYGLKYTVLRYANVYGPRQDPYGEAGVVAIFTERMLRGEEVHIFGDGEYVRDYVYVDDVVRANLLAMEKGDN------EVFNIGT",
                        range_, template_id)

    context = modeler._prepare_context(alignment.template_id.pdbid)
    context.set_main_target(seq, species_id, alignment.template_id.chain_id)

    chain_alignments = modeler._make_alignments(seq, species_id, alignment, context)
    for chain_id in chain_alignments:

        _log.debug("got alignment {}: {}".format(chain_id, chain_alignments[chain_id]))
        ok_(chain_alignments[chain_id].target_alignment.replace('-','') in seq)


@with_setup(setup, end)
def test_init_template_5GOX():
    context = modeler._prepare_context('5GOX')

    eq_(len(context.get_chain_ids()), 2)


@with_setup(setup, end)
def test_init_template_5MHF():
    context = modeler._prepare_context('5MHF')

    eq_(len(context.get_chain_ids()), 4)


@with_setup(setup, end)
def test_align_with_repeats():
    sequence = """MRRGRLLEIALGFTVLLASYTSHGADANLEAGNVKETRASRAKRRGGGGHD
ALKGPNVCGSRYNAYCCPGWKTLPGGNQCIVPICRHSCGDGFCSRPNMCTCPSGQIAPSCGSRSIQHCN
IRCMNGGSCSDDHCLCQKGYIGTHCGQPVCESGCLNGGRCVAPNRCACTYGFTGPQCERDYRTGPCFTV
ISNQMCQGQLSGIVCTKTLCCATVGRAWGHPCEMCPAQPHPCRRGFIPNIRTGACQDVDECQAIPGLCQ
GGNCINTVGSFECKCPAGHKLNEVSQKCEDIDECSTIPGICEGGECTNTVSSYFCKCPPGFYTSPDGTR
CIDVRPGYCYTALTNGRCSNQLPQSITKMQCCCDAGRCWSPGVTVAPEMCPIRATEDFNKLCSVPMVIP
GRPEYPPPPLGPIPPVLPVPPGFPPGPQIPVPRPPVEYLYPSREPPRVLPVNVTDYCQLVRYLCQNGRC
IPTPGSYRCECNKGFQLDLRGECIDVDECEKNPCAGGECINNQGSYTCQCRAGYQSTLTRTECRDIDEC
LQNGRICNNGRCINTDGSFHCVCNAGFHVTRDGKNCEDMDECSIRNMCLNGMCINEDGSFKCICKPGFQ
LASDGRYCKDINECETPGICMNGRCVNTDGSYRCECFPGLAVGLDGRVCVDTHMRSTCYGGYKRGQCIK
PLFGAVTKSECCCASTEYAFGEPCQPCPAQNSAEYQALCSSGPGMTSAGSDINECALDPDICPNGICEN
LRGTYKCICNSGYEVDSTGKNCVDINECVLNSLLCDNGQCRNTPGSFVCTCPKGFIYKPDLKTCEDIDE
CESSPCINGVCKNSPGSFICECSSESTLDPTKTICIETIKGTCWQTVIDGRCEININGATLKSQCCSSL
GAAWGSPCTLCQVDPICGKGYSRIKGTQCEDIDECEVFPGVCKNGLCVNTRGSFKCQCPSGMTLDATGR
ICLDIRLETCFLRYEDEECTLPIAGRHRMDACCCSVGAAWGTEECEECPMRNTPEYEELCPRGPGFATK
EITNGKPFFKDINECKMIPSLCTHGKCRNTIGSFKCRCDSGFALDSEERNCTDIDECRISPDLCGRGQC
VNTPGDFECKCDEGYESGFMMMKNCMDIDECQRDPLLCRGGVCHNTEGSYRCECPPGHQLSPNISACID
INECELSAHLCPNGRCVNLIGKYQCACNPGYHSTPDRLFCVDIDECSIMNGGCETFCTNSEGSYECSCQ
PGFALMPDQRSCTDIDECEDNPNICDGGQCTNIPGEYRCLCYDGFMASEDMKTCVDVNECDLNPNICLS
GTCENTKGSFICHCDMGYSGKKGKTGCTDINECEIGAHNCGKHAVCTNTAGSFKCSCSPGWIGDGIKCT
DLDECSNGTHMCSQHADCKNTMGSYRCLCKEGYTGDGFTCTDLDECSENLNLCGNGQCLNAPGGYRCEC
DMGFVPSADGKACEDIDECSLPNICVFGTCHNLPGLFRCECEIGYELDRSGGNCTDVNECLDPTTCISG
NCVNTPGSYICDCPPDFELNPTRVGCVDTRSGNCYLDIRPRGDNGDTACSNEIGVGVSKASCCCSLGKA
WGTPCEMCPAVNTSEYKILCPGGEGFRPNPITVILEDIDECQELPGLCQGGKCINTFGSFQCRCPTGYY
LNEDTRVCDDVNECETPGICGPGTCYNTVGNYTCICPPDYMQVNGGNNCMDMRRSLCYRNYYADNQTCD
GELLFNMTKKMCCCSYNIGRAWNKPCEQCPIPSTDEFATLCGSQRPGFVIDIYTGLPVDIDECREIPGV
CENGVCINMVGSFRCECPVGFFYNDKLLVCEDIDECQNGPVCQRNAECINTAGSYRCDCKPGYRFTSTG
QCNDRNECQEIPNICSHGQCIDTVGSFYCLCHTGFKTNDDQTMCLDINECERDACGNGTCRNTIGSFNC
RCNHGFILSHNNDCIDVDECASGNGNLCRNGQCINTVGSFQCQCNEGYEVAPDGRTCVDINECLLEPRK
CAPGTCQNLDGSYRCICPPGYSLQNEKCEDIDECVEEPEICALGTCSNTEGSFKCLCPEGFSLSSSGRR
CQDLRMSYCYAKFEGGKCSSPKSRNHSKQECCCALKGEGWGDPCELCPTEPDEAFRQICPYGSGIIVGP
DDSAVDMDECKEPDVCKHGQCINTDGSYRCECPFGYILAGNECVDTDECSVGNPCGNGTCKNVIGGFEC
TCEEGFEPGPMMTCEDINECAQNPLLCAFRCVNTYGSYECKCPVGYVLREDRRMCKDEDECEEGKHDCT
EKQMECKNLIGTYMCICGPGYQRRPDGEGCVDENECQTKPGICENGRCLNTRGSYTCECNDGFTASPNQ
DECLDNREGYCFTEVLQNMCQIGSSNRNPVTKSECCCDGGRGWGPHCEICPFQGTVAFKKLCPHGRGFM
TNGADIDECKVIHDVCRNGECVNDRGSYHCICKTGYTPDITGTSCVDLNECNQAPKPCNFICKNTEGSY
QCSCPKGYILQEDGRSCKDLDECATKQHNCQFLCVNTIGGFTCKCPPGFTQHHTSCIDNNECTSDINLC
GSKGICQNTPGSFTCECQRGFSLDQTGSSCEDVDECEGNHRCQHGCQNIIGGYRCSCPQGYLQHYQWNQ
CVDENECLSAHICGGASCHNTLGSYKCMCPAGFQYEQFSGGCQDINECGSAQAPCSYGCSNTEGGYLCG
CPPGYFRIGQGHCVSGMGMGRGNPEPPVSGEMDDNSLSPEACYECKINGYPKRGRKRRSTNETDASNIE
DQSETEANVSLASWDVEKTAIFAFNISHVSNKVRILELLPALTTLTNHNRYLIESGNEDGFFKINQKEG
ISYLHFTKKKPVAGTYSLQISSTPLYKKKELNQLEDKYDKDYLSGELGDNLKMKIQVLLH
""".replace('\n','')

    template_id = TemplateID('2w86', 'A')

    residue_number = 545

    domain_alignments = domain_aligner.get_domain_alignments(sequence, residue_number, template_id)
    domain_alignment = select_best_domain_alignment(domain_alignments)

    context = modeler._prepare_context(template_id.pdbid)
    context.set_main_target(sequence, 'HUMAN', template_id.chain_id)

    alignments = modeler._make_alignments(sequence, 'HUMAN', domain_alignment, context)
    alignment = alignments[template_id.chain_id]

    ok_(alignment.get_target_sequence() in sequence)
    offset = sequence.find(alignment.get_target_sequence())

    ok_(alignment.is_target_residue_covered(residue_number - offset))


@with_setup(setup, end)
def test_align_rab3d():
    sequence = "MDEDVLTTLKILIIGESGVGKSSLLLRFTDDTFDPELAATIGVDFKVKTISVDGN" + \
"KAKLAIWVTLHQQTANFFLKSQIGNSPILKWAMWQYDTAGQERFRTLTPSYYRGAQGVILVYDVTRRDTF" + \
"VKLDNWLNELETYCTRNDIVNMLVGNKIDKENREVDRNEGLKFARKHSMLFIEASAKTCDGVQCAFEELV" + \
"EKIIQTPGLWESENQNKGVKLSHREEGQGGGACGGYCSVL"

    template_id = TemplateID('2GF9', 'A')

    residue_number = 70

    domain_alignments = domain_aligner.get_domain_alignments(sequence, residue_number, template_id)
    if len(domain_alignments) > 0:
        domain_alignment = select_best_domain_alignment(domain_alignments)

        context = modeler._prepare_context(template_id.pdbid)
        context.set_main_target(sequence, 'HUMAN', template_id.chain_id)

        alignments = modeler._make_alignments(sequence, 'HUMAN', domain_alignment, context)
        alignment = alignments[template_id.chain_id]

        ok_(alignment.get_target_sequence() in sequence)
        offset = sequence.find(alignment.get_target_sequence())

        ok_(alignment.is_target_residue_covered(residue_number - offset))