
# Parameters

    Name :                      MagicalLights2_convert3_TEST-1
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      60526672814 function calls (60254621163 primitive calls) in 86116.27 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.269 86116.269 {built-in method builtins.exec}
                      1    4.507    4.507 86116.269 86116.269 <string>:1(<module>)
                      1  321.956  321.956 86111.762 86111.762 main.py:79(CFagent)
                8496405   34.135    0.000 27853.860    0.003 agent.py:29(learn)
                8496402  689.778    0.000 23252.887    0.003 learner.py:42(Qlearn)
                2832135   13.668    0.000 18839.355    0.007 game.py:41(step)
                2832135   17.206    0.000 18108.937    0.006 layers.py:718(step)
        304161237/32111277 1355.064    0.000 12236.829    0.000 module.py:866(_call_impl)
                2832135  257.501    0.000 12006.749    0.004 layers.py:17(step)
              283213500  814.984    0.000 11722.371    0.000 layer.py:98(move)
               23614875   71.426    0.000 11493.477    0.000 network.py:27(forward)
               23614875  358.540    0.000 11265.168    0.000 container.py:117(forward)
                2832135  315.557    0.000 10738.804    0.004 agent.py:54(_learn)
                2832135 1264.821    0.000 10717.709    0.004 agent.py:212(counterfact)
                2832135  313.644    0.000 9965.509    0.004 agent.py:204(_learn)
                8496402   78.281    0.000 9889.490    0.001 optimizer.py:84(wrapper)
                8496402   37.856    0.000 9518.031    0.001 grad_mode.py:24(decorate_context)
                8496402  283.553    0.000 9395.070    0.001 adam.py:55(step)
                8496402 1936.450    0.000 8804.121    0.001 _functional.py:53(adam)
              283213500 1383.827    0.000 7369.824    0.000 layers.py:735(check)
                2832135   89.790    0.000 7095.043    0.003 agent.py:117(_learn)
                2832135 3334.142    0.001 6259.094    0.002 replaybuffer.py:28(teleporter_save_data)
                2832136  428.857    0.000 6061.284    0.002 layers.py:684(update)
                7558049  213.644    0.000 5944.002    0.001 agent.py:49(__call__)
                8496402   37.661    0.000 5779.555    0.001 tensor.py:195(backward)
                8496402   33.876    0.000 5740.475    0.001 __init__.py:68(backward)
                8496402 5498.599    0.001 5498.599    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2832135 3126.027    0.001 5349.161    0.002 agent.py:88(interveen)
               46714597 5075.742    0.000 5075.742    0.000 {built-in method tensor}
                2832135 3988.549    0.001 4984.008    0.002 replaybuffer.py:22(sample_data)
               40148192   30.865    0.000 4873.152    0.000 game.py:37(board)
                2832135 3777.205    0.001 4740.493    0.002 replaybuffer.py:67(sample_data)
               47229750  116.368    0.000 4034.948    0.000 conv.py:398(forward)
               56642710 2346.455    0.000 3941.774    0.000 layer.py:151(update)
               47229750   71.641    0.000 3867.493    0.000 conv.py:390(_conv_forward)
               47229750 3795.852    0.000 3795.852    0.000 {built-in method conv2d}
               65180355  142.793    0.000 3274.593    0.000 linear.py:93(forward)
                1896157   45.913    0.000 3102.211    0.002 agent.py:176(choose_action)
               65180355   57.758    0.000 3062.603    0.000 functional.py:1737(linear)
               65180355 2989.727    0.000 2989.727    0.000 {built-in method torch._C._nn.linear}
              283213500  610.072    0.000 2966.749    0.000 layers.py:729(isFree)
              192850315 2738.105    0.000 2738.105    0.000 {built-in method clone}
                2832135 1839.447    0.001 2732.234    0.001 agent.py:67(modify)
             2693489113 1915.408    0.000 2356.677    0.000 layer.py:95(isFree)
               88795230   75.149    0.000 1826.192    0.000 activation.py:713(forward)
              158599500 1805.608    0.000 1805.608    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               88795230   80.726    0.000 1751.043    0.000 functional.py:1364(leaky_relu)
               38711519 1722.510    0.000 1722.510    0.000 {built-in method cat}
                2832135 1264.785    0.000 1694.596    0.001 replaybuffer.py:73(CF_save_data)
               88795230 1653.369    0.000 1653.369    0.000 {built-in method torch._C._nn.leaky_relu}
               10390184   77.121    0.000 1625.219    0.000 agent.py:59(modify_board)
                4266419   53.631    0.000 1610.423    0.000 layers.py:740(restart)
              158599500 1584.733    0.000 1584.733    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2832132   53.769    0.000 1555.680    0.001 agent.py:172(__call__)
             5582739795 1039.092    0.000 1498.887    0.000 enum.py:646(__hash__)
                2832135   49.844    0.000 1454.679    0.001 agent.py:112(__call__)
                8496402  229.818    0.000 1382.587    0.000 optimizer.py:189(zero_grad)
              281779317  306.413    0.000 1345.174    0.000 {built-in method builtins.any}
              283213500  850.945    0.000 1149.656    0.000 layers.py:77(check)
                4266419   23.708    0.000 1132.229    0.000 level.py:8(__init__)
              283213500  694.305    0.000 1100.890    0.000 layers.py:246(check)
             3068418991  858.235    0.000 1038.761    0.000 layers.py:700(<genexpr>)
               10390184 1028.700    0.000 1028.700    0.000 {built-in method torch._C._nn.one_hot}
              283213500  625.144    0.000 1009.149    0.000 layers.py:286(check)
               79299750  981.722    0.000  981.722    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4266419  146.605    0.000  923.705    0.000 levels.py:199(generate)
             1172741798  902.098    0.000  902.098    0.000 layer.py:146(elements)
               79299750  845.878    0.000  845.878    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               79299750  820.667    0.000  820.667    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               79299750  803.141    0.000  803.141    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             7021931030  781.813    0.000  781.813    0.000 layer.py:91(positions)
                2832135   59.553    0.000  778.562    0.000 replaybuffer.py:18(stacker)
                2832132   59.632    0.000  753.524    0.000 replaybuffer.py:63(stacker)
              206072631  701.696    0.000  701.696    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2832135  386.966    0.000  638.109    0.000 collector.py:46(collect)
                8532838   73.046    0.000  633.256    0.000 level.py:41(notUsed)
               79299750  624.396    0.000  624.396    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7558049  225.226    0.000  615.164    0.000 exploration.py:53(softmaxer)
              283213500  462.549    0.000  608.308    0.000 layers.py:62(check)
        7452800194/7452800191  534.534    0.000  595.655    0.000 {built-in method builtins.len}
                1896157  502.734    0.000  533.952    0.000 agent.py:187(convert_values)
              283213500  341.354    0.000  524.948    0.000 layers.py:273(check)
              283213500  318.498    0.000  519.297    0.000 layers.py:313(check)
              555098334  413.686    0.000  510.465    0.000 tensor.py:906(grad)
               14197108  184.020    0.000  484.687    0.000 random.py:315(sample)
              283213500  299.132    0.000  460.765    0.000 layers.py:48(check)
             5582772194  459.802    0.000  459.802    0.000 {built-in method builtins.hash}
                8496402   13.326    0.000  450.021    0.000 loss.py:527(forward)
              283213600   64.461    0.000  444.413    0.000 {built-in method builtins.all}
                8496402   35.070    0.000  436.695    0.000 functional.py:2898(mse_loss)
              655179198  166.437    0.000  416.419    0.000 layers.py:690(<genexpr>)
               42664190   58.213    0.000  409.734    0.000 layer.py:69(restart)
              285718833  257.442    0.000  339.736    0.000 layer.py:126(remove)
              283213500  220.506    0.000  327.435    0.000 layers.py:23(check)
              531510790  224.337    0.000  304.943    0.000 layer.py:130(add)
               47229750   34.794    0.000  301.871    0.000 flatten.py:39(forward)
                8496402  287.129    0.000  287.129    0.000 {built-in method torch._C._nn.mse_loss}
               16992810  268.165    0.000  268.165    0.000 {built-in method sum}
               47229750  267.078    0.000  267.078    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                5664272  261.067    0.000  261.067    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9572852: <MagicalLights2_convert3_TEST_1> in cluster <dcc> Done

Job <MagicalLights2_convert3_TEST_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 26 00:55:52 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 26 01:05:41 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 01:05:41 2021
Terminated at Tue Apr 27 01:01:08 2021
Results reported at Tue Apr 27 01:01:08 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
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

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85902.34 sec.
    Max Memory :                                 8553 MB
    Average Memory :                             5855.48 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7831.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86128 sec.
    Turnaround time :                            86716 sec.

The output (if any) is above this job summary.

