
# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      61080620973 function calls (60734786498 primitive calls) in 86119.10 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.099 86119.099 {built-in method builtins.exec}
                      1    4.237    4.237 86119.099 86119.099 <string>:1(<module>)
                      1  263.514  263.514 86114.862 86114.862 main.py:80(CFagent)
                2338327 4250.193    0.002 23779.763    0.010 agent.py:212(counterfact)
                7014981   26.578    0.000 21072.268    0.003 agent.py:29(learn)
                7014981  527.632    0.000 17555.599    0.003 learner.py:42(Qlearn)
                2338327   11.463    0.000 16910.703    0.007 game.py:42(step)
                2338327   14.406    0.000 16415.728    0.007 layers.py:827(step)
        382446606/36613822 1501.122    0.000 13814.325    0.000 module.py:866(_call_impl)
               29598841   80.139    0.000 13168.231    0.000 network.py:28(forward)
               29598841  405.279    0.000 12910.725    0.000 container.py:117(forward)
                6615298  141.010    0.000 10038.102    0.002 agent.py:176(choose_action)
                2338328  340.781    0.000 8466.352    0.004 layers.py:793(update)
                2338327  246.371    0.000 8120.722    0.003 agent.py:54(_learn)
               11291908  301.579    0.000 8051.561    0.001 agent.py:49(__call__)
                2338327  200.352    0.000 7917.403    0.003 layers.py:17(step)
              230474843  626.679    0.000 7695.421    0.000 layer.py:106(move)
                2338327  246.478    0.000 7544.155    0.003 agent.py:204(_learn)
                7014981   59.456    0.000 7426.757    0.001 optimizer.py:84(wrapper)
                7014981   28.406    0.000 7139.159    0.001 grad_mode.py:24(decorate_context)
                7014981  204.810    0.000 7045.108    0.001 adam.py:55(step)
                7014981 1440.659    0.000 6609.193    0.001 _functional.py:53(adam)
               83783287 6531.273    0.000 6531.273    0.000 {built-in method tensor}
               78304810   54.394    0.000 6409.285    0.000 game.py:38(board)
                2338327   72.232    0.000 5366.081    0.002 agent.py:117(_learn)
              230474843  703.774    0.000 5169.564    0.000 layers.py:844(check)
                2338327 2727.580    0.001 5043.315    0.002 replaybuffer.py:28(teleporter_save_data)
                8307735   66.351    0.000 4598.882    0.001 layers.py:849(restart)
               59197682  125.267    0.000 4580.680    0.000 conv.py:398(forward)
               59197682   78.511    0.000 4402.549    0.000 conv.py:390(_conv_forward)
                7014981   27.410    0.000 4385.285    0.001 tensor.py:195(backward)
                7014981   25.836    0.000 4356.763    0.001 __init__.py:68(backward)
               59197682 4324.037    0.000 4324.037    0.000 {built-in method conv2d}
                7014981 4174.985    0.001 4174.985    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2338327 2507.140    0.001 4172.600    0.002 agent.py:88(interveen)
                2338327 3389.558    0.001 4157.260    0.002 replaybuffer.py:22(sample_data)
                2338327 3396.569    0.001 4145.085    0.002 replaybuffer.py:67(sample_data)
               56119842 2580.640    0.000 4032.839    0.000 layer.py:159(update)
                8307735   32.831    0.000 3951.502    0.000 level.py:8(__init__)
               84119869  170.602    0.000 3810.624    0.000 linear.py:93(forward)
                8307735  588.583    0.000 3587.155    0.000 levels.py:428(generate)
               84119869   69.304    0.000 3565.502    0.000 functional.py:1737(linear)
               84119869 3479.374    0.000 3479.374    0.000 {built-in method torch._C._nn.linear}
              230474843 1696.816    0.000 2987.595    0.000 layers.py:538(check)
              193212324 2452.100    0.000 2452.100    0.000 {built-in method clone}
               41538675  372.914    0.000 2431.845    0.000 level.py:41(notUsed)
                2338327 1727.591    0.001 2422.981    0.001 replaybuffer.py:73(CF_save_data)
                2338327 1525.712    0.001 2209.203    0.001 agent.py:67(modify)
              113718710   86.672    0.000 2119.923    0.000 activation.py:713(forward)
              113718710   93.396    0.000 2033.251    0.000 functional.py:1364(leaky_relu)
                6615298 1662.742    0.000 1970.385    0.000 agent.py:187(convert_values)
               13630235   90.799    0.000 1960.426    0.000 agent.py:59(modify_board)
              113718710 1919.151    0.000 1919.151    0.000 {built-in method torch._C._nn.leaky_relu}
               37013505 1530.765    0.000 1530.765    0.000 {built-in method cat}
              238028888  167.932    0.000 1510.261    0.000 {built-in method builtins.any}
              230474843  283.978    0.000 1453.333    0.000 layers.py:838(isFree)
              130946312 1359.225    0.000 1359.225    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1611608513  441.895    0.000 1342.962    0.000 layers.py:809(<genexpr>)
             5669589981  912.180    0.000 1317.297    0.000 enum.py:646(__hash__)
               13630235 1248.491    0.000 1248.491    0.000 {built-in method torch._C._nn.one_hot}
              130946312 1189.293    0.000 1189.293    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2338327   43.463    0.000 1184.234    0.001 agent.py:172(__call__)
             1321102932  983.783    0.000 1169.354    0.000 layer.py:103(isFree)
               41538675   32.358    0.000 1131.555    0.000 level.py:38(elementsIn)
                2338327   40.981    0.000 1113.299    0.000 agent.py:112(__call__)
                7014981  162.573    0.000 1026.298    0.000 optimizer.py:189(zero_grad)
             1928308591  835.826    0.000  835.826    0.000 layer.py:154(elements)
               11291908  302.458    0.000  834.444    0.000 exploration.py:53(softmaxer)
              231013908  509.627    0.000  819.130    0.000 layers.py:575(isDead)
               65473156  738.188    0.000  738.188    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               41538675  371.102    0.000  735.883    0.000 level.py:39(<listcomp>)
              230474843  514.740    0.000  719.487    0.000 layers.py:77(check)
               46215329  255.997    0.000  659.724    0.000 random.py:315(sample)
               65473156  640.173    0.000  640.173    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              209180886  632.769    0.000  632.769    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               49965473  623.054    0.000  623.054    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               65473156  617.418    0.000  617.418    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2338327   41.845    0.000  605.456    0.000 replaybuffer.py:18(stacker)
               65473156  604.496    0.000  604.496    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              541477956  453.025    0.000  596.830    0.000 layer.py:134(remove)
             1772214522  593.973    0.000  593.973    0.000 level.py:32(inverse)
                2338327   43.409    0.000  591.118    0.000 replaybuffer.py:63(stacker)
        7592558415/7592558412  502.349    0.000  571.738    0.000 {built-in method builtins.len}
               49846410   56.177    0.000  565.212    0.000 layer.py:77(restart)
              331114095  103.036    0.000  538.033    0.000 random.py:244(randint)
              750281176  350.733    0.000  504.417    0.000 random.py:250(_randbelow_with_getrandbits)
                2338327  288.913    0.000  480.257    0.000 collector.py:46(collect)
               65473156  474.372    0.000  474.372    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              918355646  339.878    0.000  458.632    0.000 layer.py:138(add)
              331114095  182.623    0.000  434.997    0.000 random.py:200(randrange)
             4615758710  409.987    0.000  409.987    0.000 layer.py:99(positions)
             5669616780  405.122    0.000  405.122    0.000 {built-in method builtins.hash}
                8307835  199.272    0.000  395.402    0.000 layers.py:36(reset)
              458312176  305.530    0.000  378.888    0.000 tensor.py:906(grad)
             2143397666  376.092    0.000  376.092    0.000 enum.py:352(<genexpr>)
               41538675  224.972    0.000  363.314    0.000 {built-in method _functools.reduce}
              230474843  242.257    0.000  353.719    0.000 layers.py:48(check)
               59197682   40.480    0.000  344.624    0.000 flatten.py:39(forward)
                7014981    9.343    0.000  340.517    0.000 loss.py:527(forward)
              230474843  118.637    0.000  337.735    0.000 layers.py:572(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624184: <MonsterLevel_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May 10 02:21:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May 10 02:21:52 2021
Terminated at Tue May 11 02:17:23 2021
Results reported at Tue May 11 02:17:23 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85900.54 sec.
    Max Memory :                                 7860 MB
    Average Memory :                             5672.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8524.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86132 sec.
    Turnaround time :                            175686 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 85, in CFagent
    CFagent = CFAgent(env, **defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 171, in __init__
    if a != b:
NameError: name 'a' is not defined


# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      247836 function calls (247547 primitive calls) in 8.00 seconds

##    Ordered by: cumulative time
   List reduced from 208 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    7.999    7.999 {built-in method builtins.exec}
                      1    0.000    0.000    7.998    7.998 <string>:1(<module>)
                      1    0.000    0.000    7.998    7.998 main.py:80(CFagent)
                      3    0.000    0.000    7.884    2.628 agent.py:16(__init__)
                      3    0.000    0.000    7.884    2.628 network.py:37(__init__)
                      1    0.000    0.000    7.867    7.867 agent.py:109(__init__)
                      9    0.000    0.000    7.833    0.870 module.py:573(to)
                  111/9    0.001    0.000    7.833    0.870 module.py:385(_apply)
                     84    0.000    0.000    7.831    0.093 module.py:667(convert)
                     84    7.828    0.093    7.831    0.093 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.110    0.110 game.py:9(__init__)
                      1    0.000    0.000    0.092    0.092 layers.py:793(update)
                    100    0.001    0.000    0.086    0.001 layers.py:849(restart)
                    100    0.000    0.000    0.077    0.001 level.py:8(__init__)
                    100    0.008    0.000    0.073    0.001 levels.py:428(generate)
                    500    0.005    0.000    0.057    0.000 level.py:41(notUsed)
                      9    0.000    0.000    0.051    0.006 network.py:17(__init__)
                     18    0.000    0.000    0.039    0.002 conv.py:370(__init__)
                     18    0.008    0.000    0.039    0.002 conv.py:66(__init__)
                     42    0.000    0.000    0.034    0.001 init.py:347(kaiming_uniform_)
                  21264    0.033    0.000    0.033    0.000 level.py:32(inverse)
                     84    0.032    0.000    0.032    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     18    0.000    0.000    0.029    0.002 conv.py:114(reset_parameters)
                    500    0.000    0.000    0.015    0.000 level.py:38(elementsIn)
                    200    0.006    0.000    0.012    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.012    0.012 layers.py:751(__init__)
                      5    0.000    0.000    0.011    0.002 layers.py:782(add)
                    500    0.005    0.000    0.010    0.000 level.py:39(<listcomp>)
                  39207    0.006    0.000    0.009    0.000 enum.py:646(__hash__)
                      1    0.000    0.000    0.009    0.009 agent.py:39(__init__)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                      6    0.001    0.000    0.009    0.001 layer.py:61(__init__)
                    600    0.001    0.000    0.008    0.000 layer.py:77(restart)
                     24    0.000    0.000    0.008    0.000 linear.py:75(__init__)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                  27836    0.006    0.000    0.006    0.000 enum.py:352(<genexpr>)
                      6    0.004    0.001    0.005    0.001 layer.py:159(update)
                    500    0.003    0.000    0.005    0.000 {built-in method _functools.reduce}
                    500    0.002    0.000    0.005    0.000 random.py:315(sample)
                   1698    0.003    0.000    0.005    0.000 module.py:950(__setattr__)
                      1    0.000    0.000    0.005    0.005 game.py:30(<setcomp>)
                   8012    0.003    0.000    0.004    0.000 layer.py:138(add)
                     41    0.002    0.000    0.004    0.000 game.py:30(<listcomp>)
                    114    0.001    0.000    0.004    0.000 module.py:250(__init__)
                    100    0.002    0.000    0.003    0.000 level.py:16(<dictcomp>)
                  39207    0.003    0.000    0.003    0.000 {built-in method builtins.hash}
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                    4/1    0.000    0.000    0.003    0.003 __init__.py:144(_lazy_init)
                  16892    0.003    0.000    0.003    0.000 layer.py:190(grid)
                      1    0.002    0.002    0.002    0.002 {built-in method torch._C._cuda_init}
                      1    0.002    0.002    0.002    0.002 layers.py:529(__init__)
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                  21000    0.002    0.000    0.002    0.000 level.py:39(<lambda>)
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                   2190    0.001    0.000    0.002    0.000 types.py:171(__get__)
                     33    0.000    0.000    0.002    0.000 activation.py:708(__init__)
                   2228    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                   5273    0.001    0.000    0.002    0.000 {built-in method builtins.isinstance}
                  17891    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                    600    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   8024    0.001    0.000    0.001    0.000 layer.py:154(elements)
                      5    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                   1090    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                     84    0.000    0.000    0.001    0.000 module.py:322(register_parameter)
                    700    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                   2189    0.000    0.000    0.000    0.000 enum.py:659(name)
                      6    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                   1090    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                      1    0.000    0.000    0.000    0.000 layers.py:73(__init__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    648    0.000    0.000    0.000    0.000 enum.py:351(__iter__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                    600    0.000    0.000    0.000    0.000 layer.py:142(clear)
                   3544    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    213    0.000    0.000    0.000    0.000 module.py:1338(children)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     84    0.000    0.000    0.000    0.000 {built-in method _make_subclass}
                    500    0.000    0.000    0.000    0.000 enum.py:354(__len__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                   1492    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632725: <MonsterLevel_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:09 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:12:42 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:12:42 2021
Terminated at Wed May 12 15:12:57 2021
Results reported at Wed May 12 15:12:57 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   5.66 sec.
    Max Memory :                                 10 MB
    Average Memory :                             6.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16374.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   14 sec.
    Turnaround time :                            3708 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 85, in CFagent
    CFagent = CFAgent(env, **defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 171, in __init__
    if a != b:
NameError: name 'a' is not defined


# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     0.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      247177 function calls (246888 primitive calls) in 3.57 seconds

##    Ordered by: cumulative time
   List reduced from 208 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    3.574    3.574 {built-in method builtins.exec}
                      1    0.000    0.000    3.574    3.574 <string>:1(<module>)
                      1    0.000    0.000    3.574    3.574 main.py:80(CFagent)
                      3    0.000    0.000    3.470    1.157 agent.py:16(__init__)
                      3    0.000    0.000    3.469    1.156 network.py:37(__init__)
                      1    0.000    0.000    3.452    3.452 agent.py:109(__init__)
                      9    0.000    0.000    3.452    0.384 module.py:573(to)
                  111/9    0.001    0.000    3.452    0.384 module.py:385(_apply)
                     84    0.000    0.000    3.450    0.041 module.py:667(convert)
                     84    3.448    0.041    3.450    0.041 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.101    0.101 game.py:9(__init__)
                      1    0.000    0.000    0.088    0.088 layers.py:793(update)
                    100    0.001    0.000    0.082    0.001 layers.py:849(restart)
                    100    0.000    0.000    0.073    0.001 level.py:8(__init__)
                    100    0.008    0.000    0.069    0.001 levels.py:428(generate)
                    500    0.005    0.000    0.054    0.000 level.py:41(notUsed)
                  21285    0.030    0.000    0.030    0.000 level.py:32(inverse)
                      9    0.000    0.000    0.017    0.002 network.py:17(__init__)
                    500    0.000    0.000    0.015    0.000 level.py:38(elementsIn)
                    200    0.005    0.000    0.010    0.000 layers.py:36(reset)
                    500    0.005    0.000    0.010    0.000 level.py:39(<listcomp>)
                     42    0.000    0.000    0.009    0.000 init.py:347(kaiming_uniform_)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                      1    0.000    0.000    0.009    0.009 agent.py:39(__init__)
                  38992    0.006    0.000    0.009    0.000 enum.py:646(__hash__)
                      1    0.000    0.000    0.009    0.009 layers.py:751(__init__)
                      5    0.000    0.000    0.009    0.002 layers.py:782(add)
                     84    0.009    0.000    0.009    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                    600    0.001    0.000    0.008    0.000 layer.py:77(restart)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                     18    0.000    0.000    0.007    0.000 conv.py:370(__init__)
                     18    0.001    0.000    0.006    0.000 conv.py:66(__init__)
                      6    0.000    0.000    0.006    0.001 layer.py:61(__init__)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                  27836    0.005    0.000    0.005    0.000 enum.py:352(<genexpr>)
                      6    0.004    0.001    0.005    0.001 layer.py:159(update)
                    500    0.003    0.000    0.005    0.000 {built-in method _functools.reduce}
                     18    0.000    0.000    0.005    0.000 conv.py:114(reset_parameters)
                    500    0.002    0.000    0.005    0.000 random.py:315(sample)
                   1698    0.003    0.000    0.004    0.000 module.py:950(__setattr__)
                   8005    0.003    0.000    0.004    0.000 layer.py:138(add)
                    114    0.001    0.000    0.004    0.000 module.py:250(__init__)
                    100    0.002    0.000    0.003    0.000 level.py:16(<dictcomp>)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                  38992    0.003    0.000    0.003    0.000 {built-in method builtins.hash}
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  16892    0.002    0.000    0.002    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.002    0.002 game.py:30(<setcomp>)
                     41    0.001    0.000    0.002    0.000 game.py:30(<listcomp>)
                      1    0.002    0.002    0.002    0.002 layers.py:529(__init__)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                  21000    0.002    0.000    0.002    0.000 level.py:39(<lambda>)
                      1    0.002    0.002    0.002    0.002 {built-in method torch._C._cuda_init}
                   2228    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                     33    0.000    0.000    0.002    0.000 activation.py:708(__init__)
                   5273    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                  17870    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                    600    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   8017    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   2190    0.001    0.000    0.001    0.000 types.py:171(__get__)
                     84    0.001    0.000    0.001    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                   1090    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                      5    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                     42    0.000    0.000    0.001    0.000 init.py:337(_calculate_correct_fan)
                     18    0.000    0.000    0.000    0.000 flatten.py:34(__init__)
                    272    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
                    700    0.000    0.000    0.000    0.000 layers.py:799(<genexpr>)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                   1090    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                    648    0.000    0.000    0.000    0.000 enum.py:351(__iter__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                   3529    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                    213    0.000    0.000    0.000    0.000 module.py:1338(children)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                      6    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                      1    0.000    0.000    0.000    0.000 layers.py:73(__init__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    500    0.000    0.000    0.000    0.000 enum.py:354(__len__)
                   2189    0.000    0.000    0.000    0.000 enum.py:659(name)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                      2    0.000    0.000    0.000    0.000 {built-in method zeros}
                     31    0.000    0.000    0.000    0.000 module.py:1227(_named_members)
                    600    0.000    0.000    0.000    0.000 layer.py:142(clear)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632768: <MonsterLevel_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:39 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:14:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:14:11 2021
Terminated at Wed May 12 15:14:24 2021
Results reported at Wed May 12 15:14:24 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   4.75 sec.
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16380.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   7 sec.
    Turnaround time :                            3645 sec.

The output (if any) is above this job summary.

