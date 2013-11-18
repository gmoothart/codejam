
// creates a hash that automatically evicts
// stale items to keep it within a specific
// size
exports.create = function(size) {
    var cache = {},
        queue = [];
        max_size = size;

    return {
        add: function(key, val) {
            var v = { val: val, on: new Date() },
                d;
            cache[key] = v;

            // no. Need to be able to update this easily.
            queue.push({key: key, v: v});

            while (queue.length > max_size) {
                d = queue.shift();
                delete cache[d.key];
            }
        },
        get: function(key) {
            if (key in cache) {
                // update val in queue
                return cache[key].val;
            }
        },
        debug: function() {
            return {
                q: queue,
                c: cache,
            }
        }
    };
}
