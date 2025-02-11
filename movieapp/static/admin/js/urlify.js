/*global XRegExp*/
'use strict';
{
    const LATIN_MAP = {
        'Ã€': 'A', 'Ã': 'A', 'Ã‚': 'A', 'Ãƒ': 'A', 'Ã„': 'A', 'Ã…': 'A', 'Ã†': 'AE',
        'Ã‡': 'C', 'Ãˆ': 'E', 'Ã‰': 'E', 'ÃŠ': 'E', 'Ã‹': 'E', 'ÃŒ': 'I', 'Ã': 'I',
        'Ã': 'I', 'Ã': 'I', 'Ã': 'D', 'Ã‘': 'N', 'Ã’': 'O', 'Ã“': 'O', 'Ã”': 'O',
        'Ã•': 'O', 'Ã–': 'O', 'Å': 'O', 'Ã˜': 'O', 'Ã™': 'U', 'Ãš': 'U', 'Ã›': 'U',
        'Ãœ': 'U', 'Å°': 'U', 'Ã': 'Y', 'Ã': 'TH', 'Å¸': 'Y', 'ÃŸ': 'ss', 'Ã ': 'a',
        'Ã¡': 'a', 'Ã¢': 'a', 'Ã£': 'a', 'Ã¤': 'a', 'Ã¥': 'a', 'Ã¦': 'ae', 'Ã§': 'c',
        'Ã¨': 'e', 'Ã©': 'e', 'Ãª': 'e', 'Ã«': 'e', 'Ã¬': 'i', 'Ã­': 'i', 'Ã®': 'i',
        'Ã¯': 'i', 'Ã°': 'd', 'Ã±': 'n', 'Ã²': 'o', 'Ã³': 'o', 'Ã´': 'o', 'Ãµ': 'o',
        'Ã¶': 'o', 'Å‘': 'o', 'Ã¸': 'o', 'Ã¹': 'u', 'Ãº': 'u', 'Ã»': 'u', 'Ã¼': 'u',
        'Å±': 'u', 'Ã½': 'y', 'Ã¾': 'th', 'Ã¿': 'y'
    };
    const LATIN_SYMBOLS_MAP = {
        'Â©': '(c)'
    };
    const GREEK_MAP = {
        'Î±': 'a', 'Î²': 'b', 'Î³': 'g', 'Î´': 'd', 'Îµ': 'e', 'Î¶': 'z', 'Î·': 'h',
        'Î¸': '8', 'Î¹': 'i', 'Îº': 'k', 'Î»': 'l', 'Î¼': 'm', 'Î½': 'n', 'Î¾': '3',
        'Î¿': 'o', 'Ï€': 'p', 'Ï': 'r', 'Ïƒ': 's', 'Ï„': 't', 'Ï…': 'y', 'Ï†': 'f',
        'Ï‡': 'x', 'Ïˆ': 'ps', 'Ï‰': 'w', 'Î¬': 'a', 'Î­': 'e', 'Î¯': 'i', 'ÏŒ': 'o',
        'Ï': 'y', 'Î®': 'h', 'Ï': 'w', 'Ï‚': 's', 'ÏŠ': 'i', 'Î°': 'y', 'Ï‹': 'y',
        'Î': 'i', 'Î‘': 'A', 'Î’': 'B', 'Î“': 'G', 'Î”': 'D', 'Î•': 'E', 'Î–': 'Z',
        'Î—': 'H', 'Î˜': '8', 'Î™': 'I', 'Îš': 'K', 'Î›': 'L', 'Îœ': 'M', 'Î': 'N',
        'Î': '3', 'ÎŸ': 'O', 'Î ': 'P', 'Î¡': 'R', 'Î£': 'S', 'Î¤': 'T', 'Î¥': 'Y',
        'Î¦': 'F', 'Î§': 'X', 'Î¨': 'PS', 'Î©': 'W', 'Î†': 'A', 'Îˆ': 'E', 'ÎŠ': 'I',
        'ÎŒ': 'O', 'Î': 'Y', 'Î‰': 'H', 'Î': 'W', 'Îª': 'I', 'Î«': 'Y'
    };
    const TURKISH_MAP = {
        'ÅŸ': 's', 'Å': 'S', 'Ä±': 'i', 'Ä°': 'I', 'Ã§': 'c', 'Ã‡': 'C', 'Ã¼': 'u',
        'Ãœ': 'U', 'Ã¶': 'o', 'Ã–': 'O', 'ÄŸ': 'g', 'Ä': 'G'
    };
    const ROMANIAN_MAP = {
        'Äƒ': 'a', 'Ã®': 'i', 'È™': 's', 'È›': 't', 'Ã¢': 'a',
        'Ä‚': 'A', 'Ã': 'I', 'È˜': 'S', 'Èš': 'T', 'Ã‚': 'A'
    };
    const RUSSIAN_MAP = {
        'Ğ°': 'a', 'Ğ±': 'b', 'Ğ²': 'v', 'Ğ³': 'g', 'Ğ´': 'd', 'Ğµ': 'e', 'Ñ‘': 'yo',
        'Ğ¶': 'zh', 'Ğ·': 'z', 'Ğ¸': 'i', 'Ğ¹': 'j', 'Ğº': 'k', 'Ğ»': 'l', 'Ğ¼': 'm',
        'Ğ½': 'n', 'Ğ¾': 'o', 'Ğ¿': 'p', 'Ñ€': 'r', 'Ñ': 's', 'Ñ‚': 't', 'Ñƒ': 'u',
        'Ñ„': 'f', 'Ñ…': 'h', 'Ñ†': 'c', 'Ñ‡': 'ch', 'Ñˆ': 'sh', 'Ñ‰': 'sh', 'ÑŠ': '',
        'Ñ‹': 'y', 'ÑŒ': '', 'Ñ': 'e', 'Ñ': 'yu', 'Ñ': 'ya',
        'Ğ': 'A', 'Ğ‘': 'B', 'Ğ’': 'V', 'Ğ“': 'G', 'Ğ”': 'D', 'Ğ•': 'E', 'Ğ': 'Yo',
        'Ğ–': 'Zh', 'Ğ—': 'Z', 'Ğ˜': 'I', 'Ğ™': 'J', 'Ğš': 'K', 'Ğ›': 'L', 'Ğœ': 'M',
        'Ğ': 'N', 'Ğ': 'O', 'ĞŸ': 'P', 'Ğ ': 'R', 'Ğ¡': 'S', 'Ğ¢': 'T', 'Ğ£': 'U',
        'Ğ¤': 'F', 'Ğ¥': 'H', 'Ğ¦': 'C', 'Ğ§': 'Ch', 'Ğ¨': 'Sh', 'Ğ©': 'Sh', 'Ğª': '',
        'Ğ«': 'Y', 'Ğ¬': '', 'Ğ­': 'E', 'Ğ®': 'Yu', 'Ğ¯': 'Ya'
    };
    const UKRAINIAN_MAP = {
        'Ğ„': 'Ye', 'Ğ†': 'I', 'Ğ‡': 'Yi', 'Ò': 'G', 'Ñ”': 'ye', 'Ñ–': 'i',
        'Ñ—': 'yi', 'Ò‘': 'g'
    };
    const CZECH_MAP = {
        'Ä': 'c', 'Ä': 'd', 'Ä›': 'e', 'Åˆ': 'n', 'Å™': 'r', 'Å¡': 's', 'Å¥': 't',
        'Å¯': 'u', 'Å¾': 'z', 'ÄŒ': 'C', 'Ä': 'D', 'Äš': 'E', 'Å‡': 'N', 'Å˜': 'R',
        'Å ': 'S', 'Å¤': 'T', 'Å®': 'U', 'Å½': 'Z'
    };
    const SLOVAK_MAP = {
        'Ã¡': 'a', 'Ã¤': 'a', 'Ä': 'c', 'Ä': 'd', 'Ã©': 'e', 'Ã­': 'i', 'Ä¾': 'l',
        'Äº': 'l', 'Åˆ': 'n', 'Ã³': 'o', 'Ã´': 'o', 'Å•': 'r', 'Å¡': 's', 'Å¥': 't',
        'Ãº': 'u', 'Ã½': 'y', 'Å¾': 'z',
        'Ã': 'a', 'Ã„': 'A', 'ÄŒ': 'C', 'Ä': 'D', 'Ã‰': 'E', 'Ã': 'I', 'Ä½': 'L',
        'Ä¹': 'L', 'Å‡': 'N', 'Ã“': 'O', 'Ã”': 'O', 'Å”': 'R', 'Å ': 'S', 'Å¤': 'T',
        'Ãš': 'U', 'Ã': 'Y', 'Å½': 'Z'
    };
    const POLISH_MAP = {
        'Ä…': 'a', 'Ä‡': 'c', 'Ä™': 'e', 'Å‚': 'l', 'Å„': 'n', 'Ã³': 'o', 'Å›': 's',
        'Åº': 'z', 'Å¼': 'z',
        'Ä„': 'A', 'Ä†': 'C', 'Ä˜': 'E', 'Å': 'L', 'Åƒ': 'N', 'Ã“': 'O', 'Åš': 'S',
        'Å¹': 'Z', 'Å»': 'Z'
    };
    const LATVIAN_MAP = {
        'Ä': 'a', 'Ä': 'c', 'Ä“': 'e', 'Ä£': 'g', 'Ä«': 'i', 'Ä·': 'k', 'Ä¼': 'l',
        'Å†': 'n', 'Å¡': 's', 'Å«': 'u', 'Å¾': 'z',
        'Ä€': 'A', 'ÄŒ': 'C', 'Ä’': 'E', 'Ä¢': 'G', 'Äª': 'I', 'Ä¶': 'K', 'Ä»': 'L',
        'Å…': 'N', 'Å ': 'S', 'Åª': 'U', 'Å½': 'Z'
    };
    const ARABIC_MAP = {
        'Ø£': 'a', 'Ø¨': 'b', 'Øª': 't', 'Ø«': 'th', 'Ø¬': 'g', 'Ø­': 'h', 'Ø®': 'kh', 'Ø¯': 'd',
        'Ø°': 'th', 'Ø±': 'r', 'Ø²': 'z', 'Ø³': 's', 'Ø´': 'sh', 'Øµ': 's', 'Ø¶': 'd', 'Ø·': 't',
        'Ø¸': 'th', 'Ø¹': 'aa', 'Øº': 'gh', 'Ù': 'f', 'Ù‚': 'k', 'Ùƒ': 'k', 'Ù„': 'l', 'Ù…': 'm',
        'Ù†': 'n', 'Ù‡': 'h', 'Ùˆ': 'o', 'ÙŠ': 'y'
    };
    const LITHUANIAN_MAP = {
        'Ä…': 'a', 'Ä': 'c', 'Ä™': 'e', 'Ä—': 'e', 'Ä¯': 'i', 'Å¡': 's', 'Å³': 'u',
        'Å«': 'u', 'Å¾': 'z',
        'Ä„': 'A', 'ÄŒ': 'C', 'Ä˜': 'E', 'Ä–': 'E', 'Ä®': 'I', 'Å ': 'S', 'Å²': 'U',
        'Åª': 'U', 'Å½': 'Z'
    };
    const SERBIAN_MAP = {
        'Ñ’': 'dj', 'Ñ˜': 'j', 'Ñ™': 'lj', 'Ñš': 'nj', 'Ñ›': 'c', 'ÑŸ': 'dz',
        'Ä‘': 'dj', 'Ğ‚': 'Dj', 'Ğˆ': 'j', 'Ğ‰': 'Lj', 'ĞŠ': 'Nj', 'Ğ‹': 'C',
        'Ğ': 'Dz', 'Ä': 'Dj'
    };
    const AZERBAIJANI_MAP = {
        'Ã§': 'c', 'É™': 'e', 'ÄŸ': 'g', 'Ä±': 'i', 'Ã¶': 'o', 'ÅŸ': 's', 'Ã¼': 'u',
        'Ã‡': 'C', 'Æ': 'E', 'Ä': 'G', 'Ä°': 'I', 'Ã–': 'O', 'Å': 'S', 'Ãœ': 'U'
    };
    const GEORGIAN_MAP = {
        'áƒ': 'a', 'áƒ‘': 'b', 'áƒ’': 'g', 'áƒ“': 'd', 'áƒ”': 'e', 'áƒ•': 'v', 'áƒ–': 'z',
        'áƒ—': 't', 'áƒ˜': 'i', 'áƒ™': 'k', 'áƒš': 'l', 'áƒ›': 'm', 'áƒœ': 'n', 'áƒ': 'o',
        'áƒ': 'p', 'áƒŸ': 'j', 'áƒ ': 'r', 'áƒ¡': 's', 'áƒ¢': 't', 'áƒ£': 'u', 'áƒ¤': 'f',
        'áƒ¥': 'q', 'áƒ¦': 'g', 'áƒ§': 'y', 'áƒ¨': 'sh', 'áƒ©': 'ch', 'áƒª': 'c', 'áƒ«': 'dz',
        'áƒ¬': 'w', 'áƒ­': 'ch', 'áƒ®': 'x', 'áƒ¯': 'j', 'áƒ°': 'h'
    };

    const ALL_DOWNCODE_MAPS = [
        LATIN_MAP,
        LATIN_SYMBOLS_MAP,
        GREEK_MAP,
        TURKISH_MAP,
        ROMANIAN_MAP,
        RUSSIAN_MAP,
        UKRAINIAN_MAP,
        CZECH_MAP,
        SLOVAK_MAP,
        POLISH_MAP,
        LATVIAN_MAP,
        ARABIC_MAP,
        LITHUANIAN_MAP,
        SERBIAN_MAP,
        AZERBAIJANI_MAP,
        GEORGIAN_MAP
    ];

    const Downcoder = {
        'Initialize': function() {
            if (Downcoder.map) { // already made
                return;
            }
            Downcoder.map = {};
            for (const lookup of ALL_DOWNCODE_MAPS) {
                Object.assign(Downcoder.map, lookup);
            }
            Downcoder.regex = new RegExp(Object.keys(Downcoder.map).join('|'), 'g');
        }
    };

    function downcode(slug) {
        Downcoder.Initialize();
        return slug.replace(Downcoder.regex, function(m) {
            return Downcoder.map[m];
        });
    }


    function URLify(s, num_chars, allowUnicode) {
        // changes, e.g., "Petty theft" to "petty-theft"
        if (!allowUnicode) {
            s = downcode(s);
        }
        s = s.toLowerCase(); // convert to lowercase
        // if downcode doesn't hit, the char will be stripped here
        if (allowUnicode) {
            // Keep Unicode letters including both lowercase and uppercase
            // characters, whitespace, and dash; remove other characters.
            s = XRegExp.replace(s, XRegExp('[^-_\\p{L}\\p{N}\\s]', 'g'), '');
        } else {
            s = s.replace(/[^-\w\s]/g, ''); // remove unneeded chars
        }
        s = s.replace(/^\s+|\s+$/g, ''); // trim leading/trailing spaces
        s = s.replace(/[-\s]+/g, '-'); // convert spaces to hyphens
        s = s.substring(0, num_chars); // trim to first num_chars chars
        return s.replace(/-+$/g, ''); // trim any trailing hyphens
    }
    window.URLify = URLify;
}