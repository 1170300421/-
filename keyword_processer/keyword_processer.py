import sys

import pymysql


class KeywordProcesser(object):
    def __init__(self, keywords=None, ignore_space=False):
        self.keyword_trie_dict = dict()
        self.keyword_count = 0
        self._keyword_flag = '_type_'

        self._ignore_space = ignore_space

        if isinstance(keywords, str):
            self.add_keyword_from_file(keywords)
        elif isinstance(keywords, list):
            self.add_keyword_from_list(keywords)
        elif isinstance(keywords, dict):
            self.add_keyword_from_dict(keywords)
        else:
            pass

    def add_keyword(self, keyword, keyword_type=None):
        if not keyword_type:
            keyword_type = keyword
        current_dict = self.keyword_trie_dict
        for char in keyword:
            current_dict = current_dict.setdefault(char, {})
        if self._keyword_flag not in current_dict:
            self.keyword_count += 1
            current_dict[self._keyword_flag] = keyword_type

    def add_keyword_from_list(self, keyword_list):
        keyword_list = keyword_list.split(' ')
        for keyword in keyword_list:
            self.add_keyword(keyword)

    def add_keyword_from_dict(self, keyword_dict):
        for keyword in keyword_dict:
            self.add_keyword(keyword, keyword_dict[keyword])

    def add_keyword_from_file(self, path, split='\t'):
        import codecs
        file_r = codecs.open(path, 'r', encoding='utf-8')
        line = file_r.readline()
        while line:
            line = line.strip()
            if not line:
                line = file_r.readline()
                continue
            items = line.split(split)
            if len(items) == 1:
                self.add_keyword(items[0])
            else:
                self.add_keyword(items[0], items[1])
            line = file_r.readline()
        file_r.close()

    def delete_keyword(self, keyword):
        current_dict = self.keyword_trie_dict
        level_node_list = []
        for char in keyword:
            if char not in current_dict:
                return False
            level_node_list.append((char, current_dict))
            current_dict = current_dict[char]

        if self._keyword_flag not in current_dict:
            return False

        level_node_list.append((self._keyword_flag, current_dict))
        for char, level_dict in level_node_list[::-1]:
            if len(level_dict) == 1:
                level_dict.pop(char)
            else:
                level_dict.pop(char)
                break
        self.keyword_count -= 1
        return True

    def delete_keyword_from_list(self, keyword_list):
        for keyword in keyword_list:
            self.delete_keyword(keyword)

    def _match_text(self, text, start, end):
        current_dict = self.keyword_trie_dict
        index, entity_type = -1, ''

        for i in range(start, end):
            if text[i] == ' ' and self._ignore_space:
                continue
            if text[i] not in current_dict:
                if index == -1:
                    return start + 1, 0, ''
                else:
                    return index + 1, index + 1 - start, entity_type
            current_dict = current_dict[text[i]]
            if self._keyword_flag in current_dict:
                index = i
                entity_type = current_dict[self._keyword_flag]
        if index != -1:
            return index + 1, index + 1 - start, entity_type
        return start + 1, 0, ''

    def extract_keywords(self, text):
        keywords = []

        end, text_len = 0, len(text)
        while end < text_len:
            end, entity_len, entity_type = self._match_text(text, end, text_len)
            if entity_type:
                keywords.append([end - entity_len, end, entity_type])
        return keywords

    def extract_keywords_from_list(self, words):
        keywords = []
        for i, word in enumerate(words):
            if self.contain_keyword(word):
                keywords.append([word, i])
        return keywords

    def extract_keywords_from_list_yield(self, words):
        for i, word in enumerate(words):
            if self.contain_keyword(word):
                yield [word, i]

    def extract_keywords_yield(self, text):
        end, text_len = 0, len(text)
        while end < text_len:
            end, entity_len, entity_type = self._match_text(text, end, text_len)
            if entity_type:
                yield [end - entity_len, end, entity_type]

    def get_keyword_type(self, keyword):
        current_dict = self.keyword_trie_dict
        for char in keyword:
            if char not in current_dict:
                return None
            current_dict = current_dict[char]
        if self._keyword_flag not in current_dict:
            return None
        return current_dict[self._keyword_flag]

    def contain_keyword(self, keyword):
        current_dict = self.keyword_trie_dict
        for char in keyword:
            if char not in current_dict:
                return False
            current_dict = current_dict[char]
        if self._keyword_flag not in current_dict:
            return False
        return True

    def get_keywords(self, keyword_part='', current_dict=None):
        keywords = dict()
        if current_dict is None:
            current_dict = self.keyword_trie_dict
        for char in current_dict:
            if char == self._keyword_flag:
                keywords[keyword_part] = current_dict[self._keyword_flag]
            else:
                keywords_ = self.get_keywords(keyword_part + char, current_dict[char])
                keywords.update(keywords_)
        return keywords


if __name__ == '__main__':
    keyword = sys.stdin.readline().strip()
    #keyword="肖战"
    keyword_processor = KeywordProcesser()
    keyword_processor.add_keyword_from_list(keyword)
    print(keyword_processor.keyword_count)
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="124088he",
        database="weibo1",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "select * from microblog_hotspot"
    cursor.execute(sql)
    data = cursor.fetchall()
    sql1 = "delete from microblog_controlledhotspot where id < 10000"
    cursor.execute(sql1)
    conn.commit()
    for i in data:
        if keyword_processor.extract_keywords(i[1]):
            sql2 = 'insert into microblog_controlledhotspot(id, content, author, publishTime, repost, comment, ' \
                  'approve, address) values (%s, %s, %s, %s, %s, %s, %s, %s)'
            print(i)
            cursor.executemany(sql2, [i])
            conn.commit()
    cursor.close()
    conn.close()
