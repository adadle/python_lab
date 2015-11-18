#coding=utf-8
class Members:
    def __init__(self, name):
        self.name = name
        print "I'm member of com,name: %s" % self.name

    def skill(self):
        print "%s's skill" % self.name
#pm
class Pm(Members):
    def __init__(self, name, work):
        Members.__init__(self, name)
        self.work = work
        print "skill: %s" % self.work
    
    def skill(self):
        Members.skill(self)
        print "--------"
        print "pm can %s" % self.work
                
#tech
class Tech(Members):
    def __init__(self, name, work):
        Members.__init__(self, name)
        self.work = work
        print "tech: %s" % self.name
    def skill(self):
        print 'tech can %s' % self.work
            


if __name__ == '__main__':
    pm = Pm('pm','design product')
    tech = Tech('tech','coding')
    members = [pm,tech]
    for m in members:
        m.skill() 



