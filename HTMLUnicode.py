#!/usr/bin/env python
# coding: utf-8	

def HTMLUnicode(PageHS):
	PageHS = PageHS.replace(u'&#261;&#769;', u'ą́ ')
	PageHS = PageHS.replace(u'&#596;&#771;', u'ɔ̃')
	PageHS = PageHS.replace(u'&#593;&#771;', u'ɑ̃')
	PageHS = PageHS.replace(u'&#603;&#771;', u'ɛ̃')
	PageHS = PageHS.replace(u'&#339;&#771;', u'œ̃')

	PageHS = PageHS.replace(u'&#224;', u'à')
	PageHS = PageHS.replace(u'&#225;', u'á')
	PageHS = PageHS.replace(u'&#226;', u'â')
	PageHS = PageHS.replace(u'&#259;', u'ă')
	PageHS = PageHS.replace(u'&#228;', u'ä')
	PageHS = PageHS.replace(u'&#261;', u'ą')
	PageHS = PageHS.replace(u'&#227;', u'ã')
	PageHS = PageHS.replace(u'&#230;', u'æ')
	PageHS = PageHS.replace(u'&#231;', u'ç')
	PageHS = PageHS.replace(u'&#269;', u'č')
	PageHS = PageHS.replace(u'&#240;', u'ð')
	PageHS = PageHS.replace(u'&#233;', u'é')
	PageHS = PageHS.replace(u'&#232;', u'è')
	PageHS = PageHS.replace(u'&#234;', u'ê')
	PageHS = PageHS.replace(u'&#235;', u'ë')
	PageHS = PageHS.replace(u'&#235;', u'ë')
	PageHS = PageHS.replace(u'&#817;', u'e̱')
	PageHS = PageHS.replace(u'&#281;', u'ę')
	PageHS = PageHS.replace(u'&#287;', u'ğ')
	PageHS = PageHS.replace(u'&#238;', u'î')
	PageHS = PageHS.replace(u'&#237;', u'í')
	PageHS = PageHS.replace(u'&#239;', u'ï')
	PageHS = PageHS.replace(u'&#299;', u'ī')
	PageHS = PageHS.replace(u'&#303;', u'į')
	PageHS = PageHS.replace(u'&#241;', u'ñ')
	PageHS = PageHS.replace(u'&#242;', u'ò')
	PageHS = PageHS.replace(u'&#243;', u'ó')
	PageHS = PageHS.replace(u'&#244;', u'ô')
	PageHS = PageHS.replace(u'&#246;', u'ö')
	PageHS = PageHS.replace(u'&#245;', u'õ')
	PageHS = PageHS.replace(u'&#339;', u'œ')
	PageHS = PageHS.replace(u'&#353;', u'š')
	PageHS = PageHS.replace(u'&#351;', u'ş')
	PageHS = PageHS.replace(u'&#249;', u'ù')
	PageHS = PageHS.replace(u'&#250;', u'ú')
	PageHS = PageHS.replace(u'&#7913;', u'ứ')
	PageHS = PageHS.replace(u'&#251;', u'û')
	PageHS = PageHS.replace(u'&#252;', u'ü')
	PageHS = PageHS.replace(u'&#365;', u'ŭ')
	PageHS = PageHS.replace(u'&#380;', u'ż')
	
	PageHS = PageHS.replace(u'&#260;&#769;', u'Ą́ ')
	PageHS = PageHS.replace(u'&#390;&#771;', u'Ɔ̃')
	PageHS = PageHS.replace(u'&#11373;&#771;', u'Ɑ̃')
	PageHS = PageHS.replace(u'&#400;&#771;', u'Ɛ̃')
	PageHS = PageHS.replace(u'&#338;&#771;', u'Œ̃')

	PageHS = PageHS.replace(u'&#192;', u'À')
	PageHS = PageHS.replace(u'&#193;', u'Á')
	PageHS = PageHS.replace(u'&#194;', u'Â')
	PageHS = PageHS.replace(u'&#258;', u'Ă')
	PageHS = PageHS.replace(u'&#196;', u'Ä')
	PageHS = PageHS.replace(u'&#260;', u'Ą')
	PageHS = PageHS.replace(u'&#195;', u'Ã')
	PageHS = PageHS.replace(u'&#198;', u'Æ')
	PageHS = PageHS.replace(u'&#199;', u'Ç')
	PageHS = PageHS.replace(u'&#268;', u'Č')
	PageHS = PageHS.replace(u'&#208;', u'Ð')
	PageHS = PageHS.replace(u'&#201;', u'É')
	PageHS = PageHS.replace(u'&#200;', u'È')
	PageHS = PageHS.replace(u'&#202;', u'Ê')
	PageHS = PageHS.replace(u'&#203;', u'Ë')
	PageHS = PageHS.replace(u'&#203;', u'Ë')
	PageHS = PageHS.replace(u'E&#817;', u'E̱')
	PageHS = PageHS.replace(u'&#280;', u'Ę')
	PageHS = PageHS.replace(u'&#286;', u'Ğ')
	PageHS = PageHS.replace(u'&#206;', u'Î')
	PageHS = PageHS.replace(u'&#205;', u'Í')
	PageHS = PageHS.replace(u'&#207;', u'Ï')
	PageHS = PageHS.replace(u'&#298;', u'Ī')
	PageHS = PageHS.replace(u'&#302;', u'Į')
	PageHS = PageHS.replace(u'&#209;', u'Ñ')
	PageHS = PageHS.replace(u'&#210;', u'Ò')
	PageHS = PageHS.replace(u'&#211;', u'Ó')
	PageHS = PageHS.replace(u'&#212;', u'Ô')
	PageHS = PageHS.replace(u'&#214;', u'Ö')
	PageHS = PageHS.replace(u'&#213;', u'Õ')
	PageHS = PageHS.replace(u'&#338;', u'Œ')
	PageHS = PageHS.replace(u'&#352;', u'Š')
	PageHS = PageHS.replace(u'&#350;', u'Ş')
	PageHS = PageHS.replace(u'&#217;', u'Ù')
	PageHS = PageHS.replace(u'&#218;', u'Ú')
	PageHS = PageHS.replace(u'&#7912;', u'Ứ')
	PageHS = PageHS.replace(u'&#219;', u'Û')
	PageHS = PageHS.replace(u'&#220;', u'Ü')
	PageHS = PageHS.replace(u'&#364;', u'Ŭ')
	PageHS = PageHS.replace(u'&#379;', u'Ż')
	
	PageHS = PageHS.replace(u'&#223;', u'ß')
	PageHS = PageHS.replace(u'&#305;', u'ı')
	PageHS = PageHS.replace(u'&#688;', u'ʰ')
	PageHS = PageHS.replace(u'&#700;', u'\'')
	PageHS = PageHS.replace(u'&#8217;', u'’')
	PageHS = PageHS.replace(u'&#35;', u'#')
	PageHS = PageHS.replace(u'&#32;', u'&nbsp;')
	PageHS = PageHS.replace(u'&#451;', u'ǃ')
	PageHS = PageHS.replace(u'&#8265;', u'⁉')
	
	# grec
	PageHS = PageHS.replace(u'&#945;', u'α')
	PageHS = PageHS.replace(u'&#913;', u'Α')
	PageHS = PageHS.replace(u'&#946;', u'β')
	PageHS = PageHS.replace(u'&#914;', u'Β')
	PageHS = PageHS.replace(u'&#976;', u'ϐ')
	PageHS = PageHS.replace(u'&#947;', u'γ')
	PageHS = PageHS.replace(u'&#915;', u'Γ')
	PageHS = PageHS.replace(u'&#948;', u'δ')
	PageHS = PageHS.replace(u'&#916;', u'Δ')
	PageHS = PageHS.replace(u'&#949;', u'ε')
	PageHS = PageHS.replace(u'&#917;', u'Ε')
	PageHS = PageHS.replace(u'&#950;', u'ζ')
	PageHS = PageHS.replace(u'&#918;', u'Ζ')
	PageHS = PageHS.replace(u'&#951;', u'η')
	PageHS = PageHS.replace(u'&#919;', u'Η')
	PageHS = PageHS.replace(u'&#881;', u'ͱ')
	PageHS = PageHS.replace(u'&#880;', u'Ͱ')
	PageHS = PageHS.replace(u'&#952;', u'θ')
	PageHS = PageHS.replace(u'&#920;', u'Θ')
	PageHS = PageHS.replace(u'&#977;', u'ϑ')
	PageHS = PageHS.replace(u'&#1012;', u'ϴ')
	PageHS = PageHS.replace(u'&#953;', u'ι')
	PageHS = PageHS.replace(u'&#921;', u'Ι')
	PageHS = PageHS.replace(u'&#954;', u'κ')
	PageHS = PageHS.replace(u'&#922;', u'Κ')
	PageHS = PageHS.replace(u'&#1008;', u'ϰ')
	PageHS = PageHS.replace(u'&#955;', u'λ')
	PageHS = PageHS.replace(u'&#923;', u'Λ')
	PageHS = PageHS.replace(u'&#956;', u'μ')
	PageHS = PageHS.replace(u'&#924;', u'Μ')
	PageHS = PageHS.replace(u'&#957;', u'ν')
	PageHS = PageHS.replace(u'&#925;', u'Ν')
	PageHS = PageHS.replace(u'&#958;', u'ξ')
	PageHS = PageHS.replace(u'&#926;', u'Ξ')
	PageHS = PageHS.replace(u'&#959;', u'ο')
	PageHS = PageHS.replace(u'&#927;', u'Ο')
	PageHS = PageHS.replace(u'&#339;', u'œ')
	PageHS = PageHS.replace(u'&#338;', u'Œ')
	PageHS = PageHS.replace(u'&#960;', u'π')
	PageHS = PageHS.replace(u'&#928;', u'Π')
	PageHS = PageHS.replace(u'&#982;', u'ϖ')
	PageHS = PageHS.replace(u'&#961;', u'ρ')
	PageHS = PageHS.replace(u'&#929;', u'Ρ')
	PageHS = PageHS.replace(u'&#1009;', u'ϱ')
	PageHS = PageHS.replace(u'&#963;', u'σ')
	PageHS = PageHS.replace(u'&#931;', u'Σ')
	PageHS = PageHS.replace(u'&#962;', u'ς')
	PageHS = PageHS.replace(u'&#1010;', u'ϲ')
	PageHS = PageHS.replace(u'&#1017;', u'Ϲ')
	PageHS = PageHS.replace(u'&#964;', u'τ')
	PageHS = PageHS.replace(u'&#932;', u'Τ')
	PageHS = PageHS.replace(u'&#965;', u'υ')
	PageHS = PageHS.replace(u'&#933;', u'Υ')
	PageHS = PageHS.replace(u'&#966;', u'φ')
	PageHS = PageHS.replace(u'&#934;', u'Φ')
	PageHS = PageHS.replace(u'&#981;', u'ϕ')
	PageHS = PageHS.replace(u'&#935;', u'Χ')
	PageHS = PageHS.replace(u'&#967;', u'χ')
	PageHS = PageHS.replace(u'&#969;', u'ω')
	PageHS = PageHS.replace(u'&#983;', u'ϗ')
	PageHS = PageHS.replace(u'&#991;', u'ϟ')
	PageHS = PageHS.replace(u'&#990;', u'Ϟ')
	PageHS = PageHS.replace(u'&#993;', u'ϡ')
	PageHS = PageHS.replace(u'&#1016;', u'ϸ')
	PageHS = PageHS.replace(u'&#1015;', u'Ϸ')
	PageHS = PageHS.replace(u'&#8016;', u'ὐ')
	PageHS = PageHS.replace(u'&#973;', u'ύ')
	
	# russe
	PageHS = PageHS.replace(u'&#1072;', u'а')
	PageHS = PageHS.replace(u'&#1040;', u'А')
	PageHS = PageHS.replace(u'&#1073;', u'б')
	PageHS = PageHS.replace(u'&#1041;', u'Б')
	PageHS = PageHS.replace(u'&#1074;', u'в')
	PageHS = PageHS.replace(u'&#1042;', u'В')
	PageHS = PageHS.replace(u'&#1075;', u'г')
	PageHS = PageHS.replace(u'&#1043;', u'Г')
	PageHS = PageHS.replace(u'&#1076;', u'д')
	PageHS = PageHS.replace(u'&#1044;', u'Д')
	PageHS = PageHS.replace(u'&#1045;', u'Е')
	PageHS = PageHS.replace(u'&#1077;', u'е')
	PageHS = PageHS.replace(u'&#1105;', u'ё')
	PageHS = PageHS.replace(u'&#1025;', u'Ё')
	PageHS = PageHS.replace(u'&#1078;', u'ж')
	PageHS = PageHS.replace(u'&#1046;', u'Ж')
	PageHS = PageHS.replace(u'&#1079;', u'з')
	PageHS = PageHS.replace(u'&#1047;', u'З')
	PageHS = PageHS.replace(u'&#1080;', u'и')
	PageHS = PageHS.replace(u'&#1048;', u'И')
	PageHS = PageHS.replace(u'&#1081;', u'й')
	PageHS = PageHS.replace(u'&#1049;', u'Й')
	PageHS = PageHS.replace(u'&#1082;', u'к')
	PageHS = PageHS.replace(u'&#1050;', u'К')
	PageHS = PageHS.replace(u'&#1083;', u'л')
	PageHS = PageHS.replace(u'&#1051;', u'Л')
	PageHS = PageHS.replace(u'&#1084;', u'м')
	PageHS = PageHS.replace(u'&#1052;', u'М')
	PageHS = PageHS.replace(u'&#1085;', u'н')
	PageHS = PageHS.replace(u'&#1053;', u'Н')
	PageHS = PageHS.replace(u'&#1086;', u'о')
	PageHS = PageHS.replace(u'&#1054;', u'О')
	PageHS = PageHS.replace(u'&#1087;', u'п')
	PageHS = PageHS.replace(u'&#1055;', u'П')
	PageHS = PageHS.replace(u'&#1088;', u'р')
	PageHS = PageHS.replace(u'&#1056;', u'Р')
	PageHS = PageHS.replace(u'&#1089;', u'с')
	PageHS = PageHS.replace(u'&#1057;', u'С')
	PageHS = PageHS.replace(u'&#1090;', u'т')
	PageHS = PageHS.replace(u'&#1058;', u'Т')
	PageHS = PageHS.replace(u'&#1091;', u'у')
	PageHS = PageHS.replace(u'&#1059;', u'У')
	PageHS = PageHS.replace(u'&#1092;', u'ф')
	PageHS = PageHS.replace(u'&#1060;', u'Ф')
	PageHS = PageHS.replace(u'&#1093;', u'х')
	PageHS = PageHS.replace(u'&#1061;', u'Х')
	PageHS = PageHS.replace(u'&#1094;', u'ц')
	PageHS = PageHS.replace(u'&#1062;', u'Ц')
	PageHS = PageHS.replace(u'&#1095;', u'ч')
	PageHS = PageHS.replace(u'&#1063;', u'Ч')
	PageHS = PageHS.replace(u'&#1096;', u'ш')
	PageHS = PageHS.replace(u'&#1064;', u'Ш')
	PageHS = PageHS.replace(u'&#1097;', u'щ')
	PageHS = PageHS.replace(u'&#1065;', u'Щ')
	PageHS = PageHS.replace(u'&#1098;', u'ъ')
	PageHS = PageHS.replace(u'&#1066;', u'Ъ')
	PageHS = PageHS.replace(u'&#1099;', u'ы')
	PageHS = PageHS.replace(u'&#1067;', u'Ы')
	PageHS = PageHS.replace(u'&#1100;', u'ь')
	PageHS = PageHS.replace(u'&#1068;', u'Ь')
	PageHS = PageHS.replace(u'&#1069;', u'Э')
	PageHS = PageHS.replace(u'&#1101;', u'э')
	PageHS = PageHS.replace(u'&#1102;', u'ю')
	PageHS = PageHS.replace(u'&#1070;', u'Ю')
	PageHS = PageHS.replace(u'&#1103;', u'я')
	PageHS = PageHS.replace(u'&#1071;', u'Я')
	PageHS = PageHS.replace(u'&#1112;', u'ј')
	PageHS = PageHS.replace(u'&#1032;', u'Ј')
	PageHS = PageHS.replace(u'&#277;', u'ĕ')
	PageHS = PageHS.replace(u'&#276;', u'Ĕ')
	PageHS = PageHS.replace(u'&#943;', u'ί')
	PageHS = PageHS.replace(u'&#906;', u'Ί')
	PageHS = PageHS.replace(u'&#972;', u'ό')
	PageHS = PageHS.replace(u'&#908;', u'Ό')
	PageHS = PageHS.replace(u'&#974;', u'ώ')
	PageHS = PageHS.replace(u'&#911;', u'Ώ')
	PageHS = PageHS.replace(u'&#7954;', u'ἒ')
	PageHS = PageHS.replace(u'&#7962;', u'Ἒ')
	PageHS = PageHS.replace(u'&#941;', u'έ')
	PageHS = PageHS.replace(u'&#904;', u'Έ')
	PageHS = PageHS.replace(u'&#7937;', u'ἁ')
	PageHS = PageHS.replace(u'&#7945;', u'Ἁ')
	
	# arabe
	PageHS = PageHS.replace(u'&#1600;&#1614;', u'ـَ')
	PageHS = PageHS.replace(u'&#1600;&#1615;', u'ـُ')
	PageHS = PageHS.replace(u'&#1600;&#1616;', u'ـِ')
	PageHS = PageHS.replace(u'&#1600;&#1617;', u'ـّ')
	PageHS = PageHS.replace(u'&#1600;&#1618;', u'ـْ')
	PageHS = PageHS.replace(u'&#1600;&#1648;', u'ـٰ')
	PageHS = PageHS.replace(u'&#1601;', u'ف')
	PageHS = PageHS.replace(u'&#1602;', u'ق')
	PageHS = PageHS.replace(u'&#1603;', u'ك')
	PageHS = PageHS.replace(u'&#1604;', u'ل')
	PageHS = PageHS.replace(u'&#1604;&#1575;', u'لا')
	PageHS = PageHS.replace(u'&#1605;', u'م')
	PageHS = PageHS.replace(u'&#1606;', u'ن')
	PageHS = PageHS.replace(u'&#1607;', u'ه')
	PageHS = PageHS.replace(u'&#1608;', u'و')
	PageHS = PageHS.replace(u'&#1610;', u'ي')
	PageHS = PageHS.replace(u'&#8205;&#65194;', u'ﺪ')
	PageHS = PageHS.replace(u'&#8205;&#65196;', u'ﺬ')
	PageHS = PageHS.replace(u'&#8205;&#65264;', u'ﻰ')
	PageHS = PageHS.replace(u'&#8205;&#65276;', u'‍ﻼ')
	PageHS = PageHS.replace(u'&#65194;', u'ﺪ')
	PageHS = PageHS.replace(u'&#65196;', u'ﺬ')
	PageHS = PageHS.replace(u'&#65218;', u'ﻂ')
	PageHS = PageHS.replace(u'&#65263;', u'ﻯ')
	PageHS = PageHS.replace(u'&#1583;&#1614;', u'دَ')
	PageHS = PageHS.replace(u'&#1583;&#1614;&#1575;', u'دَا')
	PageHS = PageHS.replace(u'&#1583;&#1614;&#1609;', u'دَى')
	PageHS = PageHS.replace(u'&#1583;&#1615;', u'دُ')
	PageHS = PageHS.replace(u'&#1583;&#1615;&#1608;', u'دُو')
	PageHS = PageHS.replace(u'&#1583;&#1616;', u'دِ')
	PageHS = PageHS.replace(u'&#1583;&#1616;&#1610;', u'دِي')
	PageHS = PageHS.replace(u'&#1584;&#1648;', u'ذٰ')
	PageHS = PageHS.replace(u'&#1600;&#1614;&#1575;', u'ـَا')
	PageHS = PageHS.replace(u'&#1600;&#1614;&#1609;', u'ـَى')
	PageHS = PageHS.replace(u'&#1600;&#1615;&#1608;', u'ـُو')
	PageHS = PageHS.replace(u'&#1600;&#1616;&#1610;', u'ـِي')
	PageHS = PageHS.replace(u'&#1604;&#1648;', u'لٰ')
	PageHS = PageHS.replace(u'&#1605;&#1648;', u'مٰ')
	PageHS = PageHS.replace(u'&#1607;&#1648;', u'هٰ')
	PageHS = PageHS.replace(u'&#8205;&#1575;', u'‍ا')
	PageHS = PageHS.replace(u'&#8205;&#1594;', u'غ')
	PageHS = PageHS.replace(u'&#8205;&#65166;', u'ﺎ')
	PageHS = PageHS.replace(u'&#8205;&#65168;', u'ﺐ')
	PageHS = PageHS.replace(u'&#8205;&#65169;', u'ﺑ')
	PageHS = PageHS.replace(u'&#8205;&#65170;', u'ﺒ')
	PageHS = PageHS.replace(u'&#8205;&#65172;', u'ﺔ')
	PageHS = PageHS.replace(u'&#8205;&#65174;', u'ﺖ')
	PageHS = PageHS.replace(u'&#8205;&#65176;', u'ﺘ')
	PageHS = PageHS.replace(u'&#8205;&#65178;', u'‍ﺚ')
	PageHS = PageHS.replace(u'&#8205;&#65179;', u'ﺛ')
	PageHS = PageHS.replace(u'&#8205;&#65180;', u'‍ﺜ')
	PageHS = PageHS.replace(u'&#8205;&#65182;', u'ﺞ')
	PageHS = PageHS.replace(u'&#8205;&#65186;', u'ﺢ')
	PageHS = PageHS.replace(u'&#8205;&#65187;', u'ﺣ')
	PageHS = PageHS.replace(u'&#8205;&#65188;', u'ﺤ')
	PageHS = PageHS.replace(u'&#8205;&#65190;', u'ﺦ')
	PageHS = PageHS.replace(u'&#8205;&#65191;', u'ﺧ')
	PageHS = PageHS.replace(u'&#8205;&#65198;', u'ﺮ')
	PageHS = PageHS.replace(u'&#8205;&#65200;', u'ﺰ')
	PageHS = PageHS.replace(u'&#8205;&#65202;', u'‍ﺲ')
	PageHS = PageHS.replace(u'&#8205;&#65214;', u'ﺾ')
	PageHS = PageHS.replace(u'&#8205;&#65218;', u'ﻂ')
	PageHS = PageHS.replace(u'&#8205;&#65222;', u'ﻆ')
	PageHS = PageHS.replace(u'&#8205;&#65226;', u'ﻊ')
	PageHS = PageHS.replace(u'&#8205;&#65230;', u'ﻎ')
	PageHS = PageHS.replace(u'&#8205;&#65234;', u'ﻒ')
	PageHS = PageHS.replace(u'&#8205;&#65238;', u'ﻖ')
	PageHS = PageHS.replace(u'&#8205;&#65242;', u'‍ﻚ')
	PageHS = PageHS.replace(u'&#8205;&#65246;', u'ﻞ')
	PageHS = PageHS.replace(u'&#8205;&#65250;', u'ﻢ')
	PageHS = PageHS.replace(u'&#8205;&#65254;', u'ﻦ')
	PageHS = PageHS.replace(u'&#8205;&#65258;', u'ﻪ')
	PageHS = PageHS.replace(u'&#8205;&#65262;', u'ﻮ‍')
	PageHS = PageHS.replace(u'&#8205;&#65266;', u'ﻲ')
	PageHS = PageHS.replace(u'&#65206;&#8205;', u'ﺶ‍')
	PageHS = PageHS.replace(u'&#65210;&#8205;', u'ﺺ‍')
	
	PageHS = PageHS.replace(u'&#1569;', u'ء')
	PageHS = PageHS.replace(u'&#1570;', u'آ')
	PageHS = PageHS.replace(u'&#1575;', u'ا')
	PageHS = PageHS.replace(u'&#1576;', u'ب')
	PageHS = PageHS.replace(u'&#1577;', u'ة')
	PageHS = PageHS.replace(u'&#1578;', u'ت')
	PageHS = PageHS.replace(u'&#1579;', u'ث')
	PageHS = PageHS.replace(u'&#1580;', u'ج')
	PageHS = PageHS.replace(u'&#1581;', u'ح')
	PageHS = PageHS.replace(u'&#1582;', u'خ')
	PageHS = PageHS.replace(u'&#1583;', u'د')
	PageHS = PageHS.replace(u'&#1584;', u'ذ')
	PageHS = PageHS.replace(u'&#1585;', u'ر')
	PageHS = PageHS.replace(u'&#1586;', u'ز')
	PageHS = PageHS.replace(u'&#1587;', u'س')
	PageHS = PageHS.replace(u'&#1588;', u'ش')
	PageHS = PageHS.replace(u'&#1589;', u'ص')
	PageHS = PageHS.replace(u'&#1590;', u'ض')
	PageHS = PageHS.replace(u'&#1591;', u'ط')
	PageHS = PageHS.replace(u'&#1592;', u'ظ')
	PageHS = PageHS.replace(u'&#1593;', u'ع')
	PageHS = PageHS.replace(u'&#1594;', u'غ')
	PageHS = PageHS.replace(u'&#65166;', u'ﺎ')
	PageHS = PageHS.replace(u'&#65168;', u'ﺐ')
	PageHS = PageHS.replace(u'&#65169;', u'ﺑ')
	PageHS = PageHS.replace(u'&#65170;', u'ﺒ')
	PageHS = PageHS.replace(u'&#65174;', u'ﺖ')
	PageHS = PageHS.replace(u'&#65175;', u'ﺗ')
	PageHS = PageHS.replace(u'&#65176;', u'ﺘ')
	PageHS = PageHS.replace(u'&#65178;', u'ﺚ')
	PageHS = PageHS.replace(u'&#65179;', u'ﺛ')
	PageHS = PageHS.replace(u'&#65180;', u'ﺜ')
	PageHS = PageHS.replace(u'&#65182;', u'ﺞ')
	PageHS = PageHS.replace(u'&#65183;', u'ﺟ')
	PageHS = PageHS.replace(u'&#65184;', u'ﺠ')
	PageHS = PageHS.replace(u'&#65186;', u'ﺢ')
	PageHS = PageHS.replace(u'&#65187;', u'ﺣ')
	PageHS = PageHS.replace(u'&#65188;', u'ﺤ')
	PageHS = PageHS.replace(u'&#65190;', u'ﺦ')
	PageHS = PageHS.replace(u'&#65191;', u'ﺧ')
	PageHS = PageHS.replace(u'&#65192;', u'ﺨ')
	PageHS = PageHS.replace(u'&#65198;', u'ﺮ')
	PageHS = PageHS.replace(u'&#65200;', u'ﺰ')
	PageHS = PageHS.replace(u'&#65202;', u'ﺲ')
	PageHS = PageHS.replace(u'&#65203;', u'ﺳ')
	PageHS = PageHS.replace(u'&#65204;', u'ﺴ')
	PageHS = PageHS.replace(u'&#65206;', u'ﺶ')
	PageHS = PageHS.replace(u'&#65207;', u'ﺷ')
	PageHS = PageHS.replace(u'&#65208;', u'ﺸ')
	PageHS = PageHS.replace(u'&#65210;', u'ﺺ')
	PageHS = PageHS.replace(u'&#65211;', u'ﺻ')
	PageHS = PageHS.replace(u'&#65212;', u'ﺼ')
	PageHS = PageHS.replace(u'&#65214;', u'ﺾ')
	PageHS = PageHS.replace(u'&#65215;', u'ﺿ')
	PageHS = PageHS.replace(u'&#65216;', u'ﻀ')
	PageHS = PageHS.replace(u'&#65219;', u'ﻃ')
	PageHS = PageHS.replace(u'&#65220;', u'ﻄ')
	PageHS = PageHS.replace(u'&#65222;', u'ﻆ')
	PageHS = PageHS.replace(u'&#65223;', u'ﻇ')
	PageHS = PageHS.replace(u'&#65224;', u'ﻈ')
	PageHS = PageHS.replace(u'&#65227;', u'ﻋ')
	PageHS = PageHS.replace(u'&#65228;', u'ﻌ')
	PageHS = PageHS.replace(u'&#65230;', u'ﻎ')
	PageHS = PageHS.replace(u'&#65231;', u'ﻏ')
	PageHS = PageHS.replace(u'&#65232;', u'ﻐ')
	PageHS = PageHS.replace(u'&#65234;', u'ﻒ')
	PageHS = PageHS.replace(u'&#65235;', u'ﻓ')
	PageHS = PageHS.replace(u'&#65236;', u'ﻔ')
	PageHS = PageHS.replace(u'&#65238;', u'ﻖ')
	PageHS = PageHS.replace(u'&#65239;', u'ﻗ')
	PageHS = PageHS.replace(u'&#65240;', u'ﻘ')
	PageHS = PageHS.replace(u'&#65242;', u'ﻚ')
	PageHS = PageHS.replace(u'&#65243;', u'ﻛ')
	PageHS = PageHS.replace(u'&#65244;', u'ﻜ')
	PageHS = PageHS.replace(u'&#65246;', u'ﻞ')
	PageHS = PageHS.replace(u'&#65247;', u'ﻟ')
	PageHS = PageHS.replace(u'&#65248;', u'ﻠ')
	PageHS = PageHS.replace(u'&#65250;', u'ﻢ')
	PageHS = PageHS.replace(u'&#65251;', u'ﻣ')
	PageHS = PageHS.replace(u'&#65252;', u'ﻤ')
	PageHS = PageHS.replace(u'&#65254;', u'ﻦ')
	PageHS = PageHS.replace(u'&#65255;', u'ﻧ')
	PageHS = PageHS.replace(u'&#65256;', u'ﻨ')
	PageHS = PageHS.replace(u'&#65258;', u'ﻪ')
	PageHS = PageHS.replace(u'&#65259;', u'ﻫ')
	PageHS = PageHS.replace(u'&#65260;', u'ﻬ')
	PageHS = PageHS.replace(u'&#65262;', u'ﻮ')
	PageHS = PageHS.replace(u'&#65266;', u'ﻲ')
	PageHS = PageHS.replace(u'&#65267;', u'ﻳ')
	PageHS = PageHS.replace(u'&#65268;', u'ﻴ')
	PageHS = PageHS.replace(u'&#1736;', u'ۈ')
	PageHS = PageHS.replace(u'&#1739;', u'ۋ')
	PageHS = PageHS.replace(u'&#1735;', u'ۇ')
	PageHS = PageHS.replace(u'&#1726;', u'ھ')
	PageHS = PageHS.replace(u'&#1662;', u'پ')
	
	# hébreu
	PageHS = PageHS.replace(u'&#1488;', u'א')
	PageHS = PageHS.replace(u'&#1489;', u'ב')
	PageHS = PageHS.replace(u'&#1490;', u'ג')
	PageHS = PageHS.replace(u'&#1491;', u'ד')
	PageHS = PageHS.replace(u'&#1492;', u'ה')
	PageHS = PageHS.replace(u'&#1493;', u'ו')
	PageHS = PageHS.replace(u'&#1494;', u'ז')
	PageHS = PageHS.replace(u'&#1495;', u'ח')
	PageHS = PageHS.replace(u'&#1496;', u'ט')
	PageHS = PageHS.replace(u'&#1497;', u'י')
	PageHS = PageHS.replace(u'&#1499;', u'כ')
	PageHS = PageHS.replace(u'&#1500;', u'ל')
	PageHS = PageHS.replace(u'&#1502;', u'מ')
	PageHS = PageHS.replace(u'&#1504;', u'נ')
	PageHS = PageHS.replace(u'&#1505;', u'ס')
	PageHS = PageHS.replace(u'&#1506;', u'ע')
	PageHS = PageHS.replace(u'&#1508;', u'פ')
	PageHS = PageHS.replace(u'&#1510;', u'צ')
	PageHS = PageHS.replace(u'&#1511;', u'ק')
	PageHS = PageHS.replace(u'&#1512;', u'ר')
	PageHS = PageHS.replace(u'&#1513;', u'ש')
	PageHS = PageHS.replace(u'&#1514;', u'ת')
	PageHS = PageHS.replace(u'&#1498;', u'ך')
	PageHS = PageHS.replace(u'&#1501;', u'ם')
	PageHS = PageHS.replace(u'&#1503;', u'ן')
	PageHS = PageHS.replace(u'&#1507;', u'ף')
	PageHS = PageHS.replace(u'&#1509;', u'ץ')
	PageHS = PageHS.replace(u'&#1523;', u'׳')

	# dévanagari
	PageHS = PageHS.replace(u'&#2344;&#2381;&#2344;&#2368;', u'न्नी')
	
	PageHS = PageHS.replace(u'&#2357;&#2366;&#2305;', u'वाँ')
	PageHS = PageHS.replace(u'&#2348;&#2381;&#2342;', u'ब्द')
	PageHS = PageHS.replace(u'&#2346;&#2366;&#2305;', u'पाँ')
	PageHS = PageHS.replace(u'&#2342;&#2381;&#2352;', u'द्र')
	
	PageHS = PageHS.replace(u'&#2309;&#2306;', u'अं')
	PageHS = PageHS.replace(u'&#2325;&#2364;', u'क़')
	PageHS = PageHS.replace(u'&#2326;&#2364;', u'ख़')
	PageHS = PageHS.replace(u'&#2327;&#2364;', u'ग़')
	PageHS = PageHS.replace(u'&#2332;&#2364;', u'ज़')
	PageHS = PageHS.replace(u'&#2337;&#2364;', u'ड़')
	PageHS = PageHS.replace(u'&#2338;&#2364;', u'ढ़')
	PageHS = PageHS.replace(u'&#2347;&#2364;', u'फ़')
	PageHS = PageHS.replace(u'&#2344;&#2367;', u'नि')
	PageHS = PageHS.replace(u'&#2357;&#2375;', u'वे')
	PageHS = PageHS.replace(u'&#2354;&#2379;', u'लो')
	PageHS = PageHS.replace(u'&#2325;&#2364;', u'क़')
	PageHS = PageHS.replace(u'&#2342;&#2368;', u'दी')
	PageHS = PageHS.replace(u'&#2358;&#2375;', u'शे')
	PageHS = PageHS.replace(u'&#2360;&#2306;', u'सं')
	PageHS = PageHS.replace(u'&#2337;&#2366;', u'डा')
	PageHS = PageHS.replace(u'&#2360;&#2366;', u'सा')
	PageHS = PageHS.replace(u'&#2358;&#2366;', u'शा')
	PageHS = PageHS.replace(u'&#2340;&#2366;', u'ता')
	PageHS = PageHS.replace(u'&#2348;&#2381;', u'ब्')
	PageHS = PageHS.replace(u'&#2325;&#2381;', u'क्')
	PageHS = PageHS.replace(u'&#2349;&#2370;', u'भू')
	PageHS = PageHS.replace(u'&#2348;&#2368;', u'बी')
	PageHS = PageHS.replace(u'&#2346;&#2381;', u'प्')
	PageHS = PageHS.replace(u'&#2346;&#2306;', u'पं')
	#PageHS = PageHS.replace(u'&#2336;&#2366;', 'ठा')
	#PageHS = PageHS.replace(u'&#2327;&#2369;', 'गु')
	#PageHS = PageHS.replace(u'&#2344;&#2380;', 'नौ')
	
	PageHS = PageHS.replace(u'&#2309;', u'अ')
	PageHS = PageHS.replace(u'&#2310;', u'आ')
	PageHS = PageHS.replace(u'&#2311;', u'इ')
	PageHS = PageHS.replace(u'&#2312;', u'ई')
	PageHS = PageHS.replace(u'&#2313;', u'उ')
	PageHS = PageHS.replace(u'&#2314;', u'ऊ')
	PageHS = PageHS.replace(u'&#2315;', u'ऋ')
	PageHS = PageHS.replace(u'&#2319;', u'ए')
	PageHS = PageHS.replace(u'&#2320;', u'ऐ')
	PageHS = PageHS.replace(u'&#2323;', u'ओ')
	PageHS = PageHS.replace(u'&#2324;', u'औ')
	PageHS = PageHS.replace(u'&#2325;', u'क')
	PageHS = PageHS.replace(u'&#2326;', u'ख')
	PageHS = PageHS.replace(u'&#2327;', u'ग')
	PageHS = PageHS.replace(u'&#2328;', u'घ')
	PageHS = PageHS.replace(u'&#2330;', u'च')
	PageHS = PageHS.replace(u'&#2331;', u'छ')
	PageHS = PageHS.replace(u'&#2332;', u'ज')
	PageHS = PageHS.replace(u'&#2333;', u'झ')
	PageHS = PageHS.replace(u'&#2334;', u'ञ')
	PageHS = PageHS.replace(u'&#2335;', u'ट')
	PageHS = PageHS.replace(u'&#2336;', u'ठ')
	PageHS = PageHS.replace(u'&#2337;', u'ड')
	PageHS = PageHS.replace(u'&#2338;', u'ढ')
	PageHS = PageHS.replace(u'&#2339;', u'ण')
	PageHS = PageHS.replace(u'&#2340;', u'त')
	PageHS = PageHS.replace(u'&#2341;', u'थ')
	PageHS = PageHS.replace(u'&#2342;', u'द')
	PageHS = PageHS.replace(u'&#2343;', u'ध')
	PageHS = PageHS.replace(u'&#2344;', u'न')
	PageHS = PageHS.replace(u'&#2346;', u'प')
	PageHS = PageHS.replace(u'&#2347;', u'फ')
	PageHS = PageHS.replace(u'&#2348;', u'ब')
	PageHS = PageHS.replace(u'&#2349;', u'भ')
	PageHS = PageHS.replace(u'&#2350;', u'म')
	PageHS = PageHS.replace(u'&#2351;', u'य')
	PageHS = PageHS.replace(u'&#2352;', u'र')
	PageHS = PageHS.replace(u'&#2354;', u'ल')
	PageHS = PageHS.replace(u'&#2357;', u'व')
	PageHS = PageHS.replace(u'&#2358;', u'श')
	PageHS = PageHS.replace(u'&#2359;', u'ष')
	PageHS = PageHS.replace(u'&#2360;', u'स')
	PageHS = PageHS.replace(u'&#2361;', u'ह')
	PageHS = PageHS.replace(u'&#2404;', u'।')
	
	# japonais
	PageHS = PageHS.replace(u'&#12539;', u'・')
	
	return PageHS
	  
