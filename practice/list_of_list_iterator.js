
exports.lol = function(list, fn) {
    var i, j, sub;

    for (i=0; i < list.length; i++) {
        sub = list[i];
        if (!sub || !sub.length) continue;

        for(j=0; j < sub.length; j++) {
            fn(sub[j]);
        }
    }
}

console.log('hello world!');
exports.lol([[1,2,3],[],[],[4,5,6,7],[8,9,10]],
    function(item) { console.log(item) });
