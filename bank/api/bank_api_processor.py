from bank.models import Branches, Banks


class BranchDetails:
    def execute(self, ifsc):
        branch = self._get_branch(ifsc)
        details = BranchDetailer.get_details(branch)
        return details

    def _get_branch(self, ifsc):
        try:
            branch = Branches.objects.get(ifsc=ifsc)
        except Branches.DoesNotExist:
            raise ValueError('Invalid IFSC code')
        return branch


class BranchDetailer:
    @staticmethod
    def get_details(branch):
        details = {
            'ifsc': branch.ifsc,
            'bank': branch.bank.name,
            'branch': branch.branch,
            'address': branch.address,
            'city': branch.city,
            'district': branch.district,
            'state': branch.state
        }
        return details


class BranchFinderInCity:
    def execute(self, name, city):
        banks = self._get_banks(name)
        branches = self._get_branches(banks, city)
        details = self._get_details(branches, name, city)
        return details

    def _get_branches(self, banks, city):
        branches = Branches.objects.filter(bank__in=banks, city__iexact=city)
        return branches

    def _get_banks(self, name):
        try:
            bank = list(Banks.objects.filter(name__icontains=name))
        except Banks.DoesNotExist:
            raise ValueError('No bank exists with such name')
        return bank

    def _get_details(self, branches, name, city):
        if not branches:
            message = 'No branch exists for bank {} in {}'.format(name, city)
            details = {'message': message}
            return details
        branch_details = list(map(BranchDetailer.get_details, branches))
        details = {'branches': branch_details}
        return details
