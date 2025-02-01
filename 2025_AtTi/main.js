class LunarYear{
    constructor(yearnum, yearname){
        this.yearnum = yearnum
        this.yearname = yearname
    }

    NewYear(){
        console.log("Chuc mung nam moi!")
        console.log(this.yearname)
        console.log(this.yearnum)
        console.log("!")
    }
}

const AtTy = new LunarYear(2025, "AtTy")
AtTy.NewYear()