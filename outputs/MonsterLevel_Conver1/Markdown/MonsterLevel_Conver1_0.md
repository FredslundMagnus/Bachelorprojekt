
# Parameters

    Name :                      MonsterLevel_Conver1-0
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      61656662267 function calls (61382704004 primitive calls) in 86123.82 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.818 86123.818 {built-in method builtins.exec}
                      1    4.493    4.493 86123.818 86123.818 <string>:1(<module>)
                      1  322.107  322.107 86119.325 86119.325 main.py:79(CFagent)
                8057823   32.084    0.000 26599.005    0.003 agent.py:29(learn)
                8057823  660.933    0.000 22196.501    0.003 learner.py:42(Qlearn)
                2685941   12.919    0.000 21083.587    0.008 game.py:41(step)
                2685941   16.487    0.000 20489.075    0.008 layers.py:718(step)
        305739423/31782851 1376.584    0.000 12386.954    0.000 module.py:866(_call_impl)
               23725028   68.720    0.000 11661.024    0.000 network.py:27(forward)
               23725028  370.443    0.000 11431.293    0.000 container.py:117(forward)
                2685941  255.852    0.000 10320.538    0.004 layers.py:17(step)
                2685941  303.522    0.000 10247.158    0.004 agent.py:54(_learn)
                2685942  440.334    0.000 10129.647    0.004 layers.py:684(update)
              267087148  818.897    0.000 10039.291    0.000 layer.py:98(move)
                2685941  300.541    0.000 9526.188    0.004 agent.py:204(_learn)
                8057823   73.245    0.000 9423.795    0.001 optimizer.py:84(wrapper)
                2685941 1590.909    0.001 9240.706    0.003 agent.py:212(counterfact)
                8057823   37.773    0.000 9069.336    0.001 grad_mode.py:24(decorate_context)
                8057823  261.483    0.000 8950.269    0.001 adam.py:55(step)
                8057823 1840.819    0.000 8398.103    0.001 _functional.py:53(adam)
                2685941   84.976    0.000 6776.108    0.003 agent.py:117(_learn)
              267087148  910.601    0.000 6769.696    0.000 layers.py:735(check)
                7833555  225.282    0.000 6174.199    0.001 agent.py:49(__call__)
                2685941 3305.670    0.001 6159.708    0.002 replaybuffer.py:28(teleporter_save_data)
                8057823   35.365    0.000 5501.276    0.001 tensor.py:195(backward)
                8057823   32.938    0.000 5464.623    0.001 __init__.py:68(backward)
                8057823 5234.429    0.001 5234.429    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2685941 3078.848    0.001 5193.290    0.002 agent.py:88(interveen)
                8436408   73.033    0.000 4891.998    0.001 layers.py:740(restart)
                2685941 3897.360    0.001 4838.661    0.002 replaybuffer.py:22(sample_data)
                2685941 3867.528    0.001 4787.005    0.002 replaybuffer.py:67(sample_data)
                8436408   36.803    0.000 4146.597    0.000 level.py:8(__init__)
               47450056  111.760    0.000 4067.788    0.000 conv.py:398(forward)
              267087148 2220.429    0.000 3907.646    0.000 layers.py:538(check)
                2461768   60.216    0.000 3907.067    0.002 agent.py:176(choose_action)
               47450056   67.858    0.000 3901.966    0.000 conv.py:390(_conv_forward)
               47450056 3834.108    0.000 3834.108    0.000 {built-in method conv2d}
                8436408  661.883    0.000 3782.488    0.000 levels.py:413(generate)
               65803202  145.362    0.000 3334.367    0.000 linear.py:93(forward)
               65803202   61.445    0.000 3117.380    0.000 functional.py:1737(linear)
               32231298 2049.825    0.000 3097.730    0.000 layer.py:151(update)
               65803202 3041.242    0.000 3041.242    0.000 {built-in method torch._C._nn.linear}
               38630132 2999.446    0.000 2999.446    0.000 {built-in method tensor}
              211838742 2961.684    0.000 2961.684    0.000 {built-in method clone}
               32385699   26.939    0.000 2810.249    0.000 game.py:37(board)
                2685941 1963.759    0.001 2749.925    0.001 replaybuffer.py:73(CF_save_data)
                2685941 1882.371    0.001 2729.997    0.001 agent.py:67(modify)
               42182040  398.951    0.000 2471.847    0.000 level.py:41(notUsed)
              268829787  215.411    0.000 1968.263    0.000 {built-in method builtins.any}
               89528230   83.125    0.000 1863.757    0.000 activation.py:713(forward)
              267087148  360.834    0.000 1857.559    0.000 layers.py:729(isFree)
               89528230   80.160    0.000 1780.633    0.000 functional.py:1364(leaky_relu)
             1845048756  560.097    0.000 1753.650    0.000 layers.py:700(<genexpr>)
              150412696 1727.178    0.000 1727.178    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               89528230 1684.211    0.000 1684.211    0.000 {built-in method torch._C._nn.leaky_relu}
               37378906 1676.158    0.000 1676.158    0.000 {built-in method cat}
               10519496   76.868    0.000 1647.042    0.000 agent.py:59(modify_board)
             6013054869 1138.868    0.000 1623.294    0.000 enum.py:646(__hash__)
              150412696 1502.535    0.000 1502.535    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1536462520 1227.692    0.000 1496.725    0.000 layer.py:95(isFree)
                2685941   50.463    0.000 1495.147    0.001 agent.py:172(__call__)
                2685941   46.942    0.000 1392.638    0.001 agent.py:112(__call__)
                8057823  211.903    0.000 1313.416    0.000 optimizer.py:189(zero_grad)
              266143845  681.130    0.000 1082.084    0.000 layers.py:575(isDead)
               42182040   34.516    0.000 1073.429    0.000 level.py:38(elementsIn)
               10519496 1043.731    0.000 1043.731    0.000 {built-in method torch._C._nn.one_hot}
              267087148  669.266    0.000  941.766    0.000 layers.py:77(check)
               75206348  939.169    0.000  939.169    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               75206348  812.402    0.000  812.402    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               47553922  308.477    0.000  795.873    0.000 random.py:315(sample)
               75206348  779.683    0.000  779.683    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75206348  771.036    0.000  771.036    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              225044179  755.276    0.000  755.276    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2685941   49.440    0.000  735.110    0.000 replaybuffer.py:18(stacker)
                2685941   50.834    0.000  720.217    0.000 replaybuffer.py:63(stacker)
              387747913  134.971    0.000  699.064    0.000 random.py:244(randint)
               42182040  340.969    0.000  689.172    0.000 level.py:39(<listcomp>)
             1799650959  679.086    0.000  679.086    0.000 level.py:32(inverse)
             2062289995  672.890    0.000  672.890    0.000 layer.py:146(elements)
              268594200   64.951    0.000  664.403    0.000 {built-in method builtins.all}
               50618448   66.612    0.000  654.218    0.000 layer.py:69(restart)
                7833555  234.636    0.000  638.691    0.000 exploration.py:53(softmaxer)
              844555463  445.798    0.000  637.779    0.000 random.py:250(_randbelow_with_getrandbits)
              589078504  150.054    0.000  636.907    0.000 layers.py:690(<genexpr>)
                2685941  367.133    0.000  608.218    0.000 collector.py:46(collect)
               75206348  594.577    0.000  594.577    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1009633169  421.584    0.000  569.980    0.000 layer.py:130(add)
              387747913  233.936    0.000  564.093    0.000 random.py:200(randrange)
             5806493181  558.838    0.000  558.838    0.000 layer.py:91(positions)
                2461768  557.720    0.000  557.720    0.000 agent.py:187(convert_values)
              623109224  358.746    0.000  536.156    0.000 layer.py:126(remove)
              267087148  333.331    0.000  495.382    0.000 layers.py:48(check)
              526444520  389.267    0.000  484.681    0.000 tensor.py:906(grad)
             6013085588  484.431    0.000  484.431    0.000 {built-in method builtins.hash}
              268594200  327.790    0.000  477.206    0.000 layers.py:113(isDone)
                8436508  231.425    0.000  457.991    0.000 layers.py:36(reset)
        4550476029/4550476026  382.499    0.000  442.987    0.000 {built-in method builtins.len}
              267087148  149.383    0.000  434.462    0.000 layers.py:572(<listcomp>)
                8057823   12.864    0.000  428.418    0.000 loss.py:527(forward)
                8057823   35.940    0.000  415.554    0.000 functional.py:2898(mse_loss)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579178: <MonsterLevel_Conver1_0> in cluster <dcc> Done

Job <MonsterLevel_Conver1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:08 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May  1 18:59:02 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  1 18:59:02 2021
Terminated at Sun May  2 18:54:39 2021
Results reported at Sun May  2 18:54:39 2021

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

    CPU time :                                   85902.23 sec.
    Max Memory :                                 8541 MB
    Average Memory :                             5961.50 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7843.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86136 sec.
    Turnaround time :                            490231 sec.

The output (if any) is above this job summary.

