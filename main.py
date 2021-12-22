from bc import TicToc, FindPi
from threading import Thread
import os

if __name__ == "__main__":  # burası direkt olark dosyayı run yaptığında çalışıyor
    tt = TicToc()
    tt.tic()
    n = 1000000
    # finding_pi.throw_points(10000) bu nun yerine alttaki threadi kullanıcaz
    # GIL : Global interpreted lock
    find_pis = []
    threads = []
    for i in range(os.cpu_count()):
        find_pis.append(FindPi())
        threads.append(Thread(target=find_pis[i].throw_points, args=(n,)))
        print("Started thread number %d" % i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    inner = 0
    total = 0
    for find_pi in find_pis:
        inner += find_pi.i
        total += find_pi.n

    pi = 4 * inner / total
    print("PI = %.8f | N = %d / %d | TIME = %.5f seconds" %
          (pi, inner, total, tt.toc()))