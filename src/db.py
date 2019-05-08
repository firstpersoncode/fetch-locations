import pymysql, json

def readFileJSON(fileName):
    with open(fileName) as json_file:
        data = json.load(json_file)

    res = [p for p in data]

    return res

class Locations:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "password"
        db = "rusaha-locations"
        self.con = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    db=db,
                                    cursorclass=pymysql.cursors.DictCursor)

        self.cur = self.con.cursor()

    def set(self, table):
        file = "src/data/{table}.json".format(table=table)
        dataJSON = readFileJSON(file)

        try:
            drop_table = "DROP TABLE IF EXISTS `{table}`".format(table=table)
            self.cur.execute(drop_table)
            create_table = "CREATE TABLE IF NOT EXISTS `{table}` ({id}, {lid}, {name}, {pk})".format(
                table=table,
                id="`id` INT NOT NULL AUTO_INCREMENT",
                lid="`lid` VARCHAR(255) NOT NULL",
                name="`name` VARCHAR(255) NOT NULL",
                pk="PRIMARY KEY (`id`)"
            )

            self.cur.execute(create_table)

            for item in dataJSON:

                insert = "INSERT INTO `{table}` (`lid`, `name`) VALUES ({lid}, \"{name}\")".format(
                    table=table,
                    lid=item.get("id"),
                    name=item.get("name")
                )

                print(insert, "\n===============================================================")

                self.cur.execute(insert)

            self.con.commit()
        except Exception as e:
            print(e)
            self.con.close()
            return False

        self.con.close()
        return True

    def get(self, table, limit, page):
        offset = (page - 1) * limit
        sql = "SELECT lid, name FROM `{table}` LIMIT {offset}, {limit}".format(
            table=table,
            offset=str(offset),
            limit=str(limit)
        )
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def getAll(self, limit, page):
        offset = (page - 1) * limit
        sql = "{provinsi} {kabupaten} {kecamatan} {kelurahan} {orderBy} {limitBy}".format(
            provinsi="SELECT lid, name FROM `provinsi` UNION ALL",
            kabupaten="SELECT lid, name FROM `kabupaten` UNION ALL",
            kecamatan="SELECT lid, name FROM `kecamatan` UNION ALL",
            kelurahan="SELECT lid, name FROM `kelurahan`",
            orderBy="ORDER BY CAST(lid AS UNSIGNED) ASC",
            limitBy="LIMIT {offset}, {limit}".format(offset=offset, limit=limit)
        )
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
