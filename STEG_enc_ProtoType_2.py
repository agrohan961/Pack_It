import cv2, numpy

def hextobin(num):
    return "".join(['{:04b}'.format(int(x,16)) for x in num])

def img_size(img):
    l, b = len(img), len(img[0])

    temp = numpy.ndarray((l*2, b*2, 3))

    for i in range(l):
        for j in range(b):
            x = i*2
            y = j*2
            temp[x][y] = temp[x + 1][y] = temp[x][y + 1] = temp[x + 1][y + 1] = img[i][j]
    return temp

"""def delimiter(img, text):
    length = len(text)
    if(len(img) > len(img[0])):
        while(length > (len(img) * (len(img[0]) - 1) * 3)):
            img = img_size(img)
        binlen = ('{:0'+str(len(img)*3)+'b}').format(length)
        for i in range(len(img[0])):
            for j in range(3):
                img[-1][i][j] = int((('{:0b}'.format(int(img[-1][i][j])))[:-1]+binlen[0]),2)
                binlen = binlen[1:]
                
    else:
        while(length > ((len(img) - 1) * len(img[0]) * 3)):
            img = img_size(img)
        binlen = ('{:0'+str(len(img[0]*3))+'b}').format(length)
        for i in range(len(img)):
            for j in range(3):
                img[i][-1][j] = int((('{:0b}'.format(int(img[i][-1][j])))[:-1]+binlen[0]),2)
                binlen = binlen[1:]
    return img"""

def steg(img, text):
    length = len(text)
    while(length > (len(img) * len(img[0]) * 3)):
        img = img_size(img)

    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                img[i][j][k] = int((('{:0b}'.format(int(img[i][j][k])))[:-1]+text[0]),2)
                text = text[1:]
                if(len(text) == 0):
                    return img
    
text = "c22d089738d91100d16aaf8c4a8b5dd1dd078e11d2933ad8b198e63fc2a552b204af11b5992ea76571aa5b7455397b8ec58adee3110f6160cc40f79c2f9bee43fa6c0399e047ad4a420e764e2007128477be819be713c42c3cfb8d37e5b548fec00e5bf4f6c67b71eed35e61534b8f1cb6726f778d7f7d8f641904aaaa892e366f3d5a753a9e05f63f8f73f4f254c986a8ad6d3682f5384e857916a85aeec9e6fa9ba238f9c3803f95cdbf86b379a78071aba81bb9213735dcba8614d81e69038b37200d71772cf71bbaa6a9439024bffd94fcc069a1fecddbfea9fa851fcbc924907d7d2e3406f20761736c9cb04f519462b69612a84a76342ad8e2882a300c6338d83b8477466d88077fd3a7d60d27e393f328b48a45087a9b3e762703eac30435f5e6280755e1277f4c8356230d1451b44f553fcd26cdb5f93b55a59b7cec51e9bb708b2e9efe945949f6fecf613ad3c5e4d153528edbdb5ed233e76fc0899bfa61d757ba5540e41617da7c4f6e1f95cdbf86b379a7802fd864d0c762e96c433e6e597499d43f17ad3ae1a10b8e73c1ce12c12559a8272c73957bd2897f739bfa61d757ba5540cdeb1a5dbbf4489ec07ca5861ec10304b28180a22a5286dacd34d8be8a8bc06874a3638382f270b8bbe0e9f7f29fe9f3ecd2f2a3f2eab81b1e58e24e7491aa0b7b2d3a8d751b4c3edb7ee4bad1fdbfdbbb94b5aa64f57c23464b7149700c9abb862fcdc448800a6babc9d42692475f498643ac8a49de1912a01e44c17d268f4b3254db30ecf12f50a2394a182103f4ee070f3935d327bb1257907536cd4785a37e526e67b5ef3db68f2767cd916244264f5ead39a84efc51945949f6fecf613a26906eee214323021a26363de0869603e391f0e2927b43217165f7cb21356ebb419b77c14876245a35bb299fbadca2ef418b95fdf00eb7c2cd96a6415a3b2e47df312808b894af4fef938ef3f54381dd450243315d3f54198afe2e0b37ea825e95cdbf86b379a7803151afe8b5780f5411922270fcd2574273c1ad007c72be9ebb5338d54f25d8027c2a8d5833dfae95403c403de40d702a0bb6aa7a7e57838f6554d432fad54e8317e53574b70db45988077fd3a7d60d276de578811926ee7c945949f6fecf613ad3c5e4d153528edbdb5ed233e76fc0899bfa61d757ba5540edf5b7b6d4992f7995cdbf86b379a7800935bc61cdf3906d1d921f779c61a432e84d094fab603e56d624b68201af56c20c013ed0e05698d61e82c01ff64f3c508d34e986874dcbfa62e5fb640a82ca6a251ff222677783f7e014cdc47d4aaa2da26d2ed77c6012944691e431b0e3a1fc3e0845eb755539b475d3d7729d6b45468d1a8b93920e711a92288396025d4f8f76818c418d0d1ee3d99c6292b8c6b5bfc58adee3110f61605c15dbaccf29473bddbaed204fe7c13cf511f8926531d8b3758001436c1f91c3abf295907796414a2e3681887a0b46605e5d0af5fe58446fdab8647053b9faaa91778bd457c2d51a9229568e1c1e2aefe4d5baa1d2ee2a287a0ccfed935666e125ac45acf9f1176c6a4a688a699eecd919c4c7e12fce4e3816738f67a006105fab979e44af00569b3427ceed33750103945949f6fecf613a1101aa38eec278e79e8decda0861bdb5a259f3d2e6a223561fb4dc2e6df08accb5e98c8a1721f81ae393f328b48a45080bc7f7897b7051289e03326d7823586cb8f6577b7f3785e71f1ead1ca001764cfa39dca1d240489b0bb6aa7a7e57838f6554d432fad54e8317e53574b70db45988077fd3a7d60d27d87f8fc570ee3d685434e0bb4d05f02b3818b784d9deb10f5c76e97171620cd7647bd8dfb5e193e789fd509e1426f641ad8d5abbe5796323cf78833b04a263d744448c0c0d7de0087b6e503254059f62a2394a182103f4ee6291e8012befe334319c50ce9123e8f9912e8979212b632b4efe5fab06d480a4a3ee6b4dfc0115693f308250fc3f6265439a2dd66010213edd1eb9412aad6b02a1111fde018135b27b2d3a8d751b4c3ec968d386524edaab76d53c3ddd49c0ce3f7ac2da12c400ff66acd37302ae6f3d0678fbdc1d333d189b5e411f40d6e1781cac5cacb8483b2d747128f1c9f96225128d0f0f0ff25dd21a88429331d541378d04200973c5a582a2394a182103f4ee6c342df1ea66134dd3fe0c0a5543381af19fea3d071ec746a12b875984d77de49bfa61d757ba5540c557ccdf8f80a40bf7ef2d4b85940b975708f7289d46f64a6db48e2ced30fb2d633ec42887934f9b73c91f3454b5e8e91397a6d4eb35089695cdbf86b379a7802fd864d0c762e96c433e6e597499d43f17ad3ae1a10b8e73127eaa0bdb3b3ca82c73957bd2897f730bc7f7897b7051289e03326d7823586cb8f6577b7f3785e76b3b587c7a0cf525fa39dca1d240489bd937801c4057aff03872f79ddd3f9456ff8033d413e041dfa9e065fb3c4cf5bdd16aaf8c4a8b5dd1dd078e11d2933ad8b198e63fc2a552b204af11b5992ea76571aa5b7455397b8ec58adee3110f6160cc40f79c2f9bee43fa6c0399e047ad4a420e764e2007128477be819be713c42c3cfb8d37e5b548fec00e5bf4f6c67b71eed35e61534b8f1cb6726f778d7f7d8f641904aaaa892e366f3d5a753a9e05f63f8f73f4f254c986a8ad6d3682f5384e857916a85aeec9e6fa9ba238f9c3803f95cdbf86b379a78071aba81bb9213735dcba8614d81e69038b37200d71772cf71bbaa6a9439024bffd94fcc069a1fecddbfea9fa851fcbc924907d7d2e3406f20761736c9cb04f519462b69612a84a76342ad8e2882a300c6338d83b8477466d88077fd3a7d60d27e393f328b48a45087a9b3e762703eac30435f5e6280755e1277f4c8356230d1451b44f553fcd26cdb5f93b55a59b7cec51e9bb708b2e9efe945949f6fecf613ad3c5e4d153528edbdb5ed233e76fc0899bfa61d757ba5540e41617da7c4f6e1f95cdbf86b379a7802fd864d0c762e96c433e6e597499d43f17ad3ae1a10b8e73c1ce12c12559a8272c73957bd2897f739bfa61d757ba5540cdeb1a5dbbf4489ec07ca5861ec10304b28180a22a5286dacd34d8be8a8bc06874a3638382f270b8bbe0e9f7f29fe9f3ecd2f2a3f2eab81b1e58e24e7491aa0b7b2d3a8d751b4c3edb7ee4bad1fdbfdbbb94b5aa64f57c23464b7149700c9abb862fcdc448800a6babc9d42692475f498643ac8a49de1912a01e44c17d268f4b3254db30ecf12f50a2394a182103f4ee070f3935d327bb1257907536cd4785a37e526e67b5ef3db68f2767cd916244264f5ead39a84efc51945949f6fecf613a26906eee214323021a26363de0869603e391f0e2927b43217165f7cb21356ebb419b77c14876245a35bb299fbadca2ef418b95fdf00eb7c2cd96a6415a3b2e47df312808b894af4fef938ef3f54381dd450243315d3f54198afe2e0b37ea825e95cdbf86b379a7803151afe8b5780f5411922270fcd2574273c1ad007c72be9ebb5338d54f25d8027c2a8d5833dfae95403c403de40d702a0bb6aa7a7e57838f6554d432fad54e8317e53574b70db45988077fd3a7d60d276de578811926ee7c945949f6fecf613ad3c5e4d153528edbdb5ed233e76fc0899bfa61d757ba5540edf5b7b6d4992f7995cdbf86b379a7800935bc61cdf3906d1d921f779c61a432e84d094fab603e56d624b68201af56c20c013ed0e05698d61e82c01ff64f3c508d34e986874dcbfa62e5fb640a82ca6a251ff222677783f7e014cdc47d4aaa2da26d2ed77c6012944691e431b0e3a1fc3e0845eb755539b475d3d7729d6b45468d1a8b93920e711a92288396025d4f8f76818c418d0d1ee3d99c6292b8c6b5bfc58adee3110f61605c15dbaccf29473bddbaed204fe7c13cf511f8926531d8b3758001436c1f91c3abf295907796414a2e3681887a0b46605e5d0af5fe58446fdab8647053b9faaa91778bd457c2d51a9229568e1c1e2aefe4d5baa1d2ee2a287a0ccfed935666e125ac45acf9f1176c6a4a688a699eecd919c4c7e12fce4e3816738f67a006105fab979e44af00569b3427ceed33750103945949f6fecf613a1101aa38eec278e79e8decda0861bdb5a259f3d2e6a223561fb4dc2e6df08accb5e98c8a1721f81ae393f328b48a45080bc7f7897b7051289e03326d7823586cb8f6577b7f3785e71f1ead1ca001764cfa39dca1d240489b0bb6aa7a7e57838f6554d432fad54e8317e53574b70db45988077fd3a7d60d27d87f8fc570ee3d685434e0bb4d05f02b3818b784d9deb10f5c76e97171620cd7647bd8dfb5e193e789fd509e1426f641ad8d5abbe5796323cf78833b04a263d744448c0c0d7de0087b6e503254059f62a2394a182103f4ee6291e8012befe334319c50ce9123e8f9912e8979212b632b4efe5fab06d480a4a3ee6b4dfc0115693f308250fc3f6265439a2dd66010213edd1eb9412aad6b02a1111fde018135b27b2d3a8d751b4c3ec968d386524edaab76d53c3ddd49c0ce3f7ac2da12c400ff66acd37302ae6f3d0678fbdc1d333d189b5e411f40d6e1781cac5cacb8483b2d747128f1c9f96225128d0f0f0ff25dd21a88429331d541378d04200973c5a582a2394a182103f4ee6c342df1ea66134dd3fe0c0a5543381af19fea3d071ec746a12b875984d77de49bfa61d757ba5540c557ccdf8f80a40bf7ef2d4b85940b975708f7289d46f64a6db48e2ced30fb2d633ec42887934f9b73c91f3454b5e8e91397a6d4eb35089695cdbf86b379a7802fd864d0c762e96c433e6e597499d43f17ad3ae1a10b8e73127eaa0bdb3b3ca82c73957bd2897f730bc7f7897b7051289e03326d7823586cb8f6577b7f3785e76b3b587c7a0cf525fa39dca1d240489bd937801c4057aff03872f79ddd3f9456ff8033d413e041dfa9e065fb3c4cf5bdd16aaf8c4a8b5dd1dd078e11d2933ad8b198e63fc2a552b204af11b5992ea76571aa5b7455397b8ec58adee3110f6160cc40f79c2f9bee43fa6c0399e047ad4a420e764e2007128477be819be713c42c3cfb8d37e5b548fec00e5bf4f6c67b71eed35e61534b8f1cb6726f778d7f7d8f641904aaaa892e366f3d5a753a9e05f63f8f73f4f254c986a8ad6d3682f5384e857916a85aeec9e6fa9ba238f9c3803f95cdbf86b379a78071aba81bb9213735dcba8614d81e69038b37200d71772cf71bbaa6a9439024bffd94fcc069a1fecddbfea9fa851fcbc924907d7d2e3406f20761736c9cb04f519462b69612a84a76342ad8e2882a300c6338d83b8477466d88077fd3a7d60d27e393f328b48a45087a9b3e762703eac30435f5e6280755e1277f4c8356230d1451b44f553fcd26cdb5f93b55a59b7cec51e9bb708b2e9efe945949f6fecf613ad3c5e4d153528edbdb5ed233e76fc0899bfa61d757ba5540e41617da7c4f6e1f95cdbf86b379a7802fd864d0c762e96c433e6e597499d43f17ad3ae1a10b8e73c1ce12c12559a8272c73957bd2897f739bfa61d757ba5540cdeb1a5dbbf4489ec07ca5861ec10304b28180a22a5286dacd34d8be8a8bc06874a3638382f270b8bbe0e9f7f29fe9f3ecd2f2a3f2eab81b1e58e24e7491aa0b7b2d3a8d751b4c3edb7ee4bad1fdbfdbbb94b5aa64f57c23464b7149700c9abb862fcdc448800a6babc9d42692475f498643ac8a49de1912a01e44c17d268f4b3254db30ecf12f50a2394a182103f4ee070f3935d327bb1257907536cd4785a37e526e67b5ef3db68f2767cd916244264f5ead39a84efc51945949f6fecf613a26906eee214323021a26363de0869603e391f0e2927b43217165f7cb21356ebb419b77c14876245a35bb299fbadca2ef418b95fdf00eb7c2cd96a6415a3b2e47df312808b894af4fef938ef3f54381dd450243315d3f54198afe2e0b37ea825e95cdbf86b379a7803151afe8b5780f5411922270fcd2574273c1ad007c72be9ebb5338d54f25d8027c2a8d5833dfae95403c403de40d702a0bb6aa7a7e57838f6554d432fad54e8317e53574b70db45988077fd3a7d60d276de578811926ee7c945949f6fecf613ad3c5e4d153528edbdb5ed233e76fc0899bfa61d757ba5540edf5b7b6d4992f7995cdbf86b379a7800935bc61cdf3906d1d921f779c61a432e84d094fab603e56fe0547132ef8da6208e9cf43b1bea03c56fe64993c82086ca26d2ed77c601294f9a7561f52fdbceb88077fd3a7d60d27277086c76845441a945949f6fecf613aad8d5abbe57963238f029a8a4c4944b8b44c10afafba44a0962eecf99f97fecf4df5bf5244934b78556a2d6bfd739ed54612192c8b472906de782690bb36162f14076a3513c3d0c457e888d24d96f92a8d68bff241d2d000f72fe5b84530b5b6db5644aa6aa3654d6d9d32c0f519c439c58adee3110f61608c5f10a37d1baf049725b75d31deadc9f9d26141f313de8191690ff03c3816ac099bbe8485ddbd513d445365a46cde2bef84b3be20e277b424c9c8865698db8792b20610e0fa20f7a27eed09638a94b41d463d66ab39d1cbecd2f2a3f2eab81ba2394a182103f4ee91993c8108cb7746c877417465b0aa81a0b167dd46cb50b01c92a761b1325acc0e5bbc0f5a15e3770142314f76ed76da7b2d3a8d751b4c3ef5ccd66983556abdc6932953625e885d04af11b5992ea765afa73788d1df1ad7c58adee3110f616026e444385c4d362d66f82e37f385b82b73e39a42fccfa061f28b51ba9d6d8758a2394a182103f4ee04af11b5992ea765247fbabc5c1d8a7f290247a8f"
text += "00"
text = hextobin(text)
image = steg(cv2.imread("TEST12.png"), text)
cv2.imwrite("TEST1.png", image)