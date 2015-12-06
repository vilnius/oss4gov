Ubuntu konfigūravimo priemonės Vilniaus savivaldybės IT infrastruktūroje.

Šioje repozitorijoje rasite priemones skirtas Vilniaus savivaldybės darbuotojo
kompiuterio, kuriame idegta Ubuntu, konfigūravimui.

Motyvacija
==========

- Perėjimas prie atviro kodo programinės įrangos padės Vilniaus savivaldybei
  sumažinti išlaidas nuosavybinės programinės įrangos licencijoms.

- Atvirojo kodo programinės įrangos naudojimas padeda išvengti verslo subjektų
  kuriamo `„užrakinimo“ efekto`_.


.. _„užrakinimo“ efekto: https://en.wikipedia.org/wiki/Vendor_lock-in


Reikalavimai
============

- Kompiuteris į kurį bus diegiama *Ubuntu*, turi būti `suderinamas su Ubuntu`_.
  Ne visa kompiuterio aparatinė įranga yra suderinama su *Ubuntu*.

- Vilniaus savivaldybėje būtina visus raštinės dokumentus saugoti `ODF (Open
  Document Format)`_ formatu. *ODF* formatą puikiai palaiko tiek `Libre
  Office`_ raštinės paketas, tiek `Microsoft Office`_ (nuo 2007 SP 2).

  *DOC*, *XSL* ir *PPT* yra seni, uždari formatai, kuriuos nuo 2007 metų
  pakeitė *OOXML* formatų grupė (*.docx*, *.xlsx*, *.pptx*).

  *OOXML* formatas yra sudėtingas ir turintis daug funkcijų ir daug palikimo iš
  šio formato pirmtakų. *OOXML* formato pilnai nepalaiko joks biuro programų
  paketas, `įskaitant ir Microsoft Office`_.

  Kadangi *ODT* yra geriausiai palaikomas formatas tarp populiariausių biuro
  programų paketų, būtina dokumentus saugoti *ODT* formatu, kad išvengti
  nesuderinamumo tarp formatų problemų.

  Taip pat žiūrėti:

  - `U.K. Government Adopts ODF, but Not Microsoft's OOXML
    <https://redmondmag.com/articles/2014/07/23/uk-adopts-odf.aspx>`_

- Kompiuteris, kuris bus konfigūruojamas turi turėti Ubuntu 14.04 LTS, kadangi
  su šia versija buvo testuojama konfigūravimo priemonė.

.. _suderinamas su Ubuntu: http://www.ubuntu.com/certification/desktop/
.. _ODF (Open Document Format): https://en.wikipedia.org/wiki/OpenDocument
.. _Libre Office : https://www.libreoffice.org/
.. _Microsoft Office: https://products.office.com/
.. _įskaitant ir Microsoft Office : https://en.wikipedia.org/wiki/Office_Open_XML#Application_support


Naudojimas
==========

Pirmiausia įdiegite sisteminius paketus, kurie reikalingi tam, kad
konfigūravimo priemonė esanti šioje repozitorijoje veiktų::

    sudo apt install python-pip
    sudo pip install ansible

Tada kompiuterio konfigūravimą galite atlikti taip::

    ansible-playbook setup.yml

Ubuntu diegimas
===============

Pasirinkite Ubuntu 14.04 LTS versiją, kadangi su šia versija yra testuota
konfigūravimo priemonė esanti šioje repozitorijoje.

Prieš diegiant Ubuntu įsitikinkite ar Ubuntu yra `suderinamas su kompiuterio
aparatine įranga`_.

Diegimo metu svarbu susikurti atskirą ``/home`` skirsnį, kuriame bus saugomi
naudotojo duomenys. Vėliau, diegiant naujesnę versiją, naudotojo duomenys bus
išsaugoti, o sistemos skirsnis įrašytas iš naujo.

.. _suderinamas su kompiuterio aparatine įranga: http://www.ubuntu.com/certification/desktop/


Konfigūravimo priemonės testavimas
==================================

Norint įsitikinti ar konfigūravimo priemonė veikia, galite ištestuoti jos
veikimą taip::

  vagrant up

Arba::

  vagrant provision

Leidžiant testus antrą kartą.
