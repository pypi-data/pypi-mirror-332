//
//  IMPORTANT: READ BEFORE DOWNLOADING, COPYING, INSTALLING OR USING.
//
//  By downloading, copying, installing or using the software you agree to this license.
//  If you do not agree to this license, do not download, install,
//  copy or use the software.
//
//
//                               License Agreement
//                               FlashBertTokenizer
//
//               Copyright (C) 2025, Kim Bomm, all rights reserved.
//
// Third party copyrights are property of their respective owners.
//
// Redistribution and use in source and binary forms, with or without modification,
// are permitted provided that the following conditions are met:
//
//   * Redistribution's of source code must retain the above copyright notice,
//     this list of conditions and the following disclaimer.
//
//   * Redistribution's in binary form must reproduce the above copyright notice,
//     this list of conditions and the following disclaimer in the documentation
//     and/or other materials provided with the distribution.
//
//   * The name of the copyright holders may not be used to endorse or promote products
//     derived from this software without specific prior written permission.
//
// This software is provided by the copyright holders and contributors "as is" and
// any express or implied warranties, including, but not limited to, the implied
// warranties of merchantability and fitness for a particular purpose are disclaimed.
// loss of use, data, or profits; or business interruption) however caused
// and on any theory of liability, whether in contract, strict liability,
// or tort (including negligence or otherwise) arising in any way out of
// the use of this software, even if advised of the possibility of such damage.
//
#include "bert_tokenizer.h"

std::vector<int> convert_by_vocab(const Vocab &vocab, const std::deque<std::string> &items, int max_length = -1) {
    std::vector<int> ids;
    ids.resize(items.size());

    auto dst = ids.begin();
    for (const auto &item: items) {
        auto it = vocab.token_to_index.find(item);
        *dst++ = (it != vocab.token_to_index.end()) ? it->second : -1;
    }

    if (max_length > static_cast<int>(ids.size())) {
        ids.resize(max_length, 0);
    }

    return ids;
}

std::deque<std::string> whitespace_tokenize(const std::string &text) {
    std::deque<std::string> tokens;

    const char *src = text.data();
    const char *end = src + text.size();

    while (src < end) {
        while (src < end && std::isspace(static_cast<unsigned char>(*src))) src++;
        if (src >= end) break;

        const char *token_start = src;
        while (src < end && !std::isspace(static_cast<unsigned char>(*src))) src++;

        tokens.emplace_back(token_start, src - token_start);
    }

    return tokens;
}


std::string to_lower(const std::string &text) {
    std::string res(text.size(), '\0');

    const char *src = text.data();
    char *dst = &res[0];
    const char *end = src + text.size();

    while (src < end) {
        unsigned char c = static_cast<unsigned char>(*src);

        if (c < 0x80) {
            *dst++ = ('A' <= c && c <= 'Z') ? (c | 0x20) : c;
            src++;
        } else {
            int len = 0;
            if ((c >> 5) == 0x6) len = 2;
            else if ((c >> 4) == 0xE) len = 3;
            else if ((c >> 3) == 0x1E) len = 4;
            else {
                src++;
                continue;
            }

            if (src + len > end) break;

            memcpy(dst, src, len);
            src += len;
            dst += len;
        }
    }

    res.resize(dst - &res[0]);
    return res;
}


std::string clean_text(const std::string &text) {
    std::string res(text.size(), '\0');

    const char *src = text.data();
    char *dst = &res[0];
    const char *end = src + text.size();

    while (src < end) {
        unsigned char c = static_cast<unsigned char>(*src);

        if (c == 0) {
            src++;
            continue;
        }

        if (c < 0x80) {
            *dst++ = std::isspace(c) ? ' ' : c;
            src++;
        } else {
            int len = 0;
            if ((c >> 5) == 0x6) len = 2;
            else if ((c >> 4) == 0xE) len = 3;
            else if ((c >> 3) == 0x1E) len = 4;
            else {
                src++;
                continue;
            }

            if (src + len > end) break;

            memcpy(dst, src, len);
            src += len;
            dst += len;
        }
    }

    res.resize(dst - &res[0]);
    return res;
}

std::deque<std::string> split_on_punc(const std::string &text) {
    std::deque<std::string> tokens;

    const char *src = text.data();
    const char *end = src + text.size();
    const char *token_start = nullptr;

    while (src < end) {
        unsigned char c = static_cast<unsigned char>(*src);

        if (c < 0x80) {
            if (std::ispunct(c) || std::isspace(c)) {
                if (token_start) {
                    tokens.emplace_back(token_start, src - token_start);
                    token_start = nullptr;
                }
                if (std::ispunct(c)) {
                    tokens.emplace_back(1, c);
                }
                src++;
            } else {
                if (!token_start) token_start = src;
                src++;
            }
        } else {
            int len = 0;
            if ((c >> 5) == 0x6) len = 2;
            else if ((c >> 4) == 0xE) len = 3;
            else if ((c >> 3) == 0x1E) len = 4;
            else {
                src++;
                continue;
            }

            if (src + len > end) break;

            if (!token_start) token_start = src;
            src += len;
        }
    }

    if (token_start && token_start < src)
        tokens.emplace_back(token_start, src - token_start);

    return tokens;
}

std::string BasicTokenizer::tokenize_chinese_chars(const std::string &text) {
    std::string output;
    output.reserve(text.size() * 2);

    const char *src = text.data();
    const char *end = src + text.size();

    while (src < end) {
        uint32_t cp = 0;
        int len = 0;
        unsigned char c = static_cast<unsigned char>(*src);

        if (c < 0x80) {
            cp = c;
            len = 1;
        } else if ((c >> 5) == 0x6 && src + 1 < end) {
            cp = ((c & 0x1F) << 6) | (src[1] & 0x3F);
            len = 2;
        } else if ((c >> 4) == 0xE && src + 2 < end) {
            cp = ((c & 0x0F) << 12) |
                 ((static_cast<unsigned char>(src[1]) & 0x3F) << 6) |
                 (static_cast<unsigned char>(src[2]) & 0x3F);
            len = 3;
        } else if ((c >> 3) == 0x1E && src + 3 < end) {
            cp = ((c & 0x07) << 18) |
                 ((static_cast<unsigned char>(src[1]) & 0x3F) << 12) |
                 ((static_cast<unsigned char>(src[2]) & 0x3F) << 6) |
                 (static_cast<unsigned char>(src[3]) & 0x3F);
            len = 4;
        } else {
            src++;
            continue;
        }

        if (is_chinese_char(cp)) {
            output.push_back(' ');
            output.append(src, len);
            output.push_back(' ');
        } else {
            output.append(src, len);
        }

        src += len;
    }

    return output;
}