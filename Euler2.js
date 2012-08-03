var fibgen = {
    a: 1,
    b: 1,
    next: function() {
        var temp;
        temp = this.a;
        this.a = this.b;
        this.b = this.a + temp;

        return this.a;
    }
}

function solve(upto) {
    var fibs = [];
    var tempfib = fibgen.next();
    while(tempfib < upto) {
        fibs.push(tempfib);
        tempfib = fibgen.next();
    }

    var evenfibs = fibs.filter(function(x){return x % 2 === 0});

    return evenfibs.reduce(function(x, y){return x + y});
}

console.log(solve(4000000));
